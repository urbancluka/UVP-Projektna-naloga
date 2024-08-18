# UVP-Projektna-naloga

### Luka Urbanč
Namen projekta je pridobiti podatke s HTML [spletne strani](https://www.cars-data.com/en/all-cars.html) in napraviti analizo teh podatkov s pomočjo Pandas. V .py datotekah se nahajajo funkcije, ki se v datoteki `main.py` zložijo v program, ki naloži vse podatke s spletnih strani. Navodila za uporabo programa so napisana spodaj. 

## Navodila za uporabo
### Nameščanje Python-a in git-a
Predvidevam, da že imate Python nameščen na svojem računalniku. če temu ni tako, lahko za namestitev Python-a sledite navodilom na [tej spletni strani](https://www.python.org/downloads/). Alternativna izbira za uporabnike macOS je tudi uporaba Brew-a, za uporabnike Windows operacijskega sistema pa je Python na voljo tudi v Microsoft Store-u. Za nameščanje git-a lahko sledite navodilom [tukaj](https://github.com/git-guides/install-git)

Če niste prepričani, ali je bilo nameščanje uspešno, ali pa se ne spomnite, če je python že nameščen, lahko preverite njegovo različico tako, da v terminal (na macOS ga lahko odpremo z: CMD + Space -> "Terminal" -> Enter) vpišemo 

```console
python --version #verzija Pythona
python3 --version #verzija python3
```

Želimo si tak izpis:
```console 
Python 3.12.2 #Številke se lahko razlikujejo
```

Prav tako lahko preverimo tudi verzijo git-a z naslednjim ukazom:

```console 
git --version
```

Nakar bi nam moral terminal izpisati:
```console 
git version 2.44.0
```

### Nameščanje knjižnic
Pri delu bomo potrebovali tudi nekatera dodatna orodja. Vse lahko enostavno pridobite z ukazom
```console
pip3 install requests pandas numpy seaborn matplotlib
```

### Pridobivanja datotek z git-om
Za uporabo programa morate naložiti vse datoteke na svoj računalnik. Vse dotične datoteke tega programa lahko enostavno namestite tako da poženete naslednji ukaz:
```console 
git clone https://github.com/urbancluka/UVP-Projektna-naloga.git
```

### Uporabljanje programa:
Najprej se moramo prepričati, da se trenutno nahajamo v pravilen direktoriju. Ko smo se prepričali oziroma smo se ustrezno premaknili, lahko začnemo z delom. Za začetek izvajanja programa moramo pognati le `main.py`, kar storimo tako da v terminal vpišemo 

``` console 
python3 main.py
```

Nato moramo le slediti navodilom, ki se izpisujejo v terminalu. Podatki se shranjujejo v mape, a edina zares pomembna je `data.csv`, v kateri se nahajajo podatki, ki nas dejansko zanimajo. 

Zajem podatkov lahko traja nekaj casa. Pri izvajanju na mojem računalniku je zajem podatkov trajal nekje med 30 do 60 minut, odvisno od hitrosti povezave in odgovorov strežnika. Sproti se izpisujejo tudi spletne strani, ki jih shranjuje. Ko nam izpise `Vase datoteke se nahajajo v datoteki 'data.csv'`, je program zaključil z delom. 


### Analiza
Analiza se nahaja v datoteki `analiza.ipynb`, ki jo lahko odpremo s programom za branje Jupyter Notebook-ov. Lažja možnost je, da si jo pogledamo kar na spletu na Github-u. Vsi grafi, rezultati in ugotovitve bodo predstavljene v tisti datoteki. Vse celice so bile pravilno poklicane, zato lahko analizo enostavno preberete brez dodatnega dela. Datoteka je dostopna [na tej povezavi.](https://github.com/urbancluka/UVP-Projektna-naloga/blob/main/analiza.ipynb)



#### Spodnji seznam ni pomemben za uporabnika in je namenjen avtorju
## TODO:
 - [x] Create function to download .html file with correct parameters
 - [x] Decide what website to scrap
 - [x] Write regex function to retrieve data from raw html file
 - [x] Save data to single .csv file
 - [x] Make website inputs a prompt for the user to enter ("enter starting page, enter last page...")
 - [x] Build loop into download_main function
 - [x] Fix power scrapping
 - [x] Fix missing data point in acceleration