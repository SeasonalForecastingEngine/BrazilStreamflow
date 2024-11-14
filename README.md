# Brazil Streamflow

This repository contains some Jupyter notebooks in which the methodology proposed in the article "Multi-decadal streamflow projections for catchments in Brazil based on CMIP6 multi-model simulations and neural network embeddings for linear regression models" is implemented and illustrated. The specific scripts are:

* *OptimizeHyperparameters.ipynb*: Uses the Optuna hyperparameter optimization framework to find optimal hyperparameters for the neural network regression model.
* *CalculateExplainedVariance.ipynb*: Fits the neural network regression model in leave-one-year-out cross-validation mode and calculates an out of sample coefficient of determination to assess the quality of the fit.
* *CalculateRegressionCoefficients.ipynb*: Fits the neural network regression model to all training data and saves out the resulting regression coefficients.
* *CalculateInflowProjections.ipynb*: Loads climate model output and the regression coefficients calculated in the previous notebook, and generates inflow projections based on them.

The Python packages required to run this code can be installed using the conda package manager and the file "environment.yml", which is also included, via

```
conda env create -f environment.yml
```

