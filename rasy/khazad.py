"""
Krasnoludy albo „Dawi”, jak sami się nazywają – są uparte, 
a ichszorstkość w obejściu stała się legendarna. Chociaż większość mieszka
w ogromnych fortecach górskich, zwanych Twierdzami, w większości
dużych miast i w stolicy Reiklandu można znaleźć krasnoludzkich
mieszkańców. Ponieważ krasnoludy z natury łączą się
w klany, zazwyczaj trzymają się razem, tworząc enklawy i własne
dzielnice, gdziekolwiek się osiedlają. Wielu krasnoludów żyjących
w Reiklandzie to potomkowie tych, którzy przybyli z Utraconych
Twierdz wiele wieków temu. Mimo wszystko większość z nich uważa
się za krasnoludy z Gór Szarych, chociaż niektórzy nie widzieli
nawet wzgórz, o górach nie wspominając.
Kultura krasnoludów darzy szacunkiem biegłość w rzemiośle –
przede wszystkim kamieniarstwie, kowalstwie i inżynierii, a krasnoludzkie
Twierdze olśniewają prawdziwymi cudami techniki.
Poza tym krasnoludy są żądne złota i klejnotów, dlatego w poszukiwaniu
kamieni i metali szlachetnych drążą głębokie kopalnie
w górach. Jednakże większą czcią od dóbr doczesnych otaczają
swoją starszyznę i przodków. Nierzadko ważny antenat jest
obiektem kultu. Krasnoludy nie mają talentu do magii, ale kowale
run tworzą pokryte misternymi znakami artefakty, które kiełznają
magiczne moce. Krasnoludzka sprawność i biegłość w inżynierii
jest tak zdumiewająca, że niektóre z ich co bardziej pomysłowych
mechanizmów i maszyn parowych w oczach prostego ludu uchodzą
za magię.
Krasnoludy są przysadziste, mają szerokie klatki piersiowe oraz
muskularne kończyny. Ich rysy są jakby ciosane w kamieniu,
a włosy grube i gęste. Długie włosy są dumą krasnoluda i wyznacznikiem
jego statusu pośród innych krasnoludów, co często
jest podkreślane skomplikowanymi warkoczami i ozdobami.
Zgolenie brody lub ścięcie włosów jest dla krasnoluda ogromnym
dyshonorem. Właśnie honor jest pierwszorzędną cechą ich
charakteru. Krasnoludy są z natury dumne i bardzo pamiętliwe,
a urazę wobec wszystkich, którzy kiedykolwiek je znieważyli lub
pohańbili, chowają przez długie lata, podtrzymując niechęć przez
pokolenia. Niektóre z konfliktów i uraz powstały setki lat temu,
ale krasnoludy pielęgnują je, wiedząc, że przodkowie patrzą na ich
uczynki, a gorycz hańby nie przemija nawet po śmierci. Z drugiej
strony, choć przyjaźń przedstawiciela tej rasy zdobyć niezwykle
trudno, to raz ofiarowana łączy trwale i nie ma żadnych granic.
Mimo iż krasnoludy nie żyją tak długo jak niemal nieśmiertelne
elfy, ciągle mogą chodzić po ziemi setki lat. Niektórzy twierdzą
nawet, że krasnolud nie umrze tak długo, jak ma cel w życiu, chyba
że zostanie powalony w bitwie. To dobry przykład przeświadczenia
o uporze i konsekwencji tej rasy.

"""

import random

cechy= {
    "WW" : 30,
    "US" : 20, 
    "S" : 20,
    "Wt" : 30,
    "I" : 20,
    "Zw" : 10,
    "Zr" : 30,
    "Int" : 20,
    "SW" : 40,
    "Ogd" : 10,
}

