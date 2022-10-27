"""
Niziołki są wszechobecne w całym Reiklandzie, przeważnie świadczą
wszelkiej maści usługi we wszystkich miastach. W stolicy Reiklandu,
Altdorfie, mają nawet swoją dzielnicę, zwaną Haffenstadt. Kłębią się
w niej setki wielopokoleniowych rodzin niziołków, prowadzących swoje
restauracje, karczmy, sklepy z zielem fajkowym i niezliczone uliczne
kramiki z jedzeniem. Niziołki to powszechny widok także w wielu wioskach
Reiklandu, nie dziwota więc, że wielu z nich pracuje w karczmach
albo prowadzi własne gospodarstwa. Z natury są bardzo społeczne,
wolą żyć w zżytych grupach rodzinnych, dzieląc się domami, pokojami
i łóżkami z mnóstwem przyjaciół i krewnych. Każdy daje coś od siebie
i dzieli się tym, co ma. Ze względu na styl życia wiele niziołków ma
problem z ideą prywatnej własności i przestrzeni.
Niziołki słyną z zainteresowania genealogią, a wiele klanów może
wymienić swoich przodków na wiele setek lat wstecz, aż do założenia
Krainy Zgromadzenia (autonomicznej prowincji niziołków w Imperium).
Starszy Krainy Zgromadzenia – aktualnie jest nim Hisme
Stoutheart – jest strażnikiem Haffenlyver, starożytnego, haftowanego
zwoju, szczegółowo opisującego główne linie rodowe pierwotnych
klanów. Zwój ten uchodzi za największy skarb niziołków.
Inną osobliwością niziołków jest dziwna sympatia, jaką okazują im
ogry. Mimo ich wilczego apetytu i zamiłowania do jedzenia wszystkiego,
co nawinie im się pod rękę, te wielkoludy wydają się szanować
niziołki. Istotnie, niziołki brygadziści często nadzorują ogrów
robotników, a większość oddziałów ogrów-najemników ma w swych
szeregach kucharza niziołka.
Niziołki są niskie, pucułowate i nie rośnie im zarost. Przypominają
wielkookie ludzkie dzieci o okrągłych twarzach, i ciałach, a ich
pogodne usposobienie i wijące się, kręcone włosy tylko potęgują to
wrażenie. Znane są ze swojego ogromnego apetytu i braku poszanowania
przestrzeni osobistej (przytulają bez pytania), ograniczeń społecznych
(„Moja babka stryjeczna spiknęła się z moim najlepszym
kumplem, musisz usłyszeć, co nawyrabiali!”) oraz prawa własności
(„Przecież on tego nie używa!”). Zwłaszcza ostatnia kwestia bywa
problematyczna, przez to niejeden niziołek wylądował już w więzieniu
za kradzież.

"""

import random

profesje = {1: 'Aptekarz', 2: 'Inżynier', 3: 'Medyk', 4: 'Medyk', 5: 'Prawnik', 6: 'Prawnik', 7: 'Uczony', 8: 'Uczony', 9: 'Agitator', 10: 'Agitator', 11: 'Kupiec', 12: 'Kupiec', 13: 'Kupiec', 14: 'Kupiec', 15: 'Mieszczanin', 16: 'Mieszczanin', 17: 'Mieszczanin', 18: 'Rzemieślnik', 19: 'Rzemieślnik', 20: 'Rzemieślnik', 21: 'Rzemieślnik', 22: 'Rzemieślnik', 23: 'Strażnik', 24: 'Strażnik', 25: 'Szczurołap', 26: 'Szczurołap', 27: 'Szczurołap', 28: 'Śledczy', 29: 'Śledczy', 30: 'Żebrak', 31: 'Żebrak', 32: 'Żebrak', 33: 'Żebrak', 34: 'Artysta', 35: 'Poseł', 36: 'Doradca', 37: 'Namiestnik', 38: 'Namiestnik', 39: 'Poseł', 40: 'Służąca', 41: 'Służąca', 42: 'Służąca', 43: 'Służąca', 44: 'Służąca', 45: 'Służąca', 46: 'Szpieg', 47: 'Chłop', 48: 'Chłop', 49: 'Chłop', 50: 'Górnik', 51: 'Łowca', 52: 'Łowca', 53: 'Zarządca', 54: 'Zielarz', 55: 'Zielarz', 56: 'Zielarz', 57: 'Zwiadowca', 58: 'Domokrążca', 59: 'Domokrążca', 60: 'Kuglarz', 61: 'Kuglarz', 62: 'Kuglarz', 63: 'Łowca Nagród', 64: 'Posłaniec', 65: 'Posłaniec', 66: 'Strażnik Dróg', 67: 'Woźnica', 68: 'Woźnica', 69: 'Doker', 70: 'Doker', 71: 'Doker', 72: 'Flisak', 73: 'Flisak', 74: 'Flisak', 75: 'Pilot Rzeczny', 76: 'Przemytnik', 77: 'Przemytnik', 78: 'Przemytnik', 79: 'Przemytnik', 80: 'Przewoźnik', 81: 'Strażnik Rzeczny', 82: 'Żeglarz', 83: 'Banita', 84: 'Paser', 85: 'Hiena Cmentarna', 86: 'Rajfur', 87: 'Rajfur', 88: 'Rajfur', 89: 'Rekietier', 90: 'Szarlatan', 91: 'Złodziej', 92: 'Złodziej', 93: 'Złodziej', 94: 'Złodziej', 95: 'Gladiator', 96: 'Ochroniarz', 97: 'Ochroniarz', 98: 'Żołnierz', 99: 'Żołnierz', 100: 'Żołnierz'}


