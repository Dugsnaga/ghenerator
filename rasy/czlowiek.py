"""
Ludzie są najliczniejszą i najbardziej rozpowszechnioną cywilizowaną
rasą Starego Świata. Z powodzeniem zasiedlili każdy zakątek
kontynentu od równin Królestw Estalii aż po skute lodem
najdalsze obwody administracyjne w Kislevie, a ich rozkwit trwa
nadal. Największym i najpotężniejszym ludzkim królestwem jest
Imperium, to mozaika potężnych prowincji, pokrytych zdawałoby
się bezkresnymi lasami. W samym centrum państwa leży Reikland,
powód do dumy Imperium, a zarazem jego najbogatszy i najbardziej
kosmopolityczny region.
Wielu Reiklandczyków wierzy, że władza jest ich świętym prawem,
bo sam Sigmar, bóg patronujący Imperium, był Reiklandczykiem,
zanim setki lat temu dostąpił boskości. Jego świątynie i ołtarze są
rozsiane niemalże wszędzie, a większość Reiklandczyków to gorliwi
wyznawcy Sigmara, głoszący jego przesłanie budowania jedności
Imperium. Z tego powodu Reiklandczycy są znacznie bardziej
otwarci, przyjaźnie nastawieni i optymistyczni niż inne ludy, bo
cóż mogłoby stać się ziemi, która wydała boga na świat? Z drugiej
strony przybysze z innych krain często uznają ich za aroganckich,
apodyktycznych i nazbyt ciekawskich – słowem tych, którzy nieproszeni
wściubiają nos w nie swoje sprawy.
Oprócz wystawnego stylu życia i naturalnej skłonności do bezczelności
Reiklandczycy zasadniczo niczym nie różnią się od
reszty ludzi. Ta rasa żyje krócej niż inne, za to cechuje ich większa
werwa, wszechstronność i ambicja. Wydaje się, że ludzka natura
jest nierozerwalnie związana z działającymi niepostrzeżenie
okropieństwami Niszczycielskich Potęg, ludzie bowiem znacznie
częściej niż inne rasy wpadają w objęcia Chaosu. Nie dziwi zatem,
że wśród upadających starszych ras narasta niepokój, że gwałtowny
wzrost ludzkości może wywołać kataklizm.
"""




import random

profesje = { 1: 'Aptekarz', 2: 'Czarodziej', 3: 'Inżynier', 4: 'Kapłan', 5: 'Kapłan', 6: 'Kapłan', 7: 'Kapłan', 8: 'Kapłan', 9: 'Medyk', 10: 'Mnich', 11: 'Mnich', 12: 'Prawnik', 13: 'Uczony', 14: 'Uczony', 15: 'Agitator', 16: 'Kupiec', 17: 'Mieszczanin', 18: 'Mieszczanin', 19: 'Mieszczanin', 20: 'Rzemieślnik', 21: 'Rzemieślnik', 22: 'Strażnik', 23: 'Szczurołap', 24: 'Szczurołap', 25: 'Śledczy', 26: 'Żebrak', 27: 'Żebrak', 28: 'Artysta', 29: 'Doradca', 30: 'Namiestnik', 31: 'Poseł', 32: 'Służący', 33: 'Służący', 34: 'Służący', 35: 'Szlachcic', 36: 'Szpieg', 37: 'Zwadźca', 38: 'Chłop', 39: 'Chłop', 40: 'Chłop', 41: 'Chłop', 42: 'Chłop', 43: 'Górnik', 44: 'Guślarz', 45: 'Łowca', 46: 'Łowca', 47: 'Mistyk', 48: 'Zarządca', 49: 'Zielarz', 50: 'Zwiadowca', 51: 'Biczownik', 52: 'Biczownik', 53: 'Domokrążca', 54: 'Kuglarz', 55: 'Kuglarz', 56: 'Łowca Czarownic', 57: 'Łowca Nagród', 58: 'Posłaniec', 59: 'Strażnik Dróg', 60: 'Woźnica', 61: 'Doker', 62: 'Doker', 63: 'Flisak', 64: 'Flisak', 65: 'Flisak', 66: 'Pilot Rzeczny', 67: 'Pirat Rzeczny', 68: 'Przemytnik', 69: 'Przewoźnik', 70: 'Przewoźnik', 71: 'Strażnik Rzeczny', 72: 'Strażnik Rzeczny', 73: 'Żeglarz', 74: 'Żeglarz', 75: 'Banita', 76: 'Banita', 77: 'Banita', 78: 'Banita', 79: 'Czarownica', 80: 'Paser', 81: 'Hiena Cmentarna', 82: 'Rajfur', 83: 'Rajfur', 84: 'Rekietier', 85: 'Szarlatan', 86: 'Złodziej', 87: 'Złodziej', 88: 'Złodziej', 89: 'Gladiator', 90: 'Kapłan Bitewny', 91: 'Kawalerzysta', 92: 'Kawalerzysta', 93: 'Ochroniarz', 94: 'Ochroniarz', 95: 'Oprych', 96: 'Rycerz', 97: 'Żołnierz', 98: 'Żołnierz', 99: 'Żołnierz', 100: 'Żołnierz'}


