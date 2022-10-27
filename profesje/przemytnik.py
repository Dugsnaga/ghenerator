import random

klasa = "Wodniacy"

nazwa_profesji = {
    0 : "Szmugler Rzeczny",
    1 : "Szmugler Rzeczny",
    2 : "Przemytnik",
    3 : "Doświadczony Przemytnik",
    4 : "Król Przemytników"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Brąz",
    4 : "Srebro"
}

rozwiniecia_cech = {
    "Zw": 0,
    "Zr": 0,
    "SW" : 0,
    "I" : -1,
    "Int" : -2,
    "Ogd" : -3,
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
        

#losujemy rzutyi ustawiamy je według porządku co jest ważne  fff
waga = ["Zw", "SW", "WW", "I", "Zr", "Ogd", "Int",  "S",  "Wt",  "US", ]
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

umiejkip = ["Atletyka", "Mocna Głowa", "Opanowanie", "Pływanie", "Przekupstwo", "Skradanie (Wieś albo Miasto)", "Wioślarstwo", "Żeglarstwo"]

umiejkip0 = {}

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 1
    
umiejkip = ["Broń Biała (Podstawowa)", "Percepcja", "Plotkowanie", "Sekretne Znaki (Przemytników)", "Targowanie", "Wiedza (Lokalna)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 0
    
umiejkip = ["Błyskotliwość", "Doświadczony Wędrowiec (Wybrzeża)", "Szycha", "Urodzony Żeglarz"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -1
    
umiejkip = ["Dowodzenie", "Język (Dowolny)"]
for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -2


talenty = []

talenty0 = ["Doświadczony Wędrowiec (Bagna)"]
talenty1 = ["Mocne Plecy", "Przestępca", "Rybak"]
talenty2 = ["Bardzo Silny", "Etykieta (Przestępcy)", "Wodniak", "Żyłka Handlowa"]
talenty3 = ["Łapówkarz", "Nieustraszony (Strażnicy Rzeczni)", "Pilot", "Świetny Pływak"]
talenty4 = ["Błyskotliwość", "Doświadczony Wędrowiec (Wybrzeża)", "Szycha", "Urodzony Żeglarz"]

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



wyp1 = ["chusta albo maska", "duży worek", "lampa sztormowa z oliwą", "pudełko na hubkę i krzesiwo"]
wyp2 = ["broń ręczna", "skórzana kurta", "łódź wiosłowa", "2 beczki"]
wyp3 = ["Szmugler Rzeczny", "szybka łódź rzeczna"]
wyp4 = ["mała flota łodzi rzecznych", "zestaw do charakteryzacji"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(cechyp, umiejkip0, talenty, wyp, rozwiniecia_cech)