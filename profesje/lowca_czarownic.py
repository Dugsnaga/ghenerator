import random

klasa = "Wędrowcy"

rozwiniecia_cech = {
    "WW": 0,
    "Wt": 0,
    "SW" : 0,
    "US" : -1,
    "Ogd" : -2,
    "Int" : -3,
}

waga = ["WW", "SW", "Wt", "US", "Ogd", "Int", "Zw",  "I",  "S", "Zr" ]

nazwa_profesji = {
    0 : "Oprawca",
    1 : "Oprawca",
    2 : "Łowca Czarownic",
    3 : "Inkwizytor",
    4 : "Generał Łowców Czarownic"
}
status = {
    0 : "Srebro",
    1 : "Srebro",
    2 : "Srebro",
    3 : "Srebro",
    4 : "Złoto"
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

umiejkip = ["Broń Biała (Bijatyka)", "Charyzma", "Intuicja", "Leczenie", "Mocna Głowa", "Percepcja", "Wiedza (Tortury)", "Zastraszanie"]

umiejkip0 = {}

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 1
    
umiejkip = ["Broń Biała (Dowolna)", "Broń Zasięgowa (Dowolna)", "Jeździectwo (Konie)", "Opanowanie", "Plotkowanie", "Wiedza (Czarownice)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 0
    
umiejkip = ["Dowodzenie", "Odporność", "Wiedza (Lokalna)", "Wiedza (Prawo)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -1
    
umiejkip = ["Wiedza (Chaos)", "Wiedza (Polityka)"]
for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -2


talenty = []

talenty0 = ["Groźny"]
talenty1 = ["Czytanie/Pisanie", "Nieugięty", "Zimna Krew"]
talenty2 = ["Cień", "Dwie Bronie", "Obieżyświat", "Strzelec Wyborowy"]
talenty3 = ["Odporność Psychiczna", "Nieustępliwy", "Nieustraszony (Czarownice)", "Nos do Kłopotów"]
talenty4 = ["Czysta Dusza", "Straszny", "Wykrywanie Magii", "Żelazna Wola"]

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



wyp1 = ["broń ręczna", "narzędzia tortur"]
wyp2 = ["kapelusz (kornet)", "koń wierzchowy z rzędem", "kusza pistoletowa albo pistolet", "lina", "posrebrzany miecz", "skórzana kurta"]
wyp3 = ["podwładni Oprawcy", "ubranie dobrej jakości"]
wyp4 = ["podwładni Łowcy Czarownic", "strój dworski najlepszej jakości"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]


profes = OdProfesji(cechyp, umiejkip0, talenty, wyp, rozwiniecia_cech)
