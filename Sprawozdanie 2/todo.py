import pickle
import os
cls = lambda: os.system('cls')
terminy = []
nazwyzad = []
terminr = 0
terminm = 0
termind = 0
u = 0
cel = 0
ed = 0
try:
    nazwyzad = pickle.load(open('nazwyzad.dat', 'rb'))
except:
    pickle.dump(nazwyzad, open('nazwyzad.dat', 'wb'))
try:
    terminy = pickle.load(open('terminy.dat', 'rb'))
except:
    pickle.dump(terminy, open('terminy.dat', 'wb'))
def nowezadanie():
    print('Dodawanie zadania')
    print('Podaj nazwę zadania:')
    nazwazad = input()
    nazwyzad.append(nazwazad)
    print('Podaj termin wykonania:')
    print('Rok:')
    global terminr
    global terminm
    global termind
    def checker():
        global terminr
        terminr = int(input())
        if terminr<2021:
            print('Podaj poprawny rok')
            checker()
    checker()
    print('Miesiąc (liczba):')
    def checker():
        global terminm
        terminm = int(input())
        if terminm<1 or terminm>12:
            print('Podaj poprawny miesiąc')
            checker()
    checker()
    print('Dzień:')
    def checker():
        global termind
        global terminm
        global terminr
        termind = int(input())
        '''boże mój...'''
        if terminm == 1 or terminm == 3 or terminm == 5 or terminm == 7 or terminm == 8 or terminm == 10 or terminm == 12:
            if termind < 1 or termind >31:
                print('Podaj poprawny dzień')
                checker()
        elif terminm == 2:
            if termind < 1 or termind > 29 or termind > 28 and terminr %4 != 0:
                print('Podaj poprawny dzień')
                checker()
        else:
            if termind < 1 or termind > 30:
                print('Podaj poprawny dzień')
                checker()
    checker()
    terminr = str(terminr)
    terminm = str(terminm)
    termind = str(termind)
    termin = termind+'.'+terminm+'.'+terminr
    terminy.append(termin)
    pickle.dump(nazwyzad, open('nazwyzad.dat', 'wb'))
    pickle.dump(terminy, open('terminy.dat', 'wb'))
    menu('nie')
def edycjazadania():
    print('Edycja zadania:')
    global terminy
    global ed
    global cel
    global nazwyzad
    i = 0
    for i in range(0, len(nazwyzad)):
        print(i+1, nazwyzad[i], 'Termin:', terminy[i])
    print('Podaj cel (numer zadania):')
    def checker():
        global cel
        cel = int(input())
        if cel < 1 or cel > len(nazwyzad)+1:
            print('Podaj poprawny cel')
            checker()
        else:
            print('1. Edycja nazwy zadania 2. Edycja terminu zadania')
            checker2()
    def edzad():
        global cel
        global nazwyzad
        print('Podaj nową nazwę zadania:')
        tempnazw = input()
        nazwyzad[cel-1] = tempnazw
    def edterm():
        print('Podaj nowy termin:')
        print('Rok:')
        global terminy
        global terminr
        global terminm
        global termind
        def checker():
            global terminr
            terminr = int(input())
            if terminr < 2021:
                print('Podaj poprawny rok')
                checker()
        checker()
        print('Miesiąc (liczba):')
        def checker():
            global terminm
            terminm = int(input())
            if terminm < 1 or terminm > 12:
                print('Podaj poprawny miesiąc')
                checker()
        checker()
        print('Dzień:')
        def checker():
            global termind
            global terminm
            global terminr
            termind = int(input())
            '''boże mój... Ponownie!'''
            if terminm == 1 or terminm == 3 or terminm == 5 or terminm == 7 or terminm == 8 or terminm == 10 or terminm == 12:
                if termind < 1 or termind > 31:
                    print('Podaj poprawny dzień')
                    checker()
            elif terminm == 2:
                if termind < 1 or termind > 29 or termind > 28 and terminr % 4 != 0:
                    print('Podaj poprawny dzień')
                    checker()
            else:
                if termind < 1 or termind > 30:
                    print('Podaj poprawny dzień')
                    checker()
        checker()
        terminr = str(terminr)
        terminm = str(terminm)
        termind = str(termind)
        termin = termind + '.' + terminm + '.' + terminr
        terminy[cel-1] = termin
    def checker2():
        global ed
        ed = input()
        if ed == '1':
            edzad()
        elif ed == '2':
            edterm()
        else:
            print('Podaj poprawną akcję')
            checker2()
    checker()
    pickle.dump(nazwyzad, open('nazwyzad.dat', 'wb'))
    pickle.dump(terminy, open('terminy.dat', 'wb'))
    menu('nie')
def usunieciezadania():
    print('Usuwanie zadania:')
    i = 0
    for i in range(0, len(nazwyzad)):
        print(i+1, nazwyzad[i], 'Termin:', terminy[i])
    print('Wybierz cel:')
    global u
    u = 0
    def check():
        global u
        u = int(input())
        if u < 1 or u > len(nazwyzad):
            print('Podaj poprawny cel:')
            check()
    check()
    del nazwyzad[u-1]
    del terminy[u-1]
    pickle.dump(nazwyzad, open('nazwyzad.dat', 'wb'))
    pickle.dump(terminy, open('terminy.dat', 'wb'))
    menu('nie')
def wypiszzadania():
    print('Twoje zadania:')
    i = 0
    for i in range (0, len(nazwyzad)):
        print(i+1, nazwyzad[i], 'Termin:', terminy[i])
    dupmvariable = input()
    menu('nie')
def menu(blad):
    cls()
    if blad == 'tak':
        print('Niepoprawna akcja')
    print('Wybierz akcję: 1.Dodaj zadanie 2.Edytuj istniejące zadanie 3.Usuń zadanie 4.Wypisz zadania 5.Wyjdź')
    x = input()
    if x == '1':
        nowezadanie()
    elif x == '2':
        edycjazadania()
    elif x == '3':
        usunieciezadania()
    elif x == '4':
        wypiszzadania()
    elif x == '5':
        return 0
    else:
        blad = 'tak'
        menu(blad)
menu('nie')