cechy= {
    "WW" : 20,
    "US" : 20, 
    "S" : 20,
    "Wt" : 20,
    "I" : 20,
    "Zw" : 20,
    "Zr" : 20,
    "Int" : 20,
    "SW" : 20,
    "Ogd" : 20,
}

szybkosc = 4
punkty_bohatera0 = 1
punkty_przeznaczenia0 = 2
punkty_wolne = 3

umiejki= ["Broń Biała (Podstawowa)", "Broń Zasięgowa (Łuk)", "Charyzma", "Dowodzenie", "Język (bretoński)", "Język (Jałowej Krainy)", "Opanowanie", "Opieka nad Zwierzętami", "Plotkowanie", "Targowanie", "Wiedza (Reikland)", "Wycena"]

talentyx = []

talenty2 = [ " Błyskotliwość", "Charyzmatyczny"]
#talenty3 = ["Błyskotliwość", "Zimna Krew"]

####################LOSOWANIE IMION
wzrost = [150, 4]
im_m = ["Adhemar", "Anders", "Artur", "Beatrijs", "Clementia", "Detlev", "Frederich", "Gerner", "Gertraud", "Haletha", "Heinrich", "Henryk", "Karl", "Kruger", "Marieke", "Sebastien", "Talther", "Talunda", "Ulrich", "Werther", "Wilryn", "Adelbert", "Adolf", "Adolphus", "Albert", "Albrecht", "Adhelm", "Alex", "Alexei", "Alfred", "Alfricht", "Anders", "Andreas", "Anton,", "Arthur", "Axel", "Barthelm", "BengtS", "Bernhard", "Berthold", "Bogoslav", "Boris", "Bruno", "Carolus", "Karl", "Klaus", "Konrad", "Diehl", "Dieter", "Dietrich", "Eberhard,", "Eckhard", "Edgar", "Ehrhard", "Ehrmann", "Emmerich", "Erich", "Ernst", "Erwin", "Faustmann", "Felix", "Ferdinand", "Franz", "Friedrich", "Fritz", "Frederik", "Gebhard", "Georg", "Gerhard", "Gottfried", "Gotthard", "Gottlieb", "Gregor", "Gunnar", "Gunther", "Gustav", "Gustavus", "Hals", "Hannes", "Hans", "Hartwig", "Heinrich", "Heinz", "Hieronymus", "Helmut", "Hergard", "Herman", "Herpin", "Hildebrand", "HolgerS", "Hugo", "Hultz", "Humfried", "Jakob", "Joachim", "Johann", "Johannes", "Josef", "Kaspar", "Kastor", "KnnudS", "Kurt", "Lorenz", "Leonard", "Luitpold", "Ludovicus", "Ludwig", "Lukas", "Magnus", "Mannfred", "Mannricht", "Mannsfried", "Mannslieb", "Martin", "Matthias", "Maximillian", "Melched", "Moritz", "Nikolas", "Nikolaus", "OlafS", "Oskar", "Otto", "Paul", "Paulus", "Peter", "Pieter", "Quintus", "RalfS", "Randolf", "Ranelf", "Rannalt", "RolfS", "Reinald", "Reiner", "Reinhard", "Reinhold", "Reinwald", "Rudiger", "Rutger", "Rudolf", "Ruprecht", "Seiger", "Siegfried", "Sigismund", "Sigmund", "Stehmar", "Stephan", "Talecht", "Thedosius", "Theopilius", "Thomas", "Tobias", "Udo", "Uhler", "Ulfred", "Ulli", "Ulrich", "Ulrict", "Viktor", "Vorster", "Waldemar", "Walter", "Werner", "Wilhelm", "Wolf", "Wolfgang", "Wolmar"]
im_z = ["Erika", "Frauke", "Helga", "Irmina", "Jehanne", "Lorelay", "Ulrika", "Willelma", "Sigfreda", "Willelma", " Maria", "Emma", "Emilia", "Mia", "Anna", "Hanna", "Johanna", "Agnes", "Agnetha", "Alexa", "Alfrida", "Alice", "Amalie", "Andrea", "Anika", "Anna", "AstridS", "Barbara", "Beatrix", "Bertha", "Bianka", "Birgit", "Bogoslava", "Brigitte", "Brita", "Brunhild", "Charlotte", "Carina", "Carmilla", "Claudia", "Dagmar", "Elena", "Elfrida", "Elisabeth", "Elsa", "Emmanuelle", "Emilie", "Erika", "Esther", "Etelka", "Eva", "Franziska", "Gabrielle", "Gerda", "Gertrud", "Gilda", "Greta", "Gretel", "Gretchen", "Hanna", "Hannath", "Hedwig", "Heidi", "Helena", "Hilda", "Hildegard", "Hunni", "Ilsa", "Ilse", "Inga", "IngridS", "Irene", "Irina", "Isolde", "Johanna", "Janna", "Juliane", "Karelia", "Karin", "Karoline", "Katharine", "Katrina", "KristenS", "Klara", "Leonore", "Ludmilla", "Luise", "Lise", "Magdalene", "Magda", "Margaritha", "Marianne", "Marlene", "Marthe", "Marte", "Martina", "Marie", "Mathilde", "Tilda", "Natasha", "Ottilia", "Petra", "Regina", "Renata", "Renate", "Selena", "Sigismunda", "Sigrid", "Sigrun", "Sigunda", "Solma", "SolveigS", "Sophia", "Susanne", "Talima,. Thedora", "Theodosia", "Theda", "Therese", "Thylda", "Ulrica", "Ulrike", "Ulla", "Ursula", "Veronica", "Wanda", "Wertha", "Wilhemina", "Wolfhilda"]

