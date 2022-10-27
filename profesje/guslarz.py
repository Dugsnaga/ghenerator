import random

klasa = "Pospólstwo"

rozwiniecia_cech = {
    "I": 0,
    "Wt": 0,
    "Zr" : 0,
    "Int" : -1,
    "Ogd" : -2,
    "SW" : -3,
}

waga = ["Int", "SW", "Wt", "Ogd", "I",  "Zw",  "Zr",  "WW", "S","US"]

nazwa_profesji = {
    0 : "Uczeń Guślarza",
    1 : "Uczeń Guślarza",
    2 : "Guślarz",
    3 : "Starszy Guślarzy",
    4 : "Wiedzący "
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Brąz",
    4 : "Brąz"
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

umiejkip = ["Intuicja", "Język (Magiczny)", "Odporność", "Percepcja", "Splatanie Magii", "Sztuka Przetrwania", "Wiedza (Ludowa)", "Wiedza (Zioła)"]

umiejkip0 = {}

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 1
    
umiejkip = ["Opanowanie", "Plotkowanie", "Leczenie", "Wiedza (Lokalna)", "Rzemiosło (Amulety)", "Rzemiosło (Zielarz)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 0
    
umiejkip = ["Targowanie", "Wiedza (Duchy)", "Wiedza (Genealogia)", "Wiedza (Magia)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -1
    
umiejkip = ["Umiejętności: Modlitwa", "Zastraszanie"]
for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -2


talenty = []

talenty0 = ["Magia Prosta"]
talenty1 = ["Doświadczony Wędrowiec (Lasy)", "Ruchliwe Dłonie", "Włóczykij"]
talenty2 = ["Magia Tajemna (Guślarstwo)", "Posłuch u Zwierząt", "Szósty Zmysł", "Zmysł Magii"]
talenty3 = ["Czysta Dusza", "Odporny na (Choroby)", "Wykrywanie Magii", "Wytwórca (Zielarz)"]
talenty4 = ["Mistrz Rzemiosła (Zielarz)", "Odporność Psychiczna", "Widzenie w Ciemności", "Wyczulony Zmysł (Dowolny)"]

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



wyp1 = ["kostur", "plecak", "1k10 amuletów na szczęście"]
wyp2 = ["kataplazm leczniczy", "narzędzia pracy (Zielarza)", "zestaw do leczenia zatruć"]
wyp3 = ["odosobniona chata", "Uczeń"]
wyp4 = ["ceremonialny płaszcz z wiankiem", "zbiór zwierzęcych czaszek"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]


profes = OdProfesji(cechyp, umiejkip0, talenty, wyp, rozwiniecia_cech)