umiejki= ["Broń Biała (Podstawowa)", 
    "Język (Khazalid)", 
    "Opanowanie" ,
    "Mocna Głowa", 
    "Rzemiosło (Dowolne)", 
    "Wiedza (Geologia)",
    "Wiedza (Krasnoludy)", 
    "Wiedza (Metalurgia)", 
    "Wycena", 
    "Występy (Gawędziarstwo)",
    "Zastraszanie"]

talentyx = ["Odporny na Magię", "Tragarz", "Widzenie w Ciemności"]

talenty2 = ["Czytanie/Pisanie", "Nieustępliwy"]
talenty3 = ["Odporność Psychiczna", "Nieugięty"]


wzrost = [130, 2]

imiona_m = ["Alarik", "Alrik", "Argat", "Argorn", "Arngrim", "Azram", "Azrel", "Bafur", "Baldrik", "Balim", "Balin", "Balzud", "Bardin", "Barnok", "Beledar", "Belorn", "Bifur", "Bohdi", "Boltrez", "Bombur", "Borek", "Borgin", "Borig", "Borri","Bragi", "Brand", "Brock", "Broderin", "Brokk", "Brond", "Brun", "Burlok", "Dain", "Darin", "Darluk", "Decredie", "Deemax", "Dern", "Dimzad", "Dirk", "Dolgan", "Dori", "Dorin", "Dowbur", "Dron", "Drumin", "Dumwin", "Duncan", "Dunnor", "Durin", "Durlag", "Durnatz", "Dwalin", "Fimbur", "Fjalar", "Flint", "Frar", "Fundin", "Gafar", "Garag", "Garil", "Garin", "Garick", "Garm", "Gazil", "Gazula", "Gazunda", "Gharth", "Gimli", "Gloin", "Glosh", "Gnarok", "Gnimsh", "Gomrund", "Gotmong", "Gorm", "Gorum", "Gotran", "Gotrek", "Gotri", "Grallen", "Greip", "Grim", "Grimnir", "Grolf", "Grom", "Grommo", "Gromph", "Grum", "Grun", "Grunthor", "Hadrin", "Hagmar", "Hagri", "Haki", "Hannar", "Hargin", "Hargrim", "Helgrind", "Holgar", "Hornborin", "Hrotghar",
"Hekrath", "Ibun", "Ivan", "Kargan", "Kargrim", "Kazador", "Kazgar", "Kazrik", "Ketiger", "Kharas", "Kili", "Kragg", "Krangal", "Lofar", "Logi", "Mabal", "Malakai", "Malkar", "Melhorn", "Mimir", "Modi", "Molrik", "Nabbi", "Nahar", "Nain", "Narg", "Nester", "Nibin", "Nordri", "Nori", "Norin", "Nyrad", "Odum", "Oinn", "Okri", "Palin", "Ranhar", "Reghar", "Reck", "Reginn", "Reorx", "Rind", "Rogar", "Serg", "Sirrush",
"Skaagne", "Skalf", "Snorri", "Sorgi", "Stapmi", "Steg", "Stron", "Sudri", "Surt", "Taggin", "Tairon", "Teran", "Thadrin", "Thain", "Thekkr", "Thingrim", "Thir", "Thor", "Thorek", "Thorgal", "Thorgrim", "Thorin", "Throd", "Thror,Thunar", "Tingrim", "Trygg", "Turin", "Tyorl", "Ug", "Ulfar", "Ulli", "Ulther", "Uther", "Ungrim", "Varek", "Wargrim", "Westri", "Widar", "Wjard", "Yarpen", "Yazeran", "Ymir", "Yodri", "Yog", "Zonri"]


