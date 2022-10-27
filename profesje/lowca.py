import random

klasa = "Pospólstwo"

rozwiniecia_cech = {
    "S": 0,
    "Wt": 0,
    "Zr" : 0,
    "US" : -1,
    "I" : -2,
    "Int" : -3,
}

waga = ["US", "S", "Wt", "I", "WW", "Zw", "Int", "SW", "Zr", "Ogd", ]

nazwa_profesji = {
    0 : "Traper",
    1 : "Traper",
    2 : "Łowca",
    3 : "Tropiciel",
    4 : "Wielki Łowczy"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Brąz",
    3 : "Srebro",
    4 : "Srebro"
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

umiejkip = ["Broń Zasięgowa (Proca)", "Odporność", "Oswajanie", "Percepcja", "Sztuka Przetrwania", "Wiedza (Zwierzęta)", "Wspinaczka", "Zastawianie Pułapek"]

umiejkip0 = {}

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 1
    
umiejkip = ["Broń Biała (Podstawowa)", "Broń Zasięgowa (Łuk)", "Intuicja", "Opanowanie", "Sekretne Znaki (Łowców)", "Skradanie (Wieś)"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 0
    
umiejkip = ["Jeździectwo (Konie)", "Nawigacja", "Pływanie,Tropienie"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -1
    
umiejkip = ["Opieka nad Zwierzętami", "Tresura (Dowolna)"]
for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -2


talenty = []

talenty0 = ["Traper"]
talenty1 = ["Doświadczony Wędrowiec (Dowolny Teren)", "Twardziel", "Włóczykij"]
talenty2 = ["Błyskawiczny Strzał", "Celny Strzał", "Oko Łowcy", "Strzelec Wyborowy"]
talenty3 = ["Nieustraszony (Zwierzęta)", "Prosto Między Oczy", "Strzał w Dziesiątkę", "Wyczulony Zmysł (Dowolny)"]
talenty4 = ["Krzepki", "Nieustraszony (Potwory)", "Snajper", "Strzał Przebijający"]

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



wyp1 = ["broń ręczna", "mocne buty i płaszcz", "wybór sideł na zwierzęta", "proca z 10 kamiennymi pociskami"]
wyp2 = ["łuk z 10 strzałami"]
wyp3 = ["namiot", "plecak", "zwijane posłanie"]
wyp4 = ["koń wierzchowy z rzędem", "psiarnia z psami łowieckimi"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]


profes = OdProfesji(cechyp, umiejkip0, talenty, wyp, rozwiniecia_cech)