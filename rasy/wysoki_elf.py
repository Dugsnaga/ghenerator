"""
Widok wysokich elfów na reiklandzkich rzekach jest dość powszechny.
Zarówno Altdorf, jak i Nuln mogą pochwalić się całkiem sporymi
dzielnicami zamieszkanymi przez wysokie elfy. Większość mieszkańców
to kupcy spławiający towary w dół Reiku przez Marienburg aż do
morza. Elficcy kupcy to, obok korpusów dyplomatycznych i ich świt,
najliczniejsi spośród wysokich elfów spotykanych w Reiklandzie Dla
ludzi są powściągliwi, obcy i długowieczni. To pełen pasji, emocjonalny
lud, w Reiklandzie powszechnie uważany za najpiękniejszą rasę w Starym
Świecie, a zarazem najbardziej arogancką.
Są wysokie i szczupłe, a ich uszy są lekko spiczaste. Większość z nich
ma długie, piękne włosy i melodyjne głosy. Chociaż wyglądają na
wątłe, są nie tylko zaskakująco silne, lecz także niezwykle zręczne
i zwinne. Między elfami i elfkami trudno dostrzec różnice w wyglądzie,
co nierzadko prowadzi do nieporozumień w kontaktach
z ludźmi.
Wysokie elfy, które same siebie nazywają „Asur”, pochodzą z Ulthuanu,
magicznej wyspy leżącej gdzieś na zachód od Starego Świata.
Są dumną rasą, chlubią się tym, że są pośród najstarszych cywilizowanych
ras na świecie. Wysokie elfy darzą krasnoludów dużą
dozą pogardy, ponieważ dzieli ich długa historię wojen i konfliktów.
Odkąd opuściły Stary Świat w wyniku Wojny o Brodę, Asurowie
są rozdarci wojną domową – „waśnią w rodzinie”, jak o niej mówią
– chociaż nie jest to sprawa, o której otwarcie rozmawialiby z obcymi.
Wskutek zmagań trwających od milleniów, elfy ze zniszczonej
wojną północy Ulthuanu powoli stają się niewzruszone, praktyczne
i bezwzględne.
Społeczeństwo wysokich elfów przywiązuje wielką wagę do rytuałów
i dyscypliny, co ma na celu utrzymanie gwałtownych emocji na wodzy
i zapewnia ich złożonym umysłom ostrość myślenia. Choć wydaje się
to sprzeczne z tym, co powiedziano powyżej, niejeden Asur czując zew
przygody podąża za nim bez chwili wahania. Termin „morski elf” jest
często używany przez inne rasy do określania nieustraszonych wysokich
elfów, które wypływają poza bezpieczne wody Ulthuanu i zostają żeglarzami,
handlarzami i dyplomatami. Zdecydowanie różnią się od reszty
towarzyszących im ponurych Asurów, zazwyczaj wiodących życie wojownika.

"""

import random