imiona_z = ["Akre", "Ametrin", "Amma", "Angeya", " Angrboda", " Ankharma", " Anvila", " Arka", " Arrica", " Athrina", " Atla", " Aurboda", " Ayla", " Azlana", " Azraya", " Bestla", " Beyla", " Blid", " Boria", " Daina", " Dalla", " Danra", " Diara", " Drumba", " Dunerka", " Edria", " Eistla", " Erna", " Eudora", " Farmira", " Fulla", " Gael", " Gasta", " Gilderia", " Grella", " Helgar", " Hilga", " Jaheira", 
"Janara", " Jarnsaksa", " Jorika", " Kamira", " Kathara", " Keira", " Keri", " Krina", " Layfeja", " Magda", " Margara", " Meili", " Meure", " Modira", " Myrtha", " Oria", " Renfri", " Rhizma", " Rigunta", " Runa", " Serewassa", " Siri", " Sylga", " Teria", " Terigne", " Tesela", " Tessa", " Thera", " Therla", " Titta", " Ulfrun", " Ulla", " Umina", " Valaya", " Vanirka", " Varna", " Vigaya"]



wlosy = {0 : "Blond",
1 : "Lniany",
2 : "Rudawy",
3 : "Brązowy",
4 : "Brązowy",
5 : "Brązowy",
6 : "Miedziany",
7 : "Miedziany",
8 : "Miedziany",
9 : "Miedziany",
10 : "Brąz",
11 : "Brąz",
12 : "Brąz",
13 : "Brąz",
14 : "Brąz",
15 : "Brąz",
16 : "Ciemny brąz",
17 : "Rudy brąz",
18 : "Czarny"} 

oczy = {0 : "Czarny jak wegiel",
1 : "Szary jak olów",
2 : "Stalowoszary",
3 : "Niebieski",
4 : "Niebieski",
5 : "Niebieski",
6 : "Brązowy jak ziemia",
7 : "Brązowy jak ziemia",
8 : "Brązowy jak ziemia",
9 : "Brązowy jak ziemia",
10 : "Ciemnobrązowy",
11 : "Ciemnobrązowy",
12 : "Ciemnobrązowy",
13 : "Orzechowy",
14 : "Orzechowy",
15 : "Orzechowy",
16 : "Zielony",
17 : "Ciemny miedziany",
18 : "Złoty",}


class Rasa():
    def __init__(self, cechy, umiejki, talenty, wzrost, imie_m, imie_z, wlosy, oczy, profesja, punkty_przeznaczenia = 0, punkty_bohatera = 0,):
        self.cechy = cechy
        self.umiejki = umiejki
        self.talenty = talenty
        self.wzrost = wzrost
        self.imie_m = imie_m
        self.imie_z = imie_z  
        self.wlosy = wlosy
        self.oczy = oczy
        self.profesja = profesja
        self.szybkosc = 3
        self.punkty_przeznaczenia = punkty_przeznaczenia
        self.punkty_bohatera = punkty_bohatera


punkty_bohatera0 = 0
punkty_przeznaczenia0 = 2
punkty_wolne = 2



umiejkix = None
wzrostx = None
imiex_m = None
imiex_z = None
wlosx = None
oczyx = None
profesje = None
punkty_przeznaczeniax = None
punkty_bohaterax = None

########MIEJSCE NA INPUT PUNKTÓW PRZEZNACZENIA I BOHATERA
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


profesje = {
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




############LOSOWANIE IMION DAMSKICH, ŻEŃSKICH, ORAZ NAZWISKA. MIEJSCE NA INPUT WYBRANEGO IMIENIA BYŁ W GŁÓWNYM PLIKU
############ ZARAZ PO INSTANCJOWANIU KLASY POSTAĆ
los = random.randint(0,74)
a = imiona_z[los]
los = random.randint(0,191)
b = imiona_m[los]
imiex_z = a + " " + b + "sdottir"


los = random.randint(0,191)
a = imiona_m[los]
los = random.randint(0,191)
b = imiona_m[los]
imiex_m =  a + " " + b + "son"




rasowe = Rasa(cechy, umiejkix, talentyx, wzrostx, imiex_m, imiex_z, wlosx, oczyx, profesje, punkty_przeznaczeniax, punkty_bohaterax )


