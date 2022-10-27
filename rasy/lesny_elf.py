"""
Leśne elfy to rzadki widok w Reiklandzie i są ku temu dobre powody.
W ostatnich fazach Wojny o Brodę większość elfów wycofała się ze Starego
Świata, a niewielka grupa tych, które zdecydowały się zostać, wróciła
w głąb magicznych lasów, które teraz są ich domem. Ponad trzy tysiące
lat izolacji, trudów i wojen sprawiły, że „leśne elfy” znacznie różnią się
kulturowo od swoich kuzynów, wysokich elfów.
Życie leśnych elfów jest ściśle związane z naturą, a ich społeczeństwo
przemieszane jest z duchami lasów. Są odludkami, którzy wkładają
mnóstwo wysiłku w to, by pozostawać niewidocznymi, a ich leśne
siedziby są zmyślnie skryte potężnymi iluzjami i zwodniczą magią.
Rzadko się zdarza, że opuszczają granice swoich ukrytych w puszczy
domen, a dzieje się to zwykle w wyniku wojny. Te zaś toczą zarówno
z sąsiadami, jak i mroczniejszymi siłami. Ze względu na brak znajomości
leśnych elfów inne ludy Starego Świata uważają je za nieobliczalne
i kapryśne.
W Reiklandzie zazwyczaj widuje się przedstawicieli dwóch szczepów
leśnych elfów: „Asrai” z Athel Loren za Górami Szarymi i „Eonirów”
z Lasu Laurelorn, daleko na północy Nordlandu.
Bezlitośni Asrai z Athel Loren są skrytymi ksenofobami, którzy
rzadko zapuszczają się poza swoje włości. Jednakże ponad dekadę
temu wieszczka Naith zobaczyła potencjalną śmierć Athel Loren.
Z tej przyczyny Król i Królowa Lasu, uznając, że zagrożenie przyjdzie
z zewnątrz, z rąk obcych, wysłali grupy wytatuowanych wojowników
klanowych poza Athel Loren, by polowali na wrogów lasu,
zanim ci w ogóle do niego dotrą.
Te brutalne oddziały są czasami dowodzone przez maga, „Pieśniarza
Zaklęć”, który otwiera magiczne ścieżki w Korzeniach Świata, by
transportować oddziały między Athel Loren a sercami puszcz dawno
utraconych przez elfy, ale jeszcze nietkniętych przez ludzką cywilizację
lub Chaos. Czasami zdarza się, że tacy dzicy myśliwi uznają, że mają
wspólny cel z innymi mieszkańcami Starego Świata. Pojedyncze elfy
wychodzą nawet z cieni, by przyłączyć się do walki z większym złem.
Z drugiej strony Królowa Laurelorn natomiast obrała zupełnie inną
drogę interpretacji tej przepowiedni. Posłała niedawno liczną delegację,
która założyła obóz w głębi lasów Bursztynowych Wzgórz, na
południe od Altdorfu. Te elfy bacznie obserwują politykę ludzi, zarówno
tę tyczącą się Laurelorn, jak i innych zdarzeń. Co jakiś czas
interweniują też w sprawach, które uznają za wystarczająco ważne.
Elfy uznają obóz za rozwiązanie „tymczasowe”, lecz dla innych, nie tak
długowiecznych ras, znaczenie tego słowa jest zupełnie inne. Dzięki
założeniu tej placówki liczebność leśnych elfów w Reiklandzie stale
wzrasta. Coraz więcej decyduje się opuścić cień drzewa i ruszyć w wędrówkę
po prowincji, realizując przy tym sobie tylko znane cele, na co
dzień przyjmując role myśliwych lub artystów.

"""

import random