nazwisko = ["Müller", "Schneider", "Fischer", "Weber", "Meier", "Wagner", "Bäcker", "Hofmann", "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schwarz", "Zimmermann", "Braun", "Lange", "Fuchs", "Kaiser", "König", "Krause", "Köhler", "Schuhmacher", "Schmidt", "Beinbruch", "Bendow", "Bennefeld", "Bennefeldt", "Berger", "Bergmann", "Bernecker", "Bildt", "Braun", "Breitner", "Breull", "Bruckner", "Backer", "Dessau", "Dietz", "Dreschel", "Drucker", "Dudenbostel", "Dunkelberg", "Eberhauer", "Eckhard", "Eichheim", "Engelhart", "Engelmann", "Errlich", "Faustmann", "Finck", "Flaschmann", "Fleischer", "Flick", "Fraunhofer", "Fredersdorff", "Ganghofer", "Gebiihr", "Geldrecht", "Geller", "Genscher", "Gerber", "Gesner", "Goebbels", "Goffmann", "Gruber", "Griin", "Griinberg", "Gunzenhauser", "Hackenbusch", "Haffenheim", "Haffmeister", "Hannicke", "Hardenberg", "Hartmann", "Haufmann", "Heilborn", "Heising", "Hellbach", "Herrscher", "Heschendorf", "Heuser", "Hindenburg", "Hockmann", "Hohenberg", "Holstweig", "Hostettler", "Huber", "Hubergreiber", "Hollmer", "Horbiger", "Immelmann", "Junkermann", "Jager", "Kerzer", "Kessler", "Kesselmann", "Kesselring", "Kiefern", "Kirchner", "Kleemann", "Kleist", "Kleiter", "Klipstein", "Korff", "Krause", "Kreutzmann", "Kriiger", "Kunz", "Kupfer", "Kurz", "Korbitz", "Koster", "Lepr", "Leibelt", "Lentz", "Leonhardt", "Liebeneiner", "Liebowitz", "Lindenlaub", "Lizt", "Lohrentzen", "Luchter", "Meyer", "Meinhard", "Meissen", "Merkwiirdigliebe", "Mierendorff", "Miiller", "Nordberg", "Osterwald", "Platen", "Prasch", "Prunkvoll", "Pollnitz", "Rabenfels", "Regelsberg", "Reitsmann", "Retzer", "Richsteiger", "Riedmann", "Rosenkrantz", "Rupp", "Schatzenheimer", "Schicklgruber", "Schiller", "Schimmel", "Schlichter", "Schlichtkrull", "Schmidhuber", "Schmidt", "Schmiedehammer", "Schneider", "Schroder", "Schumacher", "Schutzmann", "Schwarz", "Schwarzberg", "Schwarzkopf", "Schwensen", "Schiinzel", "Schon", "Seefeldt", "Seydlitz", "Sonnefeld", "Stadtmiiller", "Steiger", "Stein", "Steinbocka", "Steinmeyer", "Sternheimer", "Stiefel", "Streckmann", "Stiiwe", "Vespermann", "Vogel", "Voller", "Wagner", "Wassmeier", "Geissbach"]

