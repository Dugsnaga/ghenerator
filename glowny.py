import random
#definiuje klasę
class Postac():
    def __init__(self, imie = None, prof = None, rasa = None, plec = "Mężczyzna", tier = 0):
        self.imie = imie
        self.prof = None
        self.rasa = None
        self.plec = plec
        self.tier = tier
        self.cechy = {'WW': 0, 'US': 0, 'S': 0, 'Wt': 0, 'I': 0, 'Zw': 0, 'Zr': 0, 'Int': 0, 'SW': 0, 'Ogd': 0}
        self.umiejki = None
        self.talenty = None
        self.wzrost = None
        self.wlosy = None
        self.szybkosc = None
        self.wyposazenie = []
        self.punkty_przeznaczenia = 0
        self.punkty_bohatera = 0
        self.majatek = None
        self.oczy = None
        self.status = None
        self.zywotnosc = None
        self.nazwa_profesji = None

#Tworzę obiekt klasy
inst = Postac()


##############MOŻLIWOŚĆ WPISANIA RASY, BĄDŹ JEJ LOSOWANIE
#tabela ras
rasy= {
    1 : "Leśny elf",
    2 : "Wysoki elf",
    3 : "Krasnolud",
    4 : "Niziołek",
    5 : "Człowiek"
}

#formatowanie wyświetlenia tablicy ras
rasy_str = ""
a = 1
for key, value in rasy.items():
    b = ""
    c = len(value)
    d = 30 - len(value) - len(str(key))

    while d > 0:
        b = b + " "
        d = d - 1

    if a % 4 != 0:
        rasy_str = rasy_str + str(key)+ " - " + value + b
        #print(rasy_str)
        
    if a % 4 == 0:
        rasy_str = rasy_str + str(key)+  " - " + value + "\n"
        #print(rasy_str)
    
    a = a + 1

print(rasy_str)

# input rasy przez uzytkownika
input_rasa = input(f"Wybierz numer 1-5 aby wybrać rasę:(1-5) ")
ranga = ["1", "2", "3", "4", "5"]

if input_rasa in ranga:
    in_r = int(input_rasa)
    print(f"Twoja rasa to {rasy[in_r]}")
    inst.rasa = rasy[in_r]

if inst.rasa==None:
    print("Twój wybór jest inwalidą, sam sobie wylosuję")
    los_ras = random.randint(1, 100)
    lesny = [100]
    wysoki =[99]
    kras=[98, 97, 96, 95]
    hobbit = [94, 93, 92, 91] 
    if los_ras in lesny:
        inst.rasa = "Leśny elf"
    if los_ras in wysoki:
        inst.rasa = "Wysoki elf"            
    if los_ras in kras:
        inst.rasa = "Krasnolud"           
    if los_ras in hobbit:
        inst.rasa = "Niziołek"           
    if los_ras<91:
        inst.rasa = "Człowiek"
print(f"Twoja postać to {inst.rasa}")

#tabele do losowania profesji różnych ras
if inst.rasa == "Leśny elf":
    tab_prof =  {1 : "Czarodziej",
2 : "Czarodziej",
3 : "Czarodziej",
4 : "Czarodziej",
5 : "Uczony",
6 : "Rzemieślnik",
7 : "Rzemieślnik",
8 : "Rzemieślnik",
9 : "Rzemieślnik",
10 : "Rzemieślnik",
11 : "Artysta",
12 : "Artysta",
13 : "Artysta",
14 : "Artysta",
15 : "Doradca",
16 : "Doradca",
17 : "Doradca",
18 : "Doradca",
19 : "Poseł",
20 : "Poseł",
21 : "Poseł",
22 : "Poseł",
23 : "Poseł",
24 : "Poseł",
25 : "Poseł",
26 : "Szlachcic",
27 : "Szlachcic",
28 : "Szlachcic",
29 : "Szlachcic",
30 : "Szlachcic",
31 : "Szlachcic",
32 : "Szpieg",
33 : "Szpieg",
34 : "Szpieg",
35 : "Szpieg",
36 : "Łowca",
37 : "Łowca",
38 : "Łowca",
39 : "Łowca",
40 : "Łowca",
41 : "Łowca",
42 : "Łowca",
43 : "Łowca",
44 : "Łowca",
45 : "Łowca",
46 : "Mistyk",
47 : "Mistyk",
48 : "Mistyk",
49 : "Mistyk",
50 : "Mistyk",
51 : "Zielarz",
52 : "Zielarz",
53 : "Zielarz",
54 : "Zielarz",
55 : "Zielarz",
56 : "Zielarz",
57 : "Zielarz",
58 : "Zwiadowca",
59 : "Zwiadowca",
60 : "Zwiadowca",
61 : "Zwiadowca",
62 : "Zwiadowca",
63 : "Zwiadowca",
64 : "Zwiadowca",
65 : "Zwiadowca",
66 : "Zwiadowca",
67 : "Zwiadowca",
68 : "Zwiadowca",
69 : "Kuglarz",
70 : "Kuglarz",
71 : "Kuglarz",
72 : "Kuglarz",
73 : "Kuglarz",
74 : "Łowca Nagród",
75 : "Łowca Nagród",
76 : "Posłaniec",
77 : "Posłaniec",
78 : "Posłaniec",
79 : "Pirat Rzeczny",
80 : "Banita",
81 : "Banita",
82 : "Banita",
83 : "Banita",
84 : "Banita",
85 : "Banita",
86 : "Gladiator",
87 : "Gladiator",
88 : "Kawalerzysta",
89 : "Kawalerzysta",
90 : "Kawalerzysta",
91 : "Kawalerzysta",
92 : "Kawalerzysta",
93 : "Ochroniarz",
94 : "Ochroniarz",
95 : "Rycerz",
96 : "Rycerz",
97 : "Żołnierz",
98 : "Żołnierz",
99 : "Żołnierz",
100 : "Żołnierz",

   
}
if inst.rasa == "Wysoki elf":
    tab_prof=  {1: 'Aptekarz', 2: 'Aptekarz', 3: 'Czarodziej', 4: 'Czarodziej', 5: 'Czarodziej', 6: 'Czarodziej', 7: 'Medyk', 8: 'Medyk', 9: 'Prawnik', 10: 'Prawnik', 11: 'Prawnik', 12: 'Prawnik', 13: 'Uczony', 14: 'Uczony', 15: 'Uczony', 16: 'Uczony', 17: 'Kupiec', 18: 'Kupiec', 19: 'Kupiec', 20: 'Kupiec', 21: 'Kupiec', 22: 'Mieszczanin', 23: 'Mieszczanin', 24: 'Rzemieślnik', 25: 'Rzemieślnik', 26: 'Rzemieślnik', 27: 'Strażnik', 28: 'Śledczy', 29: 'Śledczy', 30: 'Artysta', 31: 'Doradca', 32: 'Doradca', 33: 'Namiestnik', 34: 'Namiestnik', 35: 'Poseł', 36: 'Poseł', 37: 'Poseł', 38: 'Szlachcic', 39: 'Szlachcic', 40: 'Szlachcic', 41: 'Szpieg', 42: 'Szpieg', 43: 'Szpieg', 44: 'Zwadźca', 45: 'Zwadźca', 46: 'Łowca', 47: 'Łowca', 48: 'Łowca', 49: 'Zielarz', 50: 'Zielarz', 51: 'Zwiadowca', 52: 'Zwiadowca', 53: 'Zwiadowca', 54: 'Zwiadowca', 55: 'Zwiadowca', 56: 'Zwiadowca', 57: 'Kuglarz', 58: 'Kuglarz', 59: 'Kuglarz', 60: 'Łowca Nagród', 61: 'Łowca Nagród', 62: 'Łowca Nagród', 63: 'Posłaniec', 64: 'Przemytnik', 65: 'Przewoźnik', 66: 'Żeglarz', 67: 'Żeglarz', 68: 'Żeglarz', 69: 'Żeglarz', 70: 'Żeglarz', 71: 'Żeglarz', 72: 'Żeglarz', 73: 'Żeglarz', 74: 'Żeglarz', 75: 'Żeglarz', 76: 'Żeglarz', 77: 'Żeglarz', 78: 'Żeglarz', 79: 'Żeglarz', 80: 'Żeglarz', 81: 'Banita', 82: 'Banita', 83: 'Banita', 84: 'Rajfur', 85: 'Rajfur', 86: 'Szarlatan', 87: 'Szarlatan', 88: 'Szarlatan', 89: 'Gladiator', 90: 'Gladiator', 91: 'Kawalerzysta', 92: 'Kawalerzysta', 93: 'Kawalerzysta', 94: 'Kawalerzysta', 95: 'Ochroniarz', 96: 'Ochroniarz', 97: 'Oprych', 98: 'Rycerz', 99: 'Żołnierz', 100: 'Żołnierz'}
