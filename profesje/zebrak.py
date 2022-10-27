import random

klasa = "Mieszczanie"

nazwa_profesji = {
    0 : "Biedak",
    1 : "Biedak",
    2 : "Żebrak",
    3 : "Mistrz Żebraków",
    4 : "Król Żebraków"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Brąz",
    4 : "Srebro"
}

rozwiniecia_cech = {
    "Ogd": 0,
    "Wt": 0,
    "Zw" : 0,
    "SW" : -1,
    "WW" : -2,
    "I" : -3,
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
waga = ["Zw", "Ogd", "Int", "Wt", "WW", "SW", "I", "S", "US", "Zr",]
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

umiejkip = ["Atletyka", "Charyzma", "Intuicja", "Mocna Głowa", "Odporność", "Opanowanie", "Skradanie (Miasto)", "Unik"]

umiejkip0 = {}

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 1
    
umiejkip = ["Percepcja", "Plotkowanie", "Targowanie", "Występy(Aktorstwo)", "Występy (Dowolne)", "Zwinne Palce"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 0
    
umiejkip = ["Umiejętności: Dowodzenie", "Oswajanie", "Sekretne Znaki(Włóczykijów),Wiedza (Lokalna)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -1
    
umiejkip = ["Przekupstwo", "Zastraszanie"]
for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    
    umiejkip0[um] = -2


talenty = []

talenty0 = ["Naciągacz"]
talenty1 = ["Niezwykle Odporny", "Odporny na (Choroby)", "Wstrzemięźliwy"]
talenty2 = ["Etykieta (Przestępcy)", "Niegodny Uwagi", "Przestępca", "Ulicznik"]
talenty3 = ["Cios Poniżej Pasa", "Gadanina", "Twardziel", "Zejście z Linii"]
talenty4 = ["Charyzmatyczny", "Gładkie Słówka", "Nieustraszony(Strażnicy)", "Szycha"]

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



wyp1 = ["podłej jakości koc", "kubek"]
wyp2 = ["kule do chodzenia", "miska"]
wyp3 = ["kryjówka", "towarzyszący Biedak", "zestaw do charakteryzacji"]
wyp4 = ["kryjówka", "duża grupa towarzyszących Żebraków"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(cechyp, umiejkip0, talenty, wyp, rozwiniecia_cech)