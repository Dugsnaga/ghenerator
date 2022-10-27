

import random

klasa = "Uczeni"

nazwa_profesji = {
    0 : "Nowicjusz",
    1 : "Nowicjusz",
    2 : "Mnich",
    3 : "Przeor",
    4 : "Opat"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Srebro",
    4 : "Srebro"
}

rozwiniecia_cech = {
    "Int": 0,
    "Ogd": 0,
    "Zr" : 0,
    "SW" : -1,
    "I" : -2,
    "Wt" : -3,
}

class OdProfesji():
    def __init__(self, cechy, umiejki, talenty, wyposazenie, rozwiniecia_cech):
        self.cechy = cechy
        self.umiejki = umiejki
        self.talenty = talenty
        self.wyposazenie = wyposazenie
        self.rozwiniecia_cech = rozwiniecia_cech
        self.status = status
        self.nazwa_profesji = nazwa_profesji
    def __str__(self):
        pass
        

#losujemy rzutyi ustawiamy je według porządku jak co jest ważne  fff
waga = ["Int", "Ogd", "SW", "Zr", "I", "Zw", "Wt", "S", "WW", "US", ]
rzuty = []
a = 10
while a>0:
     b = random.randint(2,20) 
     rzuty.append(b)
     a = a -1
    
    
cechyp = {}
rzuty.sort()
rzuty.reverse()
#print (rzuty)
a = 0
while a<10:
    cechyp[waga[a]]=rzuty[a]
    a = a + 1
#print(cechyp)

#budujemy słownik z umiejętności. Ich wartości będą wynosić od -2 na najwyższym tierze, do 0 na najniższym. Następnie 
# dodamy tier jaką mam mieć postać (od 0, do 4)

umiejkip = ["Leczenie", "Modlitwa", "Odporność", "Opanowanie", "Plotkowanie", "Sztuka (Kaligrafia)", "Wiedza (Teologia)", "Występy (Gawędziarstwo)"]

umiejkip0 = {}

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 1
    
umiejkip = ["Badania Naukowe", "Broń Biała (Dowolna)", "Przekonywanie", "Rzemiosło (Browarnik)", "Rzemiosło(Winiarz)", "Rzemiosło (Zielarz)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 0
    
umiejkip = ["Dowodzenie", "Percepcja", "Wiedza (Lokalna)", "Wiedza (Polityka)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -1
    
umiejkip = ["Język (Dowolny)", "Wiedza (Dowolna)"]
for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -2


talenty = []

talenty0 = ["Błogosławieństwo (Dowolne Bóstwo)"]
talenty1 = ["Czytanie/Pisanie", "Naciągacz", "Wstrzemięźliwy"]
talenty2 = ["Etykieta (Kultyści)", "Inwokacja (Dowolne Bóstwo)", "Pierwsza Pomoc", "Święte Wizje"]
talenty3 = ["Odporny na (Dowolne Zagrożenie)", "Krzepki", "Znawca (Teologia)", "Waleczne Serce"]
talenty4 = ["Czysta Dusza", "Odporność Psychiczna", "Władcza Postura", "Żelazna Wola"]

talenty = {}

for idx, war in enumerate(talenty0):
    talenty[war] = 1
for idx, war in enumerate(talenty1):
    talenty[war] = 0
for idx, war in enumerate(talenty2):
    talenty[war] = -1
for idx, war in enumerate(talenty3):
    talenty[war] = -2
for idx, war in enumerate(talenty4):
    talenty[war] = -3

#print(talenty)

################ROBIMY ZBIÓR CAŁEGO MOŻLIWEGO EKWIPUNKU

if klasa == "Uczeni":
    wyp0 = ["sakwa", "sztylet", "torba na ramię z zestawem do pisania oraz 1k10 kart pergaminu", "ubranie"]
if klasa == "Mieszczanie":
    wyp0 = ["kapelusz", "płaszcz", "sakwa", "sztylet", "torba na ramię z posiłkiem","ubranie"]
if klasa == "Dworzanie":
    wyp0 = ["sakiewka z niezbędnikiem (grzebieniem patyczkiem do czyszczenia uszu i pęsetą)", "wyśmienite ubranie", "sztylet"]
if klasa == "Pospólstwo":
    wyp0 = ["płaszcz", "sakwa", "sztylet", "torba na ramię z racjami żywnościowymi(1 dzień)", "ubranie"]
if klasa == "Wędrowcy":
    wyp0 = ["plecak z hubką i krzesiwem", "kocem i racjami żywnościowymi(1 dzień)", "płaszcz", "sakwa", "sztylet", "ubranie"]
if klasa == "Wodniacy":
    wyp0 = ["płaszcz", "sakwa", "sztylet", "torba na ramię z butelką alkoholu", "ubranie"]
if klasa == "Łotrzy":
    wyp0 = ["kaptur lub maska", "sakwa", "sztylet", "ubranie", "torba na ramię z 2 świecami", "1k10 zapałek"]
if klasa == "Wojownicy":
    wyp0 = ["broń biała", "sakwa", "sztylet", "ubranie"]



wyp1 = ["bandaże", "mikstura lecznicza"]
wyp2 = ["księga (Medycyna)", "licencja Cechu", "narzędzia pracy (Medycyna)"]
wyp3 = ["Uczeń", "warsztat (Medyczny)"]
wyp4 = ["nominacja", "strój dworski"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(cechyp, umiejkip0, talenty, wyp, rozwiniecia_cech)