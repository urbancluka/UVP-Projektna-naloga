# UVP-Projektna-naloga

### Luka Urbanč
Namen projekta je pridobiti podatke s HTML [spletne strani](https://www.cars-data.com/en/all-cars.html) in napraviti analizo teh podatkov s pomočjo Pandas. V .py datotekah se nahajajo funckije, ki se v datoteki `main.py` zlozijo v program, ki nalozi vse podatke. Navodila za uporabo programa so napisana spodaj. 

## Navodila za uporabo
### Namescanje Python-a in git-a
Predvidevam, da imate Python ze namescen na svojem racunalniku. Ce temu ni tako, lahko za namestitev pythona sledite navodilom na [tej spletni strani](https://www.python.org/downloads/). Alternativna izbira za uporabnike z macOS je tudi uporaba Brew-a, za uporabnika Windows operacijskega sistema pa je Python na voljo tudi v Microsoft Store-u. Za namescanje git-a lahko sledite navodilom [tukaj](https://github.com/git-guides/install-git)

Ce niste prepricani, ali je bilo namescanje uspesno, ali pa se ne spomnite, ce je python ze namesecn, lahko preverite njegovo razlicico tako, da v terminal (na macOS ga lahko odpremo z: CMD + Space -> "Terminal" -> Enter) vpisemo 

```console
python --version #verzija pythona
python3 --version #verzija python3
```

Zelimo si tak izpis:
```console 
Python 3.12.2 #Stevilke se lahko razlikujejo
```

Prav tako lahko preverimo tudi verzijo git-a z naslednjim ukazom:

```console 
git --version
```

Nakar bi nam moral terminal izpisati:
```console 
git version 2.44.0
```

### Namescanje knjiznic
Pri delu bomo potrebovali tudi nekatera dodatna orodja. Vse lahko enostavno pridobite z ukazom
```console
pip3 install requests pandas numpy seaborn matplotlib
```

### Pridobivanja datotek z git-om
Vse doticne datoteke tega programa lahko enostavno namestite tako da pozenete naslednji ukaz:
```console 
git clone https://github.com/urbancluka/UVP-Projektna-naloga.git
```

### Struktura programa:
Najprej se moramo prepricati, da se trenutno nahajamo v pravilen direktoriju. Ko smo se prepricali oziroma smo se ustrezno premaknili, lahko zacnemo z delom, Za zacetek izvajanja programa moramo pognati le `main.py`, kar storimo tako da v terminal vpisemo 
``` console 
python3 main.py
```

V primeru da za ta ukaz nimamo dovoljenja, lahko vpisemo 
```console
sudo python3 main.py
```
a bomo morali za tem vpisati nase geslo.

Nato moramo le slediti navodilom, ki se izpisujejo v terminalu. Podatki se shranjujejo v mape, a edina zares pomembna je `data.csv`, v kateri se nahajajo podatki, ki nas dejansko zanimajo. 

Zajem podatkov lahko traja nekaj casa. Sproti se izpisujejo tudi spletne strani, ki jih shranjuje, ko nam izpise, `Vase datoteke se nahajajo v datoteki 'data.csv'` je program zakljucil z delom. 


### Analiza
Analiza se nahaja v datoteki `analiza.ipynb`, ki jo lahko odpremo s programom za branje Jupyter Notebook-ov, ali pa si jo pogledamo kar na spletu na Github-u. Vsi grafi, rezultati in ugotovitve bodo predstavljene v tisti datoteki.



#### Spodnji seznam se ne tice uporabnika in je namenjen avtorju
## TODO:
 - [x] Create function to download .html file with correct parameters
 - [x] Decide what website to scrap
 - [x] Write regex function to retrieve data from raw html file
 - [x] Save data to single .csv file
 - [x] Make website inputs a prompt for the user to enter ("enter starting page, enter last page...")
 - [x] Build loop into download_main function
 - [x] Fix power scrapping
 - [ ] Add test to see if file is empty in save_csv.py -> save_list_to_csv
 - [ ] Add test to see if list_of_data is same length as csv head
 - [x] Fix missing data point in acceleration