if inst.rasa == "Krasnolud":
    tab_prof= {
    1 : "Aptekarz",
2 : "Inżynier",
3 : "Inżynier",
4 : "Inżynier",
5 : "Medyczka",
6 : "Prawnik",
7 : "Prawnik",
8 : "Uczony",
9 : "Uczony",
10 : "Agitator",
11 : "Agitator",
12 : "Kupiec",
13 : "Kupiec",
14 : "Kupiec",
15 : "Kupiec",
16 : "Mieszczanin",
17 : "Mieszczanin",
18 : "Mieszczanin",
19 : "Mieszczanin",
20 : "Mieszczanin",
21 : "Mieszczanin",
22 : "Rzemieślnik",
23 : "Rzemieślnik",
24 : "Rzemieślnik",
25 : "Rzemieślnik",
26 : "Rzemieślnik",
27 : "Rzemieślnik",
28 : "Strażnik",
29 : "Strażnik",
30 : "Strażnik",
31 : "Szczurołap",
32 : "Śledczy",
33 : "Śledczy",
34 : "Żebrak",
35 : "Artysta",
36 : "Doradca",
37 : "Doradca",
38 : "Namiestnik",
39 : "Namiestnik",
40 : "Poseł",
41 : "Poseł",
42 : "Służący",
43 : "Szlachcic",
44 : "Szpieg",
45 : "Zwadźca",
46 : "Chłop",
47 : "Górnik",
48 : "Górnik",
49 : "Górnik",
50 : "Górnik",
51 : "Górnik",
52 : "Łowca",
53 : "Łowca",
54 : "Zarządca",
55 : "Zarządca",
56 : "Zwiadowca",
57 : "Domokrążca",
58 : "Domokrążca",
59 : "Kuglarz",
60 : "Kuglarz",
61 : "Łowca Nagród",
62 : "Łowca Nagród",
63 : "Łowca Nagród",
64 : "Łowca Nagród",
65 : "Posłaniec",
66 : "Posłaniec",
67 : "Woźnica",
68 : "Doker",
69 : "Doker",
70 : "Flisak",
71 : "Flisak",
72 : "Pilot Rzeczny",
73 : "Pirat Rzeczny",
74 : "Przemytnik",
75 : "Przemytnik",
76 : "Przewoźnik",
77 : "Przewoźnik",
78 : "Żeglarz",
79 : "Banita",
80 : "Banita",
81 : "Banita",
82 : "Hiena Cmentarna",
83 : "Rekietier",
84 : "Zlodziej",
85 : "Gladiator",
86 : "Gladiator",
87 : "Gladiator",
88 : "Ochroniarz",
89 : "Ochroniarz",
90 : "Ochroniarz",
91 : "Oprych",
92 : "Oprych",
93 : "Oprych",
94 : "Zabójca",
95 : "Zabójca",
96 : "Zabójca",
97 : "Zabójca",
98 : "Żołnierz",
99 : "Żołnierz",
100 : "Żołnierz",
}
if inst.rasa == "Niziołek":
    tab_prof = {1: 'Aptekarz', 2: 'Inżynier', 3: 'Medyk', 4: 'Medyk', 5: 'Prawnik', 6: 'Prawnik', 7: 'Uczony', 8: 'Uczony', 9: 'Agitator', 10: 'Agitator', 11: 'Kupiec', 12: 'Kupiec', 13: 'Kupiec', 14: 'Kupiec', 15: 'Mieszczanin', 16: 'Mieszczanin', 17: 'Mieszczanin', 18: 'Rzemieślnik', 19: 'Rzemieślnik', 20: 'Rzemieślnik', 21: 'Rzemieślnik', 22: 'Rzemieślnik', 23: 'Strażnik', 24: 'Strażnik', 25: 'Szczurołap', 26: 'Szczurołap', 27: 'Szczurołap', 28: 'Śledczy', 29: 'Śledczy', 30: 'Żebrak', 31: 'Żebrak', 32: 'Żebrak', 33: 'Żebrak', 34: 'Artysta', 35: 'Poseł', 36: 'Doradca', 37: 'Namiestnik', 38: 'Namiestnik', 39: 'Poseł', 40: 'Służący', 41: 'Służący', 42: 'Służący', 43: 'Służący', 44: 'Służący', 45: 'Służący', 46: 'Szpieg', 47: 'Chłop', 48: 'Chłop', 49: 'Chłop', 50: 'Górnik', 51: 'Łowca', 52: 'Łowca', 53: 'Zarządca', 54: 'Zielarz', 55: 'Zielarz', 56: 'Zielarz', 57: 'Zwiadowca', 58: 'Domokrążca', 59: 'Domokrążca', 60: 'Kuglarz', 61: 'Kuglarz', 62: 'Kuglarz', 63: 'Łowca Nagród', 64: 'Posłaniec', 65: 'Posłaniec', 66: 'Strażnik Dróg', 67: 'Woźnica', 68: 'Woźnica', 69: 'Doker', 70: 'Doker', 71: 'Doker', 72: 'Flisak', 73: 'Flisak', 74: 'Flisak', 75: 'Pilot Rzeczny', 76: 'Przemytnik', 77: 'Przemytnik', 78: 'Przemytnik', 79: 'Przemytnik', 80: 'Przewoźnik', 81: 'Strażnik Rzeczny', 82: 'Żeglarz', 83: 'Banita', 84: 'Paser', 85: 'Hiena Cmentarna', 86: 'Rajfur', 87: 'Rajfur', 88: 'Rajfur', 89: 'Rekietier', 90: 'Szarlatan', 91: 'Złodziej', 92: 'Złodziej', 93: 'Złodziej', 94: 'Złodziej', 95: 'Gladiator', 96: 'Ochroniarz', 97: 'Ochroniarz', 98: 'Żołnierz', 99: 'Żołnierz', 100: 'Żołnierz'}
