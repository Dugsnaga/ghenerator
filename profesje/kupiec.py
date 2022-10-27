import random

klasa = "Mieszczanie"

nazwa_profesji = {
    0 : "Handlarz",
    1 : "Handlarz",
    2 : "Kupiec",
    3 : "Mistrz Kupiectwa",
    4 : "Patrycjusz"
}
status = {
    0 : "Srebro",
    1 : "Srebro",
    2 : "Srebro",
    3 : "Złoto",
    4 : "Złoto"
}

rozwiniecia_cech = {
    "SW": 0,
    "Ogd": 0,
    "Zw" : 0,
    "Int" : -1,
    "I" : -2,
    "WW" : -3,
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
waga = ["Ogd", "Int", "SW", "Zw", "WW", "Wt", "I", "S", "US", "Zr", ]
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

umiejkip = ["Charyzma", "Hazard", "Mocna Głowa", "Opieka nad Zwierzętami", "Plotkowanie", "Powożenie", "Przekupstwo", "Targowanie"]

umiejkip0 = {}

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 1
    
umiejkip = ["Intuicja", "Język (Dowolny)", "Język (Gildii)", "Percepcja", "Wiedza (Lokalna)", "Wycena"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 0
    
umiejkip = ["Język (Klasyczny)", "Opanowanie", "Nawigacja", "Sekretne Znaki (Gildii)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -1
    
umiejkip = ["Wiedza (Dowolna)", "Zastraszanie"]
for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -2


talenty = []

talenty0 = ["Charyzmatyczny"]
talenty1 = ["Czytanie/Pisanie", "Gadanina", "Żyłka Handlowa"]
talenty2 = ["Błyskotliwość", "Defraudant", "Etykieta (Członkowie Gildii)", "Łapówkarz"]
talenty3 = ["Czujny", "Gładkie Słówka", "Etykieta (Dowolna Grupa)", "Numizmatyka"]
talenty4 = ["Intrygant", "Majętny", "Szczęście", "Żelazna Wola"]

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



wyp1 = ["liczydło", "płócienna plandeka", "wóz z mułem", "3k10 srebrnych szylingów"]
wyp2 = ["licencja Gildii", "łódź rzeczna albo 2 wozy", "20ZK"]
wyp3 = ["kamienica ze Służbą", "magazyn", "100 ZK"]
wyp4 = ["2 łodzie rzeczne lub 4 wozy", "dobre ubranie", "duża posiadłość w mieście", "2 magazyny", "1000 ZK"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(cechyp, umiejkip0, talenty, wyp, rozwiniecia_cech)