# python_dyp_laering
Template for deep learning projects

## Installasjon av Python og conda
For å komme i gang trenger vi to ting installert. Python og conda. Python er et programmeringspråk som f.eks. kan installeres via bedriftsportalen. Conda er et program som hjelper deg med å installere Python- (og R-) pakker riktig. I tillegg har conda en ekstra funksjon: virituelle miljøer. Man kan installere disse separat, men det er enklere å installere begge deler på en gang ved å laste ned (og installere) Anaconda, miniconda eller mini-forge. Dette er tre "pakker" som innerholder ulike ting. Alle tre innerholder Python og conda, men Anaconda innerholder i tillegg masse pakker og et grafisk brukergrensesnitt (Anaconda Navigator) for conda. Miniconda og mini-forge innerholder bare python og conda (og et par pakker de trenger), men hvilken kanal conda bruker for å laste ned pakker er ulikt for miniconda og mini-forge. Mer om dette i "Copyright og lisenser".

På grunn av lisenser (se neste delavsnitt), anbefaler jeg å installere mini-forge. Denne installeres fra [mini-forge sin github side](https://github.com/conda-forge/miniforge). For å installere Anaconda eller mini-conda gå til [hjemmesiden til Anaconda](https://docs.anaconda.com/distro-or-miniconda/) og velg den relevante installasjonen. Si ja til alt under installasjon, men se kommentaren under for installasjon på Windows!

**Obs!**
Når man installerer miniconda og Anaconda (usikker på conda-forge) på Windows må man på et tidspunkt svare på om man vil "Add anaconda path to my PATH". Det blir anbefalt å svare nei på dette spørsmålet i installasjonen. Hvis man ikke legger til i PATH, kan man ikke bruke conda eller python i terminalen fordi disse ikke blir gjennkjent som kommandoer. Man må da bruke Windows PowerShell eller Anaconda prompt til å kjøre programmer. Dette er upraktisk. Jeg anbefaler å si ja til å legge til anaconda path til PATH. 

#### Installasjon på servere
Hvis man skal kjøre ting på serverene (samba8 osv), må man installere conda og python der også. For å gjøre dette, bruker man ssh til å komme seg inn på serveren og installerer deretter slik som ovenfor, men husk at serverene har Linux som operativsystem! Følg derfor installasjonsinstrukser for Linux.

Hvis du bruker en Windows-terminal til å ssh-e deg inn på serverene kan det skje noe litt rart. Når man installerer conda og python slik som ovenfor legges conda til i et bash script som kjøres når en ny bash session åpnes. Dette gjør at systemet gjenkjenner kommentarer som conda og python. Alle nye bash sessions skal derfor gjenkjenne conda komandoen. Hvis man ssh-er inn på serverene gjennom en Windows terminal, åpnes imidlertid ikke en vanlig bash-sesjon. Istedenfor åpnes en "inloggingssesjon" og denne kjører ikke bash scriptet som gjør at conda blir gjennkjent som en kommando automatisk. Den enkleste måten å løse dette på er ved å ssh-e inn på serverene gjennom noe annet enn en Windows terminal (f.eks. gjennom Visual Studio code sin ssh-funksjon). En annen og mer komplisert løsning er å modifisere en fil ved navn .bash_profile slik at bash scriptet som sørger for at conda-kommandoen blir gjenkjent kjøres automatisk. Dette kan gjøres ved å kjøre følgende kommando inne på serveren (altså etter man har ssh-et inn):
```
echo 'if [ -f "${HOME}/.bashrc" ]; then
    . "${HOME}/.bashrc"
fi' >> .bash_profile
```
### Copyright og lisenser
Conda er gratis å bruke og krever ingen lisens, men pakkene den henter når du ber den installere pakker kan fortsatt være beskyttet av copyright. Dette gjelder for standard kanalen til conda, kanalen som henter pakker fra Anaconda sine servere. Disse er underlagt en lisens og kan ikke brukes gratis uten videre. En klausul i avtalen sier at standard-kanalen kan brukes av bedrifter/stiftelser med mindre enn 200 ansatte, så å bruke denne kanalen skal være uproblematisk for NR, men hvis man vil være på den sikre siden går det an å bruke en alternativ kanal f.eks. conda-forge. Denne er gratis å bruke, men vedlikeholdes av ildsjeler på internett. Hvem som helst kan derfor jobbe med conda-forge, så om man har veldig sensitiv data, kan det være en ide å heller bruke conda sin standard kanal.

Hvis mini-forge ble installert, er conda-forge satt automatisk som conda sin kanal. Hvis miniconda eller Anaconda installeres, er Anaconda sin standard kanal satt som condas kanal. For å sjekke hvilken kanal som brukes, skriv det følgende i terminalen:

```console
conda config --show channels
```

For å legge til conda-forge som en kanal, skriv:

```console
conda config --add channels conda-forge
```

Da blir conda-forge satt på topp av conda sin prioriteringsliste og conda kommer til å lete i denne kanalen først. For å fjerne conda-forge som en kanal, skriv:

```console
conda config --remove channels conda-forge
```

### Hvorfor kan jeg ikke bruke Poetry?
Du kan bruke Poetry istedenfor conda, men det er visst vanskelig å installere Pytorch riktig med poetry, særlig hvis man vil få kjørt ting på gpu-er.

### Kan jeg bruke conda med R?
Ja, conda fungerer med R, men i denne guiden kommer jeg til å bruke Python.

## Hva er conda og hvordan bruker jeg det?
La oss begynne med hva conda ikke er. Conda er ikke Python eller R eller noe annet programmeringsspråk. Det er heller ikke det samme som Anaconda eller miniconda eller mini-forge. Conda er bare en av flere programmer som blir installert når du installerer en av disse "pakkene". Det conda er, er et program som gjør to ting: 1. conda kan brukes til å installere og holde styr på Python-pakker og 2. conda kan brukes til å lage og jobbe med virituelle miljøer.

### 1.
Python-pakker kan installeres på mange måter (f.eks. ved hjelp av pip), og strengt tatt trenger man ikke conda for å gjøre dette. Når det er sagt, er det ofte mye enklere sagt enn gjort å installere python-pakker. Flere pakker avhenger av hverandre og noen pakker overskriver kanskje hverandre. Man kan bruke pip og holde styr på alt dette selv, men ved å bruke conda, heller enn pip, til å installere pakkene, gjøres dette automatisk og alle avhengigheter holdes styr på av conda.

### 2.
Et virituelt miljø er en slags isolert installasjon av Python + pakker. Man kan opprette mange ulike virituelle miljøer og hvert enkelt ett kan ha ulike versjoner av python (eller R) installert. Dette er nyttig hvis man plutselig trenger å sjekke ut hvordan noe fungerer på en gammel versjon av Python, men virituelle miljøer er ikke bare nyttig for å jobbe med utdaterte versjoner av et programmeringsspråk. På hvert enkelt virituelle miljø kan man installere ulike kombinasjoner av pakker. Ved å laste inn miljøene, kan man derfor jobbe på "ulike" installasjoner av Python med ulike pakker installert. Du kan altså ha et virituellt miljø med Python+pakker som er nyttige for maskinlæring installert og et annet med Python + kun standardpakker som numpy og matplotlib installert. Hvis alle maskinlæringspakkene trengs, kan det første miljøet aktiveres, men om ikke alt dette er nødvendig, kan man aktivere det andre miljøet.

Hvis du har et virituelt miljø som heter `env`, kan du aktivere det ved å skrive det følgende i terminalen:
```
conda activate env
```
Når env er aktivert, vil denne terminalen oppføre seg som om alt som er installert på env er installert på maskinen. Så hvis env innerholder en gammel versjon av python + numpy og matplolib, vil du kunne kjøre programmer gjennom denne terminalen som om du har denne gamle versjonen av python samt numpy og matplolib installert. Miljøer kan også brukes andre steder enn i terminalen. Når man f.eks. kjører Jupyter Notebooks, kan man velge å kjøre det med et miljø aktivert.

Når man installerer Python gjennom å installere miniconda, Anaconda eller mini-forge, blir Python installert direkte på datamaskinen. Pakker kan deretter installeres direkte "oppå" denne python installasjonen. Det er derfor ikke strengt tatt nødvendig å bruke virituelle miljøer, men man har mye mer kontroll når man bruker dette verktøyet. Hvis programmet ditt fungerer i et miljø med bare python og numpy installer, kommer det mest sannsynlig til å fungere på andre folk sine pc-er. Hvis man istedenfor installerer alle pakkene direkte på systemet, blir lista med installerte pakker og deres avhenigheter fort ganske stor, og hvorvidt et program kjører likt på andres pc-er blir mye vanskeligere å vurdere. Jeg anbefaler derfor å kunn ha standard Python installert direkte på maskinens system. Hvis pakker skal installeres, er det best å lage et virituellt miljø og installere dem der.

### Praktiske kommandoer
#### conda info --envs
```
conda info --envs
```
Gir deg en liste over tilgjenglige miljøer.

#### conda create
```
conda create -n <navn på miljøet> python=<ønsket python versjon> <pakke 1> <pakke 2> ... <pakke n>
```
Dette lager et miljø med den ønskede python versjonen + de pakkene man skriver opp installert. python = <ønsket python versjon> kan sløyfes. Da velger conda selv hvilken versjonen den skal bruke. Man kan også si hvilken versjon av pakkene man vil ha ved å legge til en =<ønsket versjon> etter pakken.

Eks:
```
conda create env python=3.9 numpy scipy=0.17.3 matplotlib
```

#### conda activate
```
conda activate <navn på miljøet>
```
Denne kommandoen aktiverer miljøet med navn `<navn på miljøet>`. Terminalen vil nå oppføre seg som om alt som er installert på dette miljøet er installert på maskinen. Når et miljø er aktivert dukker det opp foran filplasseringa i terminalen:
```
(<navn på miljøet>) C:\mappe1\mappe2>
```

#### conda deactivate
```
conda deactivate <navn på miljøet>
```
Kommandoen deaktiverer miljøet du er i og sender deg tilbake til systemet på maskinen din. 

***Obs!***
Hvis du har aktivert et miljø og vil bytte til et annet, kan du bare aktivere det direkte. Du trenger ikke å deaktivere miljøet du er i først. Conda bytter om for deg

#### conda install
```
conda install <pakke 1> <pakke 2> ... <pakke n>
```
Denne kommandoen installere pakker direkte på det aktive miljøet. Så hvis du først aktiverer et miljø og så bruker `conda install` vil du installere på miljøet du aktiverte.

***Obs!***
Denne komandoen fungerer også direkte på maskinen, så sørg for å være i riktig miljø før du bruker den.

Hvis du vil installere pakker på et miljø som ikke nødvendigvis trenger å være det aktive, skriv
```
conda install -n <navn på miljø> <pakke 1> <pakke 2> ... <pakke n>
```

#### conda list
```
conda list
```
Lister alle installerte pakker på det aktive miljøet. Hvis du vil se hva som er installert på et spesifikt miljø, skriv
```
conda list -n <navn på miljø>
```

#### conda remove
```
conda env remove --name <navn på miljø>
```
Sletter det spesifiserte miløjet.

### Ting å tenke på
Ikke installer pakker direkte på systemet ditt. Installer heller inn i et conda miljø og last dette. Dette fører som regel til færre problemer.

Installer så mange pakker du kan på en gang. Dette gjør det lettere for conda å håndtere alle avhenigheter.

Hvis enkelte pakker ikke er tilgjengelig med conda. Installer alt du kan med conda først og installer resten med pip til slutt. Dette fører som reglel til færre problemer.

### Conda-miljø for dyp læring
Jeg har lagd et miljø som har alle pakkene vi kommer til å trenge. Det heter pytorch_env og er lagret i filen `environment.yml`. Dere kan enten ta dette i bruk ved å laste ned fila og skrive det følgende i terminalen

```
conda env create -f environment.yml
```

Dette lager et miljø som heter pytorch_env, som dere kan aktivere og bruke. Si ja til alt. Eventuelt så kan dere lage deres eget conda miljø og installere disse pakkene:

1. numpy (for generell matte)
2. scipy (for generell matte)
3. matplotlib og seaborn (for plotting)
4. pytorch (for dyp læring) (se [nettsidene til Pytorch](https://pytorch.org/get-started/locally/) for hvordan man installerer med mulighet for å kjøre på gpu)
5. ipykernel (for Jupyter notebooks)

Det vil gi samme resultat.

## Jupyter notebook
Vi kommer til å bruke Jupyter notebook. Det har ingenting med dyp læring å gjøre, men et veldig nyttig verktøy for å prøve ut kommandoer. I tillegg kan man enkelt kobinere tekst og kode i Jupyter notebooks.

En Jupyter notatbok har filendelsen .ipynb og en slags interaktiv måte å skrive kode på. I en notatbok kan man legge til kode- og tekstblokker om hverandre, og hver enkelt kodeblokk kan kjøres for seg (dette gjøres enkelt ved å trykke `shift+enter` inne i en kodeblokk). Plot og utskrifter vises underveis ettersom man kjører kodeblokkene. Jeg tenker på Jupyter Notebooks litt som Pythons versjon av RStudio. Det er veldig nyttig for å prøve ut kommandoer eller modeller ettersom du kan kjøre deler av scriptet for seg.

Hvis man har Visual Studio code installert, kan man åpne Jupyter Notebooks i dette programmet. Hvis man ikke har installert dette programmet, kan man istedenfor starte programmet Jupyter Notebook som skal være installert på pcen hvis installasjonsstegene over har blitt fulgt riktig. Dette kan gjøres fra terminalen ved å skrive `jupyter notebook` eller ved å søke gjennom installerte programmer og starte det som heter Jupyter Notebook. Når programmet startes, vil en nettside åpnes og på denne nettsiden kan man bla seg fram til notatboka man ønsker å kjøre ved å manøvrere filsystemet som dukker opp. Eventuelt kan man først bruke terminalen til å navigere seg fram til mappa der notatboka ligger og skrive
```
Jupyter Notebook <navn på notatboka>
```
i terminalen. Dette åpner den relevante notatboka i et vindu i netteleseren.

### Velge en kjerne
Jupyter Notebook kjører koden for oss. Programmet må derfor vite hva slags Python installasjon det skal bruke og hvilke pakker som skal være installert her. Dette kalles "kernel" i Jupyter Notebook. Siden et conda-miljø innerholder en Python installasjon, kan vi bruke disse til å velge en passende kjerne. 

I Visual Studio code er det veldig enkelt å velge kjerne. Man kan sette den ved å trykke på knappen øverst i høyre hjørne med et symbol som ligner på en stemmeseddel (det står `select kernel` om man ikke har valgt en kernel, ellers står det navnet på conda-miljøet man bruker). Eventuelt kan man åpne command pallet ved å trykke `ctrl+shift+p`og skrive inn `Notebook: Select Notebook Kernel`. Deretter trykker man på `Python environments` og velger conda-miljøet man ønsker å bruke.

Hvis man ikke bruker Visual Studio code, men heller starter Jupyter Notebook fra terminalen eller på annet vis, må man fortelle programmet at et conda miljø skal være mulig å bruke som kjerne. Dette gjør man ved å skrive
```
python -m ipykernel install --user --name=<navn på miljøet>
```
i terminalen. I vårt tilfellet er navnet på miljøet `pytorch_env`. Etter å ha kjørt denne kommandoen, skal conda-miljøet være tilgjengelig i Jupyter Notebook. For å bytte kjernen til det ønskede conda-miljøet, trykker man på knappet øverst i høyre hjørne og velger det ønskede miljøet. For meg står det `Python 3 (ipython)` på denne knappen, men det kan også stå noe litt annet der.

## PyTorch
Vi skal bruke PyTorch! Dette er en pakke som er spesielt nyttig for dyp læring, men den har også en del verktøy som kan være praktisk i andre situasjoner også (f.eks. automatisk derivering). Se fila `pytorch_intro.ipynb` for en introduksjon til denne pakka.

## Nevrale nett i PyTorch
PyTorch har implementert mange dype læringsmetoder. Det er derfor ikke nødvendig å tilpasse dem helt fra bunnen av. Se relevante Jupyter Notebooks for introduksjoner! Vi gjennomgår først Feed Forward Neural Networks (FFN) som en introduksjon til PyTorch sin syntaks. Deretter går vi over til Long Short Term Memory nettverk (LSTM), en type Recurrent Neural Network (RNN), som kan brukes for å modelere værdata.

## Værdata

## Dype læringsmodeller for værdata

# To do
1. CNN
2. Ekte data eks med bilder for CNN og FNN (værdata, snakk med Michael)
3. LSTM
4. Ekte data eks (hydrologi data?)