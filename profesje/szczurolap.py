import random

klasa = "Mieszczanie"

nazwa_profesji = {
    0 : "Uczeń Szczurołapa",
    1 : "Uczeń Szczurołapa",
    2 : "Szczurołap",
    3 : "Strażnik Kanałów",
    4 : "Tępiciel"
}
status = {
    0 : "Brąz",
    1 : "Brąz",
    2 : "Srebro",
    3 : "Srebro",
    4 : "Srebro"
}

rozwiniecia_cech = {
    "WW": 0,
    "US": 0,
    "SW" : 0,
    "Wt" : -1,
    "I" : -2,
    "S" : -3,
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
waga = ["WW", "US", "Wt","S", "I", "SW", "Zw", "Ogd", "Int", "Zr",]
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

umiejkip = ["Atletyka", "Tresura (Psy)", "Oswajanie", "Mocna Głowa", "Odporność", "Broń Biała (Podstawowa)", "Broń Zasięgowa(Proca)", "Skradanie (Miasto albo Podziemia)"]

umiejkip0 = {}

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 1
    
umiejkip = ["Opieka nad Zwierzętami", "Percepcja", "Plotkowanie", "Targowanie", "Wiedza (Trucizny)", "Zastawianie Pułapek"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = 0
    
umiejkip = ["Broń Zasięgowa (Kusza Pistoletowa)", "Opanowanie", "Unik", "Wspinaczka"]

for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -1
    
umiejkip = ["Dowodzenie", "Tropienie"]
for um in umiejkip:
    if um in umiejkip0:
        um = um + " "
    umiejkip0[um] = -2


talenty = []

talenty0 = ["Widzenie w Ciemności"]
talenty1 = ["Odporny na (Choroby)", "Ogłuszenie", "Silny Cios"]
talenty2 = ["Etykieta (Członkowie Cechu)", "Nieustraszony (Szczury)", "Niezwykle odporny", "Walka w Ciasnocie"]
talenty3 = ["Silne Nogi", "Szczur Kanałowy", "Twardziel", "Waleczne Serce"]
talenty4 = ["Groźny", "Krzepki", "Odporność Psychiczna", "Nieustraszony (Skaveny)"]

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



wyp1 = ["mały, ale zajadły pies", "proca z amunicją", "worek"]
wyp2 = ["sidła na zwierzęta", "drąg na martwe szczury"]
wyp3 = ["lampa Davricha", "broń ręczna", "skórzana kurta"]
wyp4 = ["Asystent", "duży i zajadły pies", "worek zatrutej przynęty (10 Porcji Sercoboju)"]
wyp = [wyp0, wyp1, wyp2, wyp3, wyp4]



profes = OdProfesji(cechyp, umiejkip0, talenty, wyp, rozwiniecia_cech)