import random

klasa = "Łotrzy"

nazwa_profesji = {
    0 : "Porywacz Zwłok",
    1 : "Porywacz Zwłok",
    2 : "Hiena Cmentarna",
    3 : "Rabuś Grobowców",
    4 : "Łowca Skarbów"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Srebro",
    4 : "Srebro"
}

rozwiniecia_cech = {
    "S": 0,
    "I": 0,
    "SW" : 0,
    "WW" : -1,
    "Zr" : -2,
    "Int" : -3,
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
waga = ["WW", "S", "I", "SW", "Int", "Zr", "Zw", "Wt",  "Ogd", "US"]
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

umiejkip = ["Intuicja", "Odporność", "Opanowanie", "Percepcja", "Plotkowanie", "Skradanie (Dowolne)", "Unik", "Wspinaczka"]

umiejkip0 = {}

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 1
    
umiejkip = ["Broń Biała (Podstawowa)", "Powożenie", "Przekupstwo", "Targowanie", "Wiedza (Medycyna)", "Wycena"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 0
    
umiejkip = ["Badania Naukowe", "Otwieranie Zamków", "Wiedza (Historia)", "Zastawianie Pułapek"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -1
    
umiejkip = ["Umiejętności: Nawigacja", "Rzemiosło (Inżynier)"]
for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -2


talenty = []

talenty0 = ["Przestępca"]
talenty1 = ["Chodu!",  "Mocne Plecy", "Ulicznik"]
talenty2 = ["Bardzo Silny", "Odporny na (Choroby)", "Widzenie w Ciemności", "Wtargnięcie z Włamaniem"]
talenty3 = ["Czytanie/Pisanie", "Silny Cios", "Szczur Kanałowy", "Wytrwały"]
talenty4 = ["Nieustraszony (Nieumarli)", "Odporność Psychiczna", "Szósty Zmysł", "Traper"]

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



wyp1 = ["łom", "plandeka", "płaszcz z kapturem", "taczka"]
wyp2 = ["broń ręczna", "lampa sztormowa z oliwą", "plecak", "szpadel"]
wyp3 = ["broń ręczna (kilof)", "lina", "narzędzia pracy (Złodziei)", "skórzana kurta", "wóz z koniem"]
wyp4 = ["mapy", "namiot", "narzędzia pracy (Inżyniera)", "zestaw do pisania", "zwijane posłanie"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(cechyp, umiejkip0, talenty, wyp, rozwiniecia_cech)