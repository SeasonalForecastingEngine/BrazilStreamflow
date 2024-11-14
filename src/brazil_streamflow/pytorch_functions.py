
import numpy as np

import os
import optuna
import torch

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.utils.data import Dataset

from ignite.engine import Engine, Events
from ignite.metrics import Loss
from ignite.handlers import Checkpoint, ModelCheckpoint, EarlyStopping


device = torch.device("cpu")
criterion = nn.MSELoss()


class MyDataset(Dataset):
    def __init__(self, Idc, Idm, X, y=None):
        self.Idc = Idc.astype('int32')
        self.Idm = Idm.astype('int32')
        self.X = X.astype('float32')
        if y is not None:
            self.y = y.astype('float32')
        else:
            self.y = None
        
    def __getitem__(self, idx):
        if self.y is not None:
            return [self.Idc[idx], self.Idm[idx], self.X[idx], self.y[idx]]
        else:
            return [self.Idc[idx], self.Idm[idx], self.X[idx]]
        
    def __len__(self):
        return len(self.X)


class MyMLP(nn.Module):
    def __init__(self, args):
        super(MyMLP, self).__init__()
        self.embc = nn.Embedding(int(args['n_catchments']), int(args['emb_dim_catchments']))
        self.embm = nn.Embedding(12, int(args['emb_dim_months']))
        self.fc1c = nn.Linear(int(args['emb_dim_catchments']), int(args['hidden_1']))
        self.fc1m = nn.Linear(int(args['emb_dim_months']), int(args['hidden_1']))
        self.fc2 = nn.Linear(int(args['hidden_1']), int(args['hidden_2']))
        self.fc3 = nn.Linear(int(args['hidden_2']), int(args['n_features']))
        self.dropout = nn.Dropout(args['drpt_rate'])
        
    def forward(self, Idc, Idm, X):
        x = self.embc(Idc)
        x = F.elu(self.fc1c(x))
        y = self.embm(Idm)
        y = F.elu(self.fc1m(y))
        z = torch.mul(x, y)
        z = F.elu(self.fc2(z))
        z = self.dropout(z)
        beta = F.elu(self.fc3(z))
        output = torch.sum(torch.mul(X, beta), 1)
        return output


def objective(trial, fixed_args, train_loader, val_loader):
    args = {'n_features': fixed_args['n_features'],
        'n_catchments': fixed_args['n_catchments'],
        'emb_dim_catchments': trial.suggest_int("emb_dim_catchments", 3, 6),
        'emb_dim_months': trial.suggest_int("emb_dim_months", 1, 3),
        'hidden_1': trial.suggest_int("hidden_1", 10, 40, step=5),
        'hidden_2': trial.suggest_int("hidden_2", 10, 40, step=5),
        'drpt_rate': trial.suggest_categorical("drpt_rate", [0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
    }
    
    model = MyMLP(args).to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.005)
    
    for epoch in range(30):
        model.train()
        for Idc, Idm, X, y in train_loader:
            Idc, Idm, X, y = Idc.to(device), Idm.to(device), X.to(device), y.to(device)
            optimizer.zero_grad()
            y_pred = model(Idc, Idm, X)
            loss = criterion(y_pred, y)
            loss.backward()
            optimizer.step()
            
        model.eval()
        valid_loss = 0.0
        with torch.no_grad():
            for Idc, Idm, X, y in val_loader:
                Idc, Idm, X, y = Idc.to(device), Idm.to(device), X.to(device), y.to(device)
                y_pred = model(Idc, Idm, X)
                loss = criterion(y_pred, y)
                valid_loss += loss.item()
                
        valid_loss = valid_loss / len(val_loader.dataset)
        
        trial.report(valid_loss, epoch)
        if trial.should_prune():
            raise optuna.exceptions.TrialPruned()
            
    return valid_loss