rand_im = random.randint(0, (len(im_m))-1)
rand_iz = random.randint(0, (len(im_z))-1)
rand_naz = random.randint(0, (len(nazwisko))-1)

imiex_m = im_m[rand_im] + " " + nazwisko[rand_naz]
imiex_z = im_z[rand_iz] + " " + nazwisko[rand_naz]

wlosy = { 1: 'Biały', 2: 'Złoty blond', 3: 'Rudoblond', 4: 'Złoty', 5: 'Złoty', 6: 'Złoty', 7: 'Jasny brąz', 8: 'Jasny brąz', 9: 'Jasny brąz', 10: 'Kasztanowy', 11: 'Ciemny brąz', 12: 'Ciemny brąz', 13: 'Ciemny brąz', 14: 'Czarny', 15: 'Czarny', 16: 'Czarny', 17: 'Kasztanowy', 18: 'Rudy', 19: 'Siwy'}

oczy = {1: 'Zielony', 2: 'Błękitny', 3: 'Niebieski', 4: 'Niebieski', 5: 'Niebieski', 6: 'Blady szary', 7: 'Blady szary', 8: 'Blady szary', 9: 'Blady szary', 10: 'Szary', 11: 'Szary', 12: 'Szary', 13: 'Brązowy', 14: 'Brązowy', 15: 'Brązowy', 16: 'Orzechowy', 17: 'Ciemnobrązowy', 18: 'Czarny'}



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

    
if wybor_umiejek != "t":
    #losowanie talentów

    los_tal1 = random.randint(0,1)
    talentyx.append(talenty2[los_tal1])

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
while los_tal1 == los_tal2:
    los_tal2 = random.randint(1, 32)
los_tal3 = random.randint(1, 32)
while los_tal3 == los_tal1 or los_tal3 == los_tal2:
    los_tal3 = random.randint(1, 32)
pierw_tal = los_tal_tab[los_tal1]
drugi_tal = los_tal_tab[los_tal2]
trzeci_tal = los_tal_tab[los_tal3]
talentyx.append(pierw_tal)
talentyx.append(drugi_tal)
talentyx.append(trzeci_tal)

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
    los_wlos = random.randint(1, 18)
    oczyx = oczy[los_wlos]








rasowe = Rasa(cechy, umiejkix, talentyx, wzrostx, imiex_m, imiex_z, wlosx, oczyx, profesje, punkty_przeznaczeniax, punkty_bohaterax)