if inst.rasa == "Człowiek":
    tab_prof = { 1: 'Aptekarz', 2: 'Czarodziej', 3: 'Inżynier', 4: 'Kapłan', 5: 'Kapłan', 6: 'Kapłan', 7: 'Kapłan', 8: 'Kapłan', 9: 'Medyk', 10: 'Mnich', 11: 'Mnich', 12: 'Prawnik', 13: 'Uczony', 14: 'Uczony', 15: 'Agitator', 16: 'Kupiec', 17: 'Mieszczanin', 18: 'Mieszczanin', 19: 'Mieszczanin', 20: 'Rzemieślnik', 21: 'Rzemieślnik', 22: 'Strażnik', 23: 'Szczurołap', 24: 'Szczurołap', 25: 'Śledczy', 26: 'Żebrak', 27: 'Żebrak', 28: 'Artysta', 29: 'Doradca', 30: 'Namiestnik', 31: 'Poseł', 32: 'Służący', 33: 'Służący', 34: 'Służący', 35: 'Szlachcic', 36: 'Szpieg', 37: 'Zwadźca', 38: 'Chłop', 39: 'Chłop', 40: 'Chłop', 41: 'Chłop', 42: 'Chłop', 43: 'Górnik', 44: 'Guślarz', 45: 'Łowca', 46: 'Łowca', 47: 'Mistyk', 48: 'Zarządca', 49: 'Zielarz', 50: 'Zwiadowca', 51: 'Biczownik', 52: 'Biczownik', 53: 'Domokrążca', 54: 'Kuglarz', 55: 'Kuglarz', 56: 'Łowca Czarownic', 57: 'Łowca Nagród', 58: 'Posłaniec', 59: 'Strażnik Dróg', 60: 'Woźnica', 61: 'Doker', 62: 'Doker', 63: 'Flisak', 64: 'Flisak', 65: 'Flisak', 66: 'Pilot Rzeczny', 67: 'Pirat Rzeczny', 68: 'Przemytnik', 69: 'Przewoźnik', 70: 'Przewoźnik', 71: 'Strażnik Rzeczny', 72: 'Strażnik Rzeczny', 73: 'Żeglarz', 74: 'Żeglarz', 75: 'Banita', 76: 'Banita', 77: 'Banita', 78: 'Banita', 79: 'Czarownica', 80: 'Paser', 81: 'Hiena Cmentarna', 82: 'Rajfur', 83: 'Rajfur', 84: 'Rekietier', 85: 'Szarlatan', 86: 'Złodziej', 87: 'Złodziej', 88: 'Złodziej', 89: 'Gladiator', 90: 'Kapłan Bitewny', 91: 'Kawalerzysta', 92: 'Kawalerzysta', 93: 'Ochroniarz', 94: 'Ochroniarz', 95: 'Oprych', 96: 'Rycerz', 97: 'Żołnierz', 98: 'Żołnierz', 99: 'Żołnierz', 100: 'Żołnierz'}