cechy= {
    "WW" : 10,
    "US" : 30, 
    "S" : 10,
    "Wt" : 20,
    "I" : 20,
    "Zw" : 20,
    "Zr" : 30,
    "Int" : 20,
    "SW" : 30,
    "Ogd" : 30,
}

szybkosc = 3
punkty_bohatera0 = 2
punkty_przeznaczenia0 = 0
punkty_wolne = 3

umiejki= ["Charyzma", "Hazard", "Intuicja", "Język (Krainy Zgromadzenia)", "Mocna Głowa", "Percepcja", "Rzemiosło (Kucharz)", "Skradanie (Dowolne)", "Targowanie", "Unik", "Wiedza (Reikland)", "Zwinne Palce"]

talentyx = ["Mały", "Odporność na Chaos", "Widzenie w Ciemności", "Wyczulony Zmysł (Smak)"]

# talenty2 = [ "Szósty Zmysł", "Percepcja Magiczna"]
# talenty3 = ["Błyskotliwość", "Zimna Krew"]


wzrost = [95, 2]
im_m = ["Ferdinand (Fred)", "Heironymus (Hiro)", "Maximilian(Max)", "Theodosius (Theo)", "Achim", "Adam", "Albert", "Albie", "Alfred", "Alton", "Asham", "Ashford", "Astin", "Axel", "Bertik", "Bertrad", "Blasco", "Bredon", "Burgis", "Burke", "Carruthers", "Carl", "Chibald", "Cibber", "Cottington", "Dekker", "Dobb", "Drayton", "Dugal", "Dyer", "Edgar", "Eldren", "Ellyot", "Eucken", "Fashi", "Fenton", "Fenwark", "Gascoyn", "Gues", "Googe", "Gosson", "Hesselwhite", "Hobb", "Hobbin", "Hodkin", "Hoiquiss", "Hugo", "Jacob", "Jaq", "Jenkin", "Joop", "Joost", "Kelsoe", "Kemble", "Kent", "Linton", "Lodge", "Lollard", "Ludo", "Ludwedge", "Lynwerd", "Map", "Marlow", "Marston", "Martobee", "Max", "Mendel", "Merrick", "Merridee", "Moss", "Murr", "Nashe", "Niklaus", "Niles", "Nivers", "Norbe", "Nython", "Orlane", "Oscar", "Otem", "Parse", "Paul", "Pence", "Penge", "Plunkett", "Pomme", "Pons", "Poole", "Quillan", "Quince", "Quinn", "Ralf", "Reene", "Reeve", "Reswald", "Rudi", "Ruskin", "Seldon", "Sime", "Spence", "Syler", "Talbot", "Tananger", "Taqi", "Tarquin", "Tasse", "Taum", "Tavi", "Tew", "Thame", "Theo", "Thomas", "Thorne", "Tibbs", "Tichbourne", "Tillyard", "Tobus", "Tolquist", "Tuck", "Tyldan", "Tyman", "Tyndal", "Udo", "Valens", "Vaughn", "Vicars", "Victor", "Wade", "Walter", "Warwyck", "Wat", "Watters", "Wim", "Wyatt"]
im_z = ["Antoniella (Anni)", "Esmerelda(Esme)", "Thomasina (Tina)", "Rosalinda(Rosa)", "Agnes", "Alice", "Amabelle", "Barthony", "Beasley", "Beaswell", "Bree", "Briley", "Canty", "Crowley", "Cubbardy", "Dee", "Dendy", "Dudney", "Dunleary", "Elena", "Eva", "Frida", "Gentry", "Greta", "Hanna", "Heidi", "Hilda", "Hoby", "Janna", "Karin", "Ketta", "Lane", "Leese", "Leni", "Lidda", "Linshey", "Lyly", "Maere", "Marie", "Misha", "Mosely", "Petra", "Quettery", "Silma", "Sophia", "Susi", "Tarby", "Tella", "Theda", "Tilbury", "Tish", "Ulla", "Wanda"]