profesje = {1: 'Aptekarz', 2: 'Aptekarz', 3: 'Czarodziej', 4: 'Czarodziej', 5: 'Czarodziej', 6: 'Czarodziej', 7: 'Medyk', 8: 'Medyk', 9: 'Prawnik', 10: 'Prawnik', 11: 'Prawnik', 12: 'Prawnik', 13: 'Uczony', 14: 'Uczony', 15: 'Uczony', 16: 'Uczony', 17: 'Kupiec', 18: 'Kupiec', 19: 'Kupiec', 20: 'Kupiec', 21: 'Kupiec', 22: 'Mieszczanin', 23: 'Mieszczanin', 24: 'Rzemieślnik', 25: 'Rzemieślnik', 26: 'Rzemieślnik', 27: 'Strażnik', 28: 'Śledczy', 29: 'Śledczy', 30: 'Artysta', 31: 'Doradca', 32: 'Doradca', 33: 'Namiestnik', 34: 'Namiestnik', 35: 'Poseł', 36: 'Poseł', 37: 'Poseł', 38: 'Szlachcic', 39: 'Szlachcic', 40: 'Szlachcic', 41: 'Szpieg', 42: 'Szpieg', 43: 'Szpieg', 44: 'Zwadźca', 45: 'Zwadźca', 46: 'Łowca', 47: 'Łowca', 48: 'Łowca', 49: 'Zielarz', 50: 'Zielarz', 51: 'Zwiadowca', 52: 'Zwiadowca', 53: 'Zwiadowca', 54: 'Zwiadowca', 55: 'Zwiadowca', 56: 'Zwiadowca', 57: 'Kuglarz', 58: 'Kuglarz', 59: 'Kuglarz', 60: 'Łowca Nagród', 61: 'Łowca Nagród', 62: 'Łowca Nagród', 63: 'Posłaniec', 64: 'Przemytnik', 65: 'Przewoźnik', 66: 'Żeglarz', 67: 'Żeglarz', 68: 'Żeglarz', 69: 'Żeglarz', 70: 'Żeglarz', 71: 'Żeglarz', 72: 'Żeglarz', 73: 'Żeglarz', 74: 'Żeglarz', 75: 'Żeglarz', 76: 'Żeglarz', 77: 'Żeglarz', 78: 'Żeglarz', 79: 'Żeglarz', 80: 'Żeglarz', 81: 'Banita', 82: 'Banita', 83: 'Banita', 84: 'Rajfur', 85: 'Rajfur', 86: 'Szarlatan', 87: 'Szarlatan', 88: 'Szarlatan', 89: 'Gladiator', 90: 'Gladiator', 91: 'Kawalerzysta', 92: 'Kawalerzysta', 93: 'Kawalerzysta', 94: 'Kawalerzysta', 95: 'Ochroniarz', 96: 'Ochroniarz', 97: 'Oprych', 98: 'Rycerz', 99: 'Żołnierz', 100: 'Żołnierz'}


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

umiejki= ["Broń Biała (Podstawowa)", "Broń Zasięgowa (Łuk)", "Dowodzenie", "Język (Eltharin)", "Muzyka(Dowolny instrument)", "Nawigacja", "Opanowanie", "Pływanie", "Percepcja", "Wycena", "Występy (Śpiewanie)", "Żeglarstwo"]

talentyx = ["Czytanie/Pisanie", "Wyczulony Zmysł (Wzrok)", "Widzenie w Ciemności"]

talenty2 = [ "Szósty Zmysł", "Percepcja Magiczna"]
talenty3 = ["Błyskotliwość", "Zimna Krew"]


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

imiona3 = {1: 'andril', 2: 'anel', 3: 'ellion', 4: 'fin', 5: 'il', 6: 'irian', 7: 'mor', 8: 'nil', 9: 'ric', 10: 'wing'}

wlosy = { 1: 'Srebrnosiwy', 2: 'Popielaty', 3: 'Jasny blond', 4: 'Miodowoblond', 5: 'Miodowoblond', 6: 'Miodowoblond', 7: 'Żółty', 8: 'Żółty', 9: 'Żółty', 10: 'Żółty', 11: 'Miedziany blond', 12: 'Miedziany blond', 13: 'Miedziany blond', 14: 'Blond', 15: 'Blond', 16: 'Blond', 17: 'Migdałowy', 18: 'Czerwony', 19: 'Czarny'}

oczy = {1: 'Czarny jak smoła', 2: 'Ametystowy', 3: 'Akwamaryna', 4: 'Szafirowy', 5: 'Szafirowy', 6: 'Szafirowy', 7: 'Turkusowy', 8: 'Turkusowy', 9: 'Turkusowy', 10: 'Turkusowy', 11: 'Szmaragdowy', 12: 'Szmaragdowy', 13: 'Szmaragdowy', 14: 'Bursztynowy', 15: 'Bursztynowy', 16: 'Bursztynowy', 17: 'Miedziany', 18: 'Cytrynowożółty', 19: 'Złoty'}



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