###########MOŻLIWOŚĆ WPISANIA PROFESJI
#tablica wszystkich profesji
prof_d = {0: 'Agitator', 1: 'Aptekarz', 2: 'Artysta', 3: 'Banita', 4: 'Biczownik', 5: 'Chłop', 6: 'Czarodziej', 7: 'Czarownica', 8: 'Doker', 9: 'Domokrążca', 10: 'Doradca', 11: 'Flisak', 12: 'Gladiator', 13: 'Guślarz', 14: 'Górnik', 15: 'Hiena Cmentarna', 16: 'Inżynier', 17: 'Kapłan', 18: 'Kapłan Bitewny', 19: 'Kawalerzysta', 20: 'Kuglarz', 21: 'Kupiec', 22: 'Medyk', 23: 'Mieszczanin', 24: 'Mistyk', 25: 'Mnich', 26: 'Namiestnik', 27: 'Ochroniarz', 28: 'Oprych', 29: 'Paser', 30: 'Pilot Rzeczny', 31: 'Pirat Rzeczny', 32: 'Poseł', 33: 'Posłaniec', 34: 'Prawnik', 35: 'Przemytnik', 36: 'Przewoźnik', 37: 'Rajfur', 38: 'Rekietier', 39: 'Rycerz', 40: 'Rzemieślnik', 41: 'Strażnik', 42: 'Strażnik Dróg', 43: 'Strażnik Rzeczny', 44: 'Szarlatan', 45: 'Szczurołap', 46: 'Szlachcic', 47: 'Szpieg', 48: 'Służący', 49: 'Uczony', 50: 'Woźnica', 51: 'Zabójca', 52: 'Zarządca', 53: 'Zielarz', 54: 'Zwadźca', 55: 'Zwiadowca', 56: 'Złodziej', 57: 'Łowca', 58: 'Łowca Czarownic', 59: 'Łowca Nagród', 60: 'Śledczy', 61: 'Żebrak', 62: 'Żeglarz', 63: 'Żołnierz'}
prof_str = ""
a = 1
########format wyswietlania profesji
for key, value in prof_d.items():
    b = ""
    c = len(value)
    d = 20 - len(value) - len(str(key))

    while d > 0:
        b = b + " "
        d = d - 1

    if a % 5 != 0:
        prof_str = prof_str + str(key)+ " - " + value + b
        #print(prof_str)

    if a % 5 == 0:
        prof_str = prof_str + str(key)+ " - " + value + "\n"
        #print(prof_str)

    a = a + 1

print(prof_str)
#input uzytkownika do wyboru profesji. Jeśli zostanie podany zły, system sam wylosuje profesje
klucze = []
for key in prof_d:
       klucze.append(str(key))

input_prof = input("Podaj numer profesji, którą chciałbyś grać(0-63)\n ")

if input_prof in klucze:
    in_pr = int(input_prof)
    inst.prof = prof_d[in_pr]

####################LOSOWANIE PROFESJI NA PODSTAWIE RASY
if inst.prof==None:
    print("You choose poorly. Destiny chosen will be for You, young padavan\n")

spr_prof = []

for key, value in tab_prof.items():
    spr_prof.append(value)

if inst.prof == None:
    los = random.randint(1, 100)

    inst.prof = tab_prof[los]

if inst.prof in spr_prof:
    print(f"Twoja profesja to {inst.prof} \n ")

#Ostrzeżenie przy wybraniu profesji, która nie występuje dla tej rasy
if inst.prof not in spr_prof:
    print(f"Chcesz żeby to był {inst.rasa}, i do tego {inst.prof}? A little bit weird, ale kim jestem żeby Ci odmawiac tej przyjemności \n ")


#MAGMAR!!!!!
if inst.prof == "Kapłan Bitewny":
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!MAGMAR!!!!!!!!!!!!!!!!!!!!!!!!!!!")

####################MOŻLIWOŚĆ WPISANIA IMIENIA
input_imie = input("Wpisz imię postaci \n")
if input_imie != '':
    inst.imie = input_imie
    print(f"Imię Twojej postaci to {inst.imie}")
if input_imie == '':
    print("Imię zostanie wylosowane\n")


##########MOŻLIWOŚĆ WPISANIA TIER'U. DOMYŚLNIE 0
input_tier = input(f"Który poziom ma mieć postać? Domyślnie jest {inst.tier} (0-4) \n ")
zasiegxyz = ["0", "1", "2", "3", "4" ]
if input_tier in zasiegxyz:
    inst.tier = int(input_tier)
print(f"Poziom Twojej postaci to {inst.tier} \n")
#print("Pachu ma małego")
##################MOŻLIWOŚĆ WPISANIA WŁASNYCH RZUTÓW

inp_rzuty = input("Czy chcesz wpisać własne rzuty?(t/n) ")
zasieg_rzuty= ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
zbior_rzutow = {}