profesje = {1 : "Czarodziej",
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


cechy= {
    "WW" : 30,
    "US" : 30, 
    "S" : 20,
    "Wt" : 20,
    "I" : 40,
    "Zw" : 30,
    "Zr" : 30,
    "Int" : 20,
    "SW" : 30,
    "Ogd" : 20,
}

szybkosc = 4
punkty_bohatera0 = 0
punkty_przeznaczenia0 = 0
punkty_wolne = 2

umiejki= ["Atletyka", "Broń Biała (Podstawowa)", "Broń Zasięgowa (Łuk)", "Język (Eltharin)", "Odporność", "Percepcja", "Skradanie", "Sztuka Przetrwania", "Tropienie", "Wspinaczka", "Występy (Śpiewanie)", "Zastraszanie"]

talentyx = ["Włóczykij", "Widzenie w Ciemności", "Wyczulony Zmysł (Wzrok)"]

talenty2 = [ "Twardziel", "Percepcja Magiczna"]
talenty3 = ["Czytanie/Pisanie", "Niezwykle Odporny"]


wzrost = [180, 3]

imiona1 = {1 : "Aes",
2 : "Ath",
3 : "Dor",
4 : "Far",
5 : "Gal",
6 : "Im",
7 : "Lin",
8 : "Mal",
9 : "Mor",
10 : "Ullia"}

imiona2 = {1 : "a",
2 : "ath",
3 : "dia",
4 : "en",
5 : "for",
6 : "lor",
7 : "mar",
8 : "ol",
9 : "sor",
10 : "than"}

imiona3 = {1 : "arha",
2 : "anhu",
3 : "dda",
4 : "han",
5 : "loc",
6 : "noc",
7 : "oth",
8 : "ryn",
9 : "stra",
10 : "wyth"}

wlosy = {0 : "Brzozowobialy",
1 : "Blond",
2 : "Różowe zloto",
3 : "Miodowoblond",
4 : "Miodowoblond",
5 : "Miodowoblond",
6 : "Brązowy",
7 : "Brązowy",
8 : "Brązowy",
9 : "Brązowy",
10 : "Mahoniowy",
11 : "Mahoniowy",
12 : "Mahoniowy",
13 : "Ciemny brąz",
14 : "Ciemny brąz",
15 : "Ciemny brąz",
16 : "Sjena",
17 : "Hebanowy",
18 : "Niebiesko-czarny"
} 

oczy = {0 : "Kość słoniowa",
1 : "Antracyt",
2: "Kolor bluszczu",
3: "Kolor mchu",
4 : "Kolor mchu",
5 : "Kolor mchu",
6 : "Kasztanowy",
7 : "Kasztanowy",
18 : "Kasztanowy",
9 : "Kasztanowy",
10 : "Kasztanowy",
11 : "Kasztanowy",
12 : "Kasztanowy",
13 : "Ciemnobrązowy",
14 : "Ciemnobrązowy",
15 : "Ciemnobrązowy",
16 : "Jasnobrązowy",
17 : "Złotobrązowy",
18 : "Fiołkowy",}



class Rasa():
    def __init__(self, cechy, umiejki, talenty, wzrost, imie_m, imie_z, wlosy, oczy, profesja, punkty_przeznaczenia, punkty_bohatera):
        self.cechy = cechy
        self.umiejki = umiejki
        self.talenty = talenty
        self.wzrost = wzrost
        self.imie_m = imie_m
        self.imie_z = imie_z  
        self.wlosy = wlosy
        self.oczy = oczy
        self.profesja = profesja
        self.szybkosc = szybkosc
        self.punkty_przeznaczenia = punkty_przeznaczenia
        self.punkty_bohatera = punkty_bohatera


umiejkix = None
wzrostx = None
imiex_m = None
imiex_z = None
wlosx = None
oczyx = None
punkty_przeznaczeniax = None
punkty_bohaterax = None

#########################MIEJSCE NA INPUT DLA PUNKTÓW PRZEZNACZENIA I BOHATERA
zasieg =[]
cab = punkty_wolne
while cab >= 0:
    zasieg.append(str(cab))
    cab = cab - 1

input_pp = input (f"Twoja rasa startowo posiada początkowo {punkty_bohatera0} punków bohatera, oraz {punkty_przeznaczenia0} punktów przeznaczenia, oraz {punkty_wolne} punktów do rozdania. Ile z nich chciałbyś przeznaczyć na punkty przeznaczenia? (0-{punkty_wolne}) \n" )

if input_pp in zasieg:
    punkty_przeznaczeniax = punkty_przeznaczenia0 + int(input_pp)
    punkty_wolne = punkty_wolne - int(input_pp)
    punkty_bohaterax = punkty_bohatera0 + punkty_wolne


if punkty_bohaterax == None or punkty_przeznaczeniax == None:
    print("Podana wartość jest z dupy, losuje ilość PPeków \n")
    a = random.randint(0, punkty_wolne)
    punkty_bohaterax = punkty_bohatera0 + a
    b = punkty_wolne - a
    punkty_przeznaczeniax = punkty_przeznaczenia0 + b

print(f"Twoja postać posiada {punkty_przeznaczeniax} punktów przeznaczenia i {punkty_bohaterax} punktów bohatera \n")

##############Decydujemy czy rasowe umiejętności i talenty będa losowane

wybor_umiejek = input("Czy chcesz wybrać wybieralne umiejętności i talenty rasowe? W przeciwnym razie będa one wylosowane(t/n): \n")
##################MIEJSCE NA INPUT DLA WYBIERALNYCH TALENTÓW

if wybor_umiejek == "t":
    zasieg = ["1", "2"]
    whale = 1
    while whale == 1:
        input_tal1 = input(f"Który talent rasowy chcesz wybrać? {talenty2[0]}-1, czy {talenty2[1]}-2? (1-2)  ")
        if input_tal1 in zasieg:
            a = int(input_tal1) -1
            talentyx.append(talenty2[a])
            whale = 2
        if input_tal1 not in zasieg:
            print("Podana wartość jest błędna. Spróbuj jeszcze raz, to naprawdę nie jest trudne")


    
    whale = 1
    while whale == 1:
        input_tal2 = input(f"Który talent rasowy chcesz wybrać? {talenty3[0]} - 1, czy {talenty3[1]} - 2?(1-2)  ")
        if input_tal2 in zasieg:
            a = int(input_tal2) -1
            talentyx.append(talenty3[a])
            whale = 2
        if input_tal2 not in zasieg:
            print("Podana wartość jest błędna. Spróbuj jeszcze raz, to naprawdę nie jest trudne")


##########losowanie talentów 
if wybor_umiejek != "t":
        #losowanie talentów
    los_tal1 = random.randint(0,1)
    talentyx.append(talenty2[los_tal1])        
    los_tal2 = random.randint(0,1)
    talentyx.append(talenty3[los_tal2])



print(f"Oto lista Twoich talentów: \n {talentyx} \n")

#print(talentyx)

################MIEJSCE NA INPUT WYBORU UMIEJEK

if wybor_umiejek == "t":
    print("Teraz możesz wybrać 3 umiejętności rasowe, które będą miały wartość 5 i 3 które będa miały wartość 3. Oto lista umiejetności: \n  ")

    umiejki_dict = {}
    for idx, wart in enumerate(umiejki):
        umiejki_dict[idx] = wart

    umiejki_str = ""
    a = 1

    for key, value in umiejki_dict.items():
        b = ""
        c = len(value)
        d = 30 - len(value) - len(str(key))

        while d > 0:
            b = b + " "
            d = d - 1

        if a % 4 != 0:
            umiejki_str = umiejki_str + str(key)+ " - " + value + b
            #print(umiejki_str)
    
        if a % 4 == 0:
            umiejki_str = umiejki_str + str(key)+ " - " + value + "\n"
            #print(umiejki_str)
        a = a + 1

    print(umiejki_str)

    wh = 1
    while wh == 1:
        ilosc_umiejetnosci_do_wyboru = (len(umiejki)-1)
        zasieg_um = []
        for key, value in umiejki_dict.items():
            zasieg_um.append(str(key))

        in_um5a = input(f"Wybierz pierwszą umiejętność, która będzie na poziomie 5 (0-{ilosc_umiejetnosci_do_wyboru}) ")
        in_um5b = input(f"Wybierz drugą umiejętność, która będzie na poziomie 5 (0-{ilosc_umiejetnosci_do_wyboru}) ")
        in_um5c = input(f"Wybierz trzecią umiejętność, która będzie na poziomie 5 (0-{ilosc_umiejetnosci_do_wyboru}) ")
        in_um3a = input(f"Wybierz pierwszą umiejętność, która będzie na poziomie 3 (0-{ilosc_umiejetnosci_do_wyboru}) ")
        in_um3b = input(f"Wybierz drugą umiejętność, która będzie na poziomie 3 (0-{ilosc_umiejetnosci_do_wyboru}) ")
        in_um3c = input(f"Wybierz trzecią umiejętność, która będzie na poziomie 3 (0-{ilosc_umiejetnosci_do_wyboru}) ")
        umiejkix = {}

        if in_um5a in zasieg_um:
            a = int(in_um5a)
            if umiejki[a] not in umiejkix:
                umiejkix[umiejki[a]] = 5

        if in_um5b in zasieg_um:
            a = int(in_um5b)
            if umiejki[a] not in umiejkix:
                umiejkix[umiejki[a]] = 5

        if in_um5c in zasieg_um:
            a = int(in_um5c)
            if umiejki[a] not in umiejkix:
                umiejkix[umiejki[a]] = 5

        if in_um3a in zasieg_um:
            a = int(in_um3a)
            if umiejki[a] not in umiejkix:
                umiejkix[umiejki[a]] = 3

        if in_um3b in zasieg_um:
            a = int(in_um3b)
            if umiejki[a] not in umiejkix:
                umiejkix[umiejki[a]] = 3

        if in_um3c in zasieg_um:
            a = int(in_um3c)
            if umiejki[a] not in umiejkix:
                umiejkix[umiejki[a]] = 3
        
        if len(umiejkix) == 6:
            wh = 2
            str_umtnsc = ""
            for key, value in umiejkix.items():
                str_umtnsc = str_umtnsc + key + " - "+ str(value) + "\n"
            
            print (f"Wybrane umiejętności to \n{str_umtnsc}")
        
        if len(umiejkix) != 6:
            print(f"Coś zjebałeś. Spróbuj jeszcze raz. Pamiętaj że musisz wybrać liczbę z przedziału 0 - {ilosc_umiejetnosci_do_wyboru}, oraz że nie możesz dwa razy wybrać tej samej umiejętności")

if wybor_umiejek != "t":
    #losowanie_umiejek
    print("Umiejętności będą losowane")
    a = 3
    umiejkix = {}
    while a > 0:
        los_um = random.randint(0,10)
        if umiejki[los_um] not in umiejkix:
            umiejkix[umiejki[los_um]] = 5
            a = a -1
        else:
            continue

    b=3
    while b > 0:
        los_um = random.randint(0,10)
        if umiejki[los_um] not in umiejkix:
            umiejkix[umiejki[los_um]] = 3
            b = b - 1
        else:
            continue



#print(umiejkix)
################ MIEJSCE NA INPUT WZROSTU
##########PYTANIE CZY CHCESZ PODAWAĆ PIERDY
input_pierdy = input("Czy chcesz podawać wzrost, kolor włosów i oczu? (t/n) ")

if input_pierdy == "t":
    zas = []
    a = 10*wzrost[1]
    b = wzrost[0]
    while a>=0:
        c = str(b)
        zas.append(c)
        a = a - 1
        b = b + 1
    whale = 1
    while whale == 1:
        input_wzrost = input(f"Podaj wzrost z przedziału ({wzrost[0]} - {wzrost[0] + wzrost[1]*10}) ")
        if input_wzrost in zas:
            in_wzr = int(input_wzrost)
            wzrostx = in_wzr
            whale = 2
        if input_wzrost not in zas:
            (print("Podana wartość jest błędna. Spróbuj jeszcze raz, to naprawdę nie jest trudne"))

if wzrostx == None:
    #losowanie wzrostu
    a = wzrost[1]
    wzrostx = wzrost[0]
    while a > 0:
        los = random.randint(1,10)
        wzrostx = wzrostx + los
        a = a - 1


########################MIEJSCE NA INPUT WŁOSÓW
if input_pierdy == "t":
    wlosy_str = ""
    a = 1

    for key, value in wlosy.items():
        b = ""
        c = len(value)
        d = 25 - len(value) - len(str(key))

        while d > 0:
            b = b + " "
            d = d - 1

        if a % 4 != 0:
            wlosy_str = wlosy_str + str(key)+ " - " + value + b
            #print(wlosy_str)
        if a % 4 == 0:
            wlosy_str = wlosy_str + str(key)+ " - " + value + "\n"
            #print(wlosy_str)
        a = a + 1

    print("\n" + wlosy_str)

    zasig =[]
    for key in wlosy:
        a = str(key)
        zasig.append(a)

    c = zasig[0]
    d=zasig[-1]
    whale = 1
    while whale == 1:
        input_wlos = input(f"Tu wybierasz włosy ({c}-{d}) ")
        if input_wlos in zasig:
            f = int(input_wlos)
            wlosx = wlosy[f]
            whale = 2
        if input_wlos not in zasig:
            (print("Podana wartość jest błędna. Spróbuj jeszcze raz, to naprawdę nie jest trudne!"))


if wlosx == None:
    #losowanie włosów
    los_wlos = random.randint(0, 18)
    wlosx = wlosy[los_wlos]

#print(wlosx)

#################################MIEJSCE NA INPUT OCZÓW
if input_pierdy == "t":
    oczy_str = ""
    a = 1

    for key, value in oczy.items():
        b = ""
        c = len(value)
        d = 20 - len(value) - len(str(key))

        while d > 0:
            b = b + " "
            d = d - 1

        if a % 5 != 0:
            oczy_str = oczy_str + str(key)+ " - " + value + b
            #print(oczy_str)
        if a % 5 == 0:
            oczy_str = oczy_str + str(key)+ " - " + value + "\n"
            #print(oczy_str)
        a = a + 1

    print("\n" + oczy_str)

    zasig =[]
    for key in oczy:
        a = str(key)
        zasig.append(a)

    c = zasig[0]
    d=zasig[-1]
    whale = 1
    while whale == 1:
        input_oczy = input(f"Tu wybierasz oczy ({c}-{d}) ")
        if input_oczy in zasig:
            f = int(input_oczy)
            oczyx = oczy[f]
            whale = 2
        
        if input_oczy not in zasig:
            (print("Podana wartość jest błędna. Spróbuj jeszcze raz, to naprawdę nie jest trudne!"))


if oczyx == None:
    #losowanie oczów
    los_wlos = random.randint(0, 18)
    oczyx = oczy[los_wlos]





############LOSOWANIE IMION DAMSKICH, MĘSKICH, ORAZ NAZWISKA. MIEJSCE NA INPUT WYBRANEGO IMIENIA BYŁ W GŁÓWNYM PLIKU
############ ZARAZ PO INSTANCJOWANIU KLASY POSTAĆ
los = random.randint(1,10)
a = imiona1[los]
los = random.randint(1,10)
b = imiona2[los]
los = random.randint(1,10)
c = imiona3[los]
imiex_z = a + b + c


los = random.randint(1,10)
a = imiona1[los]
los = random.randint(1,10)
b = imiona2[los]
los = random.randint(1,10)
c = imiona3[los]
imiex_m = a + b + c



rasowe = Rasa(cechy, umiejkix, talentyx, wzrostx, imiex_m, imiex_z, wlosx, oczyx, profesje, punkty_przeznaczeniax, punkty_bohaterax)