nazwisko = ["Ashfield", "Brandysnap", "Hayfoot", "Rumster", "Shortbottom", "Thorncobble", "Haleberry", "Greenhill", "Furfoot", "Greendale", "Warmfeet", "Brandysnap "]

rand_im = random.randint(0,(len(im_m))- 1)
rand_iz = random.randint(0, (len(im_z))-1)
rand_naz = random.randint(0,(len(nazwisko))-1)

imiex_m = im_m[rand_im] + " " + nazwisko[rand_naz]
imiex_z = im_z[rand_iz] + " " + nazwisko[rand_naz]

wlosy = { 1: 'Biały', 2: 'Lniany', 3: 'Rudawy', 4: 'Złoty', 5: 'Złoty', 6: 'Złoty', 7: 'Kasztanowy', 8: 'Kasztanowy', 9: 'Kasztanowy', 10: 'Kasztanowy', 11: 'Rudy', 12: 'Rudy', 13: 'Musztardowy', 14: 'Musztardowy', 15: 'Musztardowy', 16: 'Musztardowy', 17: 'Migdałowy', 18: 'Czekoladowy', 19: 'Lukrecjowy'}

oczy = {1: 'Jasnoszary', 2: 'Szary', 3: 'Błękitny', 4: 'Niebieski', 5: 'Niebieski', 6: 'Niebieski', 7: 'Zielony', 8: 'Zielony', 9: 'Zielony', 10: 'Zielony', 11: 'Orzechowy', 12: 'Orzechowy', 13: 'Orzechowy', 14: 'Brązowy', 15: 'Brązowy', 16: 'Brązowy', 17: 'Miedziany', 18: 'Ciemnobrązowy', 19: 'Ciemnobrązowy'}



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

##################MIEJSCE NA INPUT DLA WYBIERALNYCH TALENTÓW
##############NIZIOŁKI NIE MAJĄ WYBIERALNYCH TALENTÓW
# zasieg = ["1", "2"]

# input_tal1 = input(f"Który talent rasowy chcesz wybrać? {talenty2[0]}-1, czy {talenty2[1]}-2? (1-2)  ")

# if input_tal1 in zasieg:
#     a = int(input_tal1) -1
#     talentyx.append(talenty2[a])

# if input_tal1 not in zasieg:
#     #losowanie talentów
#     los_tal1 = random.randint(0,1)

#     talentyx.append(talenty2[los_tal1])

# input_tal2 = input(f"Który talent rasowy chcesz wybrać? {talenty3[0]} - 1, czy {talenty3[1]} - 2?(1-2)  ")

# if input_tal2 in zasieg:
#     a = int(input_tal2) -1
#     talentyx.append(talenty3[a])

# if input_tal2 not in zasieg:
#     los_tal2 = random.randint(0,1)

#     talentyx.append(talenty3[los_tal2])

#print(talentyx)
########################LOSOWANIE LOSOWYCH TALENTÓW

los_tal_tab = {1: 'Atrakcyjny', 2: 'Bardzo Silny', 3: 'Błękitna Krew', 4: 'Błyskotliwość', 5: 'Charyzmatyczny', 6: 'Chodu!', 7: 'Czujny', 8: 'Czysta Dusza', 9: 'Czytanie/Pisanie', 10: 'Geniusz Arytmetyczny', 11: 'Naśladowca', 12: 'Niezwykle Odporny', 13: 'Oburęczność', 14: 'Odporny na (Dowolne Zagrożenie)', 15: 'Poliglota', 16: 'Posłuch u Zwierząt', 17: 'Silne Nogi', 18: 'Słuch Absolutny', 19: 'Strzelec Wyborowy', 20: 'Szczęście', 21: 'Szósty Zmysł', 22: 'Szybki Refleks', 23: 'Talent Artystyczny', 24: 'Tragarz', 25: 'Twardziel', 26: 'Urodzony Wojownik', 27: 'Widzenie w Ciemności', 28: 'Wyczucie Kierunku', 29: 'Wyczulony Zmysł (Dowolny)', 30: 'Wytwórca (Dowolny)', 31: 'Zimna Krew', 32: 'Zręczny'} 
los_tal1 = random.randint(1, 32)
los_tal2 = random.randint(1, 32)
pierw_tal = los_tal_tab[los_tal1]
drugi_tal = los_tal_tab[los_tal2]

talentyx.append(pierw_tal)
talentyx.append(drugi_tal)
################MIEJSCE NA INPUT WYBORU UMIEJEK

wybor_umiejek = input("Czy chcesz wybrać umiejętności rasowe?(t/n) \n")

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
    los_wlos = random.randint(1, 19)
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
    los_wlos = random.randint(1, 19)
    oczyx = oczy[los_wlos]








rasowe = Rasa(cechy, umiejkix, talentyx, wzrostx, imiex_m, imiex_z, wlosx, oczyx, profesje, punkty_przeznaczeniax, punkty_bohaterax)