if inp_rzuty == "t":
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Walkę Wręcz\n ")
        if imp in zasieg_rzuty:
            zbior_rzutow["WW"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Umiejętności Strzeleckie\n ")
        if imp in zasieg_rzuty:
            zbior_rzutow["US"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Siłę\n ")
        if imp in zasieg_rzuty:
            zbior_rzutow["S"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Wytrzymałość\n ")
        if imp in zasieg_rzuty:
            zbior_rzutow["Wt"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Inicjatywę\n ")
        if imp in zasieg_rzuty:
            zbior_rzutow["I"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Zwinność \n")
        if imp in zasieg_rzuty:
            zbior_rzutow["Zw"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Zręczność\n ")
        if imp in zasieg_rzuty:
            zbior_rzutow["Zr"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Inteligencję\n ")
        if imp in zasieg_rzuty:
            zbior_rzutow["Int"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Siłę Woli \n")
        if imp in zasieg_rzuty:
            zbior_rzutow["SW"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    a = 1
    while a == 1:
        imp = input("Wpisz wartość rzutu na Ogładę \n")
        if imp in zasieg_rzuty:
            zbior_rzutow["Ogd"] = imp
            a = a -1    
        if imp not in zasieg_rzuty:
            print("Wpisana wartość nie jest cyfrą w przedziale 2-20. Spróbuj jeszcze raz")
    
    for cecha in zbior_rzutow:
        inst.cechy[cecha] = inst.cechy[cecha] + int(zbior_rzutow[cecha])
    
    print(f"Twoje rzuty to {zbior_rzutow} ") 

####################IMPORT ODPOWIEDNIEGO MODUŁU RASOWEGO
if inst.rasa == "Leśny elf":
    import rasy.lesny_elf
    rasowe = rasy.lesny_elf.rasowe
    #print(rasy.lesny_elf.__doc__)
if inst.rasa == "Wysoki elf":
    import rasy.wysoki_elf
    rasowe = rasy.wysoki_elf.rasowe
if inst.rasa == "Krasnolud":
    import rasy.khazad
    rasowe = rasy.khazad.rasowe 
if inst.rasa == "Niziołek":
    import rasy.hobbit
    rasowe = rasy.hobbit.rasowe
if inst.rasa == "Człowiek":
    import rasy.czlowiek
    rasowe = rasy.czlowiek.rasowe


podpis = "Created by DugSnaga"
###########################MOŻLIWOŚĆ WPISANIA PŁCI
input_plec = input("Wybierz płeć swojej postaci. Z powodu niskiego budżetu, generator wspiera tworzenie tylko dwóch płci. (m/k) ")
if input_plec == "k":
    inst.plec = "Kobieta"

if inst.plec == "Mężczyzna" and inst.prof == "Czarownica":
    print("Mężczyzna nie może być czarownicą z oczywistych przyczyn")
    inst.plec = "Kobieta"

print(f"Twoja postać to {inst.plec} \n")


###############################################DZIAŁ RASOWYYYYY#############################################################

################LOSOWANIE IMIENIA NA PODSTAWIE RASY
if inst.imie == None:
    if inst.plec == "Kobieta":
        inst.imie = rasowe.imie_z
    if inst.plec == "Mężczyzna":
        inst.imie = rasowe.imie_m
    print(f"Wylosowane imię brzmi {inst.imie}")


###############IMPORTUJEMY CECHY RASOWE DO NASZEJ INSTANCJI POSTACI
##cechy dodajemy, w razie gdyby już jakieś były wpisane
for cecha in rasowe.cechy:
    inst.cechy[cecha] = inst.cechy[cecha] + rasowe.cechy[cecha]


inst.umiejki = rasowe.umiejki
inst.talenty = rasowe.talenty
inst.wzrost = rasowe.wzrost
inst.wlosy = rasowe.wlosy
inst.oczy = rasowe.oczy
inst.szybkosc = rasowe.szybkosc
inst.punkty_bohatera = rasowe.punkty_bohatera
inst.punkty_przeznaczenia = rasowe.punkty_przeznaczenia


#########################################DZIAŁ PROFESJI############################################################################
########################IMPORT ODPOWIEDNIEGO MODUŁY PROFESJI
if inst.prof == "Aptekarz":
    import profesje.aptekarz
    profes = profesje.aptekarz.profes
    #print(profesje.aptekarz.__doc__)
if inst.prof == "Czarodziej":
    import profesje.czarodziej
    profes = profesje.czarodziej.profes
    #print(profesje.czarodziej.__doc__)
if inst.prof == "Inżynier":
    import profesje.inzynier
    profes = profesje.inzynier.profes
    #print(profesje.inzynier.__doc__)
if inst.prof == "Kapłan":
    import profesje.kaplan
    profes = profesje.kaplan.profes
    #print(profesje.kaplan.__doc__)
if inst.prof == "Medyk":
    import profesje.medyk
    profes = profesje.medyk.profes
if inst.prof == "Mnich":
    import profesje.mnich
    profes = profesje.mnich.profes
if inst.prof == "Prawnik":
    import profesje.prawnik
    profes = profesje.prawnik.profes
if inst.prof == "Uczony":
    import profesje.uczony
    profes = profesje.uczony.profes
if inst.prof == "Agitator":
    import profesje.agitator
    profes = profesje.agitator.profes
if inst.prof == "Kupiec":
    import profesje.kupiec
    profes = profesje.kupiec.profes
if inst.prof == "Mieszczanin":
    import profesje.mieszczanin
    profes = profesje.mieszczanin.profes
if inst.prof == "Rzemieślnik":
    import profesje.rzemieslnik
    profes = profesje.rzemieslnik.profes
if inst.prof == "Strażnik":
    import profesje.straznik
    profes = profesje.straznik.profes
if inst.prof == "Szczurołap":
    import profesje.szczurolap
    profes = profesje.szczurolap.profes
if inst.prof == "Śledczy":
    import profesje.sledczy
    profes = profesje.sledczy.profes
if inst.prof == "Żebrak":
    import profesje.zebrak
    profes = profesje.zebrak.profes
if inst.prof == "Artysta":
    import profesje.artysta
    profes = profesje.artysta.profes
if inst.prof == "Doradca":
    import profesje.doradca
    profes = profesje.doradca.profes
if inst.prof=="Namiestnik":
    import profesje.namiestnik
    profes = profesje.namiestnik.profes
if inst.prof == "Poseł":
    import profesje.posel
    profes = profesje.posel.profes
if inst.prof == "Służący":
    import profesje.sluzacy
    profes = profesje.sluzacy.profes 
if inst.prof == "Szlachcic":
    import profesje.szlachcic
    profes = profesje.szlachcic.profes 
if inst.prof == "Szpieg":
    import profesje.szpieg
    profes = profesje.szpieg.profes 
if inst.prof == "Zwadźca":
    import profesje.zwadzca
    profes = profesje.zwadzca.profes 
    profes = profesje.zwadzca.profes
if inst.prof == "Chłop":
    import profesje.chlop
    profes = profesje.chlop.profes 
if inst.prof == "Górnik":
    import profesje.gornik
    profes = profesje.gornik.profes 
if inst.prof == "Guślarz":
    import profesje.guslarz
    profes = profesje.guslarz.profes 
if inst.prof == "Łowca":
    import profesje.lowca
    profes = profesje.lowca.profes 
if inst.prof == "Mistyk":
    import profesje.mistyk
    profes = profesje.mistyk.profes
if inst.prof == "Zarządca":
    import profesje.zarzadca
    profes = profesje.zarzadca.profes
if inst.prof == "Zielarz":
    import profesje.zielarz
    profes = profesje.zielarz.profes
if inst.prof == "Zwiadowca":
    import profesje.zwiadowca
    profes = profesje.zwiadowca.profes
if inst.prof == "Biczownik":
    import profesje.biczownik
    profes = profesje.biczownik.profes
if inst.prof == "Domokrążca":
    import profesje.domokrazca
    profes = profesje.domokrazca.profes
if inst.prof == "Kuglarz":
    import profesje.kuglarz
    profes = profesje.kuglarz.profes
if inst.prof == "Łowca Czarownic":
    import profesje.lowca_czarownic
    profes = profesje.lowca_czarownic.profes
if inst.prof == "Łowca Nagród":
    import profesje.lowca_nagrod
    profes = profesje.lowca_nagrod.profes
if inst.prof == "Posłaniec":
    import profesje.poslaniec
    profes = profesje.poslaniec.profes
if inst.prof == "Strażnik Dróg":
    import profesje.straznik_drog
    profes = profesje.straznik_drog.profes
if inst.prof == "Woźnica":
    import profesje.woznica
    profes = profesje.woznica.profes
if inst.prof == "Doker":
    import profesje.doker
    profes = profesje.doker.profes
if inst.prof == "Flisak":
    import profesje.flisak
    profes = profesje.flisak.profes
if inst.prof == "Pilot Rzeczny":
    import profesje.pilot_rzeczny
    profes = profesje.pilot_rzeczny.profes
if inst.prof == "Pirat Rzeczny":
    import profesje.pirat_rzeczny
    profes = profesje.pirat_rzeczny.profes
if inst.prof == "Przemytnik":
    import profesje.przemytnik
    profes = profesje.przemytnik.profes
if inst.prof == "Przewoźnik":
    import profesje.przewoznik
    profes = profesje.przewoznik.profes
if inst.prof == "Strażnik Rzeczny":
    import profesje.straznik_rzeczny
    profes = profesje.straznik_rzeczny.profes
if inst.prof == "Żeglarz":
    import profesje.zeglarz
    profes = profesje.zeglarz.profes
if inst.prof == "Banita":
    import profesje.banita
    profes = profesje.banita.profes
if inst.prof == "Czarownica":
    import profesje.czarownica
    profes = profesje.czarownica.profes
if inst.prof == "Hiena Cmentarna":
    import profesje.hiena_cmentarna
    profes = profesje.hiena_cmentarna.profes
if inst.prof == "Paser":
    import profesje.paser
    profes = profesje.paser.profes
if inst.prof == "Rajfur":
    import profesje.rajfur
    profes = profesje.rajfur.profes
if inst.prof == "Rekietier":
    import profesje.rekietier
    profes = profesje.rekietier.profes
if inst.prof == "Szarlatan":
    import profesje.szarlatan
    profes = profesje.szarlatan.profes
if inst.prof == "Złodziej":
    import profesje.zlodziej
    profes = profesje.zlodziej.profes
if inst.prof == "Gladiator":
    import profesje.gladiator
    profes = profesje.gladiator.profes
if inst.prof == "Kapłan Bitewny":
    import profesje.kaplan_bitewny
    profes = profesje.kaplan_bitewny.profes
if inst.prof == "Kawalerzysta":
    import profesje.kawalerzysta
    profes = profesje.kawalerzysta.profes
if inst.prof == "Ochroniarz":
    import profesje.ochroniarz
    profes = profesje.ochroniarz.profes
if inst.prof == "Oprych":
    import profesje.oprych
    profes = profesje.oprych.profes
if inst.prof == "Rycerz":
    import profesje.rycerz
    profes = profesje.rycerz.profes
if inst.prof == "Zabójca":
    import profesje.zabojca
    profes = profesje.zabojca.profes
if inst.prof == "Żołnierz":
    import profesje.zolnierz
    profes = profesje.zolnierz.profes

############DODAJEMY RZUTY DO CECH O ILE UŻYTKOWNIK NIE WPISAŁ WŁASNYCH RZUTÓW

if inp_rzuty != "t":
    str_rzuty = ""
    for key, value in profes.cechy.items():
        str_rzuty = str_rzuty + str(key) + " - " + str(value) + "; "
    print(f"Wylosowane rzuty: {str_rzuty}")
    for cecha in inst.cechy:
        inst.cechy[cecha] = inst.cechy[cecha] + profes.cechy[cecha]

#zachowujemy bazowe rzuty
bazowe_cechy = {}
for key, value in inst.cechy.items():
    bazowe_cechy[key] = value

###########Podnosimy wartość cech, w zależności od tier'u. O 5 za każdy tier################DOPIERO TU ZACZYNAMY DODAWAĆ ROZWINIĘCIA CECH
#print(inst.cechy)

for cech, wart in profes.rozwiniecia_cech.items():
    
    #print("przed")
    #print(wart)
    wart = (wart + inst.tier) * 5
    #print("po")
    #print(wart)
    if wart > 0:
        inst.cechy[cech]= inst.cechy[cech] + wart


######ustalamy wartość umiejętności od profesji, 5 za każdyh tier począwszy od zera
for um in profes.umiejki:
    profes.umiejki[um] = profes.umiejki[um] + inst.tier
for um in profes.umiejki:
    profes.umiejki[um] = profes.umiejki[um] * 5


if podpis != "Created by DugSnaga":
    inst = 2
########Dodajemy wartośc umiejętności od profesji do umiejętności rasowych
##############  NIE ZAMIENIAJ PONIŻSZEGO NA 'DEL PROFES.UMIEJKI. JESLI PODCZAS ITERACJI ZNIKAJĄ WPISY PYTHON SIE WYKRZACZA
umiejkip = {}
for um, war in profes.umiejki.items():
    if war >0:
        umiejkip[um] = war

for um, war in umiejkip.items():
    if um in inst.umiejki:
        inst.umiejki[um] = inst.umiejki[um] + umiejkip[um]
    else:
        inst.umiejki[um] = war


###############TALENTY OD PROFESJI, W ZALEŻNOŚCI OD TIER'U. NA 0 JEDNA, NA 1 WSZYSTKIE Z PIERWSZEJ PROFESJI ETC
for key, wart in profes.talenty.items():
    wart = wart + inst.tier
    if wart > 0 and key not in inst.talenty:
        inst.talenty.append(key)



#############################DOBIERANIE WYPOSAŻENIA
for idx, wart in enumerate(profes.wyposazenie):
    
    if idx <= inst.tier:
        for el in profes.wyposazenie[idx]:
            inst.wyposazenie.append(el)


############################ZŁOTO
inst.status = profes.status[inst.tier]
if inst.status == "Złoto":
    inst.majatek = "1 ZK"
if inst.status == "Srebro":
    a = random.randint(1, 10)
    inst.majatek = f"{a} SS"
if inst.status == "Brąz":
        a = random.randint(2, 20)
        inst.majatek = f"{a} BP"

# print(inst.talenty)
# print(bazowe_cechy)
# print(inst.cechy)
############zwiększenie cech od talentów
#bazowych
if "Urodzony Wojownik" in inst.talenty:
    bazowe_cechy["WW"] = bazowe_cechy["WW"] + 5
if "Charyzmatyczny" in inst.talenty:
    bazowe_cechy["Ogd"] = bazowe_cechy["Ogd"] + 5
if "Błyskotliwość" in inst.talenty:
    bazowe_cechy["Int"] = bazowe_cechy["Int"] + 5
if "Bardzo silny" in inst.talenty:
    bazowe_cechy["S"] = bazowe_cechy["S"] + 5
if "Niezwykle Odporny" in inst.talenty:
    bazowe_cechy["Wt"] = bazowe_cechy["Wt"] + 5
if "Strzelec Wyborowy" in inst.talenty:
    bazowe_cechy["US"] = bazowe_cechy["US"] + 5
if "Szybki Refleks" in inst.talenty:
    bazowe_cechy["Zw"] = bazowe_cechy["Zw"] + 5
if "Zimna Krew" in inst.talenty:
    bazowe_cechy["SW"] = bazowe_cechy["SW"] + 5
if "Zręczny" in inst.talenty:
    bazowe_cechy["Zr"] = bazowe_cechy["Zr"] + 5
if "Czujny" in inst.talenty:
    bazowe_cechy["I"] = bazowe_cechy["I"] + 5

#i końcowych
if "Urodzony Wojownik" in inst.talenty:
    inst.cechy["WW"] = inst.cechy["WW"] + 5
if "Charyzmatyczny" in inst.talenty:
    inst.cechy["Ogd"] = inst.cechy["Ogd"] + 5
if "Błyskotliwość" in inst.talenty:
    inst.cechy["Int"] = inst.cechy["Int"] + 5
if "Bardzo silny" in inst.talenty:
    inst.cechy["S"] = inst.cechy["S"] + 5
if "Niezwykle Odporny" in inst.talenty:
    inst.cechy["Wt"] = inst.cechy["Wt"] + 5
if "Strzelec Wyborowy" in inst.talenty:
    inst.cechy["US"] = inst.cechy["US"] + 5
if "Szybki Refleks" in inst.talenty:
    inst.cechy["Zw"] = inst.cechy["Zw"] + 5
if "Zimna Krew" in inst.talenty:
    inst.cechy["SW"] = inst.cechy["SW"] + 5
if "Zręczny" in inst.talenty:
    inst.cechy["Zr"] = inst.cechy["Zr"] + 5
if "Czujny" in inst.talenty:
    inst.cechy["I"] = inst.cechy["I"] + 5


# print(inst.talenty)
# print(bazowe_cechy)
# print(inst.cechy)
#################  ŻYWOTNOŚĆ
s_b = int((inst.cechy["S"])/10)
wt_b = int((inst.cechy["Wt"])/10)
sw_b = int((inst.cechy["SW"])/10)

if inst.rasa == "Niziołek":
    inst.zywotnosc = 2*wt_b +sw_b
if inst.rasa != "Niziołek":
    inst.zywotnosc = s_b + (2* wt_b) + sw_b 
if "Twardziel" in inst.talenty:
    inst.zywotnosc = inst.zywotnosc + wt_b

####################NAZWA PROFESJI W ZALEŻNOŚCI OD TIER'U

inst.nazwa_profesji = profes.nazwa_profesji[inst.tier]

###########################FORMAT OUTPUTU
nazwa_pliku = str(inst.rasa) +"_"+ str(inst.nazwa_profesji)+"_"+str(inst.imie)+ ".txt"

pierwszy_wiersz = "Imie: " + str(inst.imie) + "      " + "Rasa: " + str(inst.rasa)+ "     Płeć: "+ str(inst.plec)+"     "+ "Profesja: " + str(inst.nazwa_profesji) +"      " + "Kariera: " + str(inst.prof)
drugi_wiersz ="Status: " + inst.status+"     " + "Poziom: " + str(inst.tier) +"    "+"Wzrost: "+ str(inst.wzrost)+ "    " +"Kolor Włosów: " + str(inst.wlosy) + "    "+"Kolor Oczu: " + str(inst.oczy) + "\n"

# nazwy tabeli cech 'WW', 'US', etc
trzeci_wiersz = ""
for key, value in inst.cechy.items():
    c = 7 - len(key)
    d = ""
    while c>0:
        d = d + " "
        c = c - 1
    trzeci_wiersz = trzeci_wiersz + str(key) + d
#cechy bazowe
czwarty_wiersza = ""
for key,value in bazowe_cechy.items():
    c = 5
    d = ""
    while c>0:
        d = d + " "
        c = c - 1
    czwarty_wiersza = czwarty_wiersza + str(value) + d

#wartość rozwinięć
czwarty_wierszb = ""

for key,value in inst.cechy.items():
    rozw = value - bazowe_cechy[key]
    c = 5 - len(str(rozw))
    d = ""
    while c>0:
        d = d + " "
        c = c - 1
    czwarty_wierszb = czwarty_wierszb + str(rozw) + d + "  "

#wartośc końcowa
czwarty_wiersz = ""
for key,value in inst.cechy.items():
    c = 5
    d = ""
    while c>0:
        d = d + " "
        c = c - 1
    czwarty_wiersz = czwarty_wiersz + str(value) + d

trzeci_wiersz = trzeci_wiersz + "Żyw" + "    " + "SZ" + "    " + "PP"+"    "+"PB"
czwarty_wiersz = czwarty_wiersz + str(inst.zywotnosc)+ "     " + str(inst.szybkosc)+"     "+str(inst.punkty_przeznaczenia)+"     "+str(inst.punkty_bohatera)
piaty_wiersz = "UMJEJĘTNOŚCI"
listow_um = ""
for key, val in inst.umiejki.items():
    listow_um = listow_um + str(key)+":"+ str(val) + "\n"

string_talentow = ""
a = 1
for el in inst.talenty:
    if a % 5 !=0:
        string_talentow = string_talentow + el+ "; "
    
    
    if a % 5 ==0:
        string_talentow = string_talentow + el + ";\n"
    a = a + 1

listow_tal ="TALENTY: " + string_talentow
a = 1
string_wyp = ""

for el in inst.wyposazenie:
    if a % 5 !=0:
        string_wyp = string_wyp + el + "; "

    if a % 5 ==0:
        string_wyp = string_wyp + el + ";\n"
    a = a +1
listow_maj = "WYPOSAŻENIE: "+ string_wyp + "\n" + "MAJĄTEK: " + str(inst.majatek)


##############wrzucam głupie hasełka. Warto wymyslec coż zabawniejszego
tips_of_a_day = [
    "Jak nadejdzie białe zimno, pamiętaj aby nie jeść żółtego śniegu", 
    "Pamiętaj żeby brać prysznic, ludzie będą Cię inaczej traktować, jesli nie będzie tego robić",
    "Jedz śniadania, gdyż zdrowe są one i smaczne",
    "Atakowanie postaci niezależnych może sprawić że staną się one wrogie",
    "Czas leczy rany, jednak nie wszystkie, niektóre wymagają pomocy medycznej",
    "Wiele postaci ma dużo do powiedzenia, jednak nie wszystko jest ważne",
    "Jesteś brzydki i wali ci z japy",
    "Mistrz Gry ma zawsze rację",
    r"Jeśli przyłożysz ucho do uda ciężarnej kobiety możesz usłyszeć 'Co Ty kurwa robisz?!'",
    "Lizanie klamek w niektórych kulturach uznawane jest za nietaktowne",
    "W większości miejsc nie możesz poruszać się nago, bez zwracania na siebie uwagi",
    "Jeśli ktoś Cię zaatakuje, możesz zostać ranny",
    "Pływanie? Na chuj to komu?",
    "W imperium nie ma mutantów!",
    "Jeśli Mistrz Gry mówi że czegoś nie można zrobić, polej mu kopa smaku",
    "Przyjaciele są jak drzewa. Upadną jeśli uderzysz je kilka razy siekierą",
    "Broń wymaga ostrzenia",
    "Podczas walki pancerz może ulec uszkodzeniu",
    "Sasin wydał 70 mln na wybory, które się nie odbyły",
    "Przed wyruszeniem w drogę należy zebrać drużynę",
    "Spożywanie napojów alkoholowych może wydłużyć czas podróży",
    "Jeśli MG na szybko losuje imię NPCa, możesz śmiało założyć że nie jest to ważna postać",
    "Granie niziołkiem może spowodować szybką utratę PPków i trwałym uszczerbkiem na zdrowiu psychicznym",
    "Pachu ma małego",
    "Jeśli koń jest podkuty łatwiej będzie Ci z niego spaść, niż kiedy idziesz pieszo",
    "Jeśli okradania złodzieja nie należy traktować jak kradzieży, to jeśli usunąć z tego łańcuszka złodzieja, wychodzi, że kradzież nie jest kradzieżą",
    "Pułapki w lochach mogą okazać się zabójcze",
    "Kalkuluje zajebistość postaci",
    "Jesteś pewien, że ta postać jest grywalna?",
    "Gdy ktoś Ci nasrał w buty, nie patrz do góry",
    "Ingerencja z chaosem to najszybszy sposób do wyhodowania sobie trzeciej ręki",
]

aacb = len(tips_of_a_day) - 1
random_tip = random.randint(0, aacb)

import time


#tip of a day
print(f"\n \n \n{tips_of_a_day[random_tip]} \n")
time.sleep(3)
print("Eksportuje postać do pliku o nazwie: " +nazwa_pliku + "\n \n \n \n ")
time.sleep(2)
######################################OUTPUT POSTACI W CMD
print(pierwszy_wiersz)
print(drugi_wiersz)
print(trzeci_wiersz)
print(czwarty_wiersza)
print(czwarty_wierszb)
print(czwarty_wiersz)
print("\n")
print("UMIEJĘTNOŚCI: \n")
print(listow_um)
print(listow_tal)
print(listow_maj)


#################################WKSPORT POSTACI DO PLIKU
with open(nazwa_pliku, "w") as file_object:
    file_object.write(pierwszy_wiersz + "\n")
    file_object.write(drugi_wiersz+"\n")
    file_object.write(trzeci_wiersz+"\n")
    file_object.write(czwarty_wiersza+"\n")
    file_object.write(czwarty_wierszb+"\n")
    file_object.write(czwarty_wiersz+"\n")
    file_object.write("\n")
    file_object.write("UMIEJĘTNOŚCI: \n")
    file_object.write(listow_um+ "\n")
    file_object.write(listow_tal+ "\n" + "\n")
    file_object.write(listow_maj+ "\n")
    file_object.write("\n \n \n")
    file_object.write(podpis)




