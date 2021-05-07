import os
cls = lambda: os.system('cls')
def dodawanie():
    print('Dodawanie:')
    print('Ile liczb chcesz do siebie dodać?')
    i = int(input())
    print('Podaj pierwszą liczbę:')
    a = int(input())
    while i>1:
        print('Podaj następną liczbę:')
        a = a+int(input())
        i-=1
    def yes_or_no(a):
        print('Czy chcesz podać kolejną liczbę? Twój obecny wynik to',a, 'Wybierz t aby kontynuować, n aby wrócić do menu, lub dowolny przycisk aby opuścić kalkulator.')
        yn = str(input())
        if yn == 't' or yn == 'T':
            print('Podaj kolejną liczbę:')
            a = a+int(input())
            yes_or_no(a)
        elif yn == 'n' or yn == 'N':
            menu('nie')
        else:
            return 0
    yes_or_no(a)
def odejmowanie():
    print('Odejmowanie')
    print('Podaj odjemną:')
    a = int(input())
    print('Ile liczb chcesz odjąć?')
    i = int(input())
    k=i
    while i > 0:
        if i == k and k!=1:
            print('Podaj pierwszy odjemnik:')
        else:
            print('Podaj odjemnik:')
        a = a - int(input())
        i-=1
    def yes_or_no(a):
        print('Czy chcesz podać kolejny odjemnik? Twój obecny wynik to',a, 'Wybierz t aby kontynuować, n aby wrócić do menu, lub dowolny przycisk aby opuścić kalkulator.')
        yn = str(input())
        if yn == 't' or yn == 'T':
            print('Podaj kolejny odjemnik:')
            a = a - int(input())
            yes_or_no(a)
        elif yn == 'n' or yn == 'N':
            menu('nie')
        else:
            return 0
    yes_or_no(a)
def mnozenie():
    print('Mnozenie')
    print('Podaj pierwszą liczbę:')
    a = int(input())
    print('Ile jeszcze chcesz podać czynników?')
    i = int(input())
    k = i
    while i > 0:
        if i == k and k != 1:
            print('Podaj pierwszy czynnik:')
        else:
            print('Podaj czynnik:')
        a = a * int(input())
        i -= 1
    def yes_or_no(a):
        print('Czy chcesz podać kolejny czynnik? Twój obecny wynik to',a, 'Wybierz t aby kontynuować, n aby wrócić do menu, lub dowolny przycisk aby opuścić kalkulator.')
        yn = str(input())
        if yn == 't' or yn == 'T':
            print('Podaj kolejny czynnik:')
            a = a * int(input())
            yes_or_no(a)
        elif yn == 'n' or yn == 'N':
            menu('nie')
        else:
            return 0
    yes_or_no(a)
def dzielenie():
    print('Dzielenie')
    print('Podaj dzielną:')
    a = int(input())
    print('Podaj dzielnik:')
    a = a / int(input())
    def yes_or_no(a):
        print('Czy chcesz podać kolejny dzielnik? Twój obecny wynik to', a, 'Wybierz t aby kontynuować, n aby wrócić do menu, lub dowolny przycisk aby opuścić kalkulator.')
        yn = str(input())
        if yn == 't' or yn == 'T':
            print('Podaj kolejny dzielnik:')
            a = a / int(input())
            yes_or_no(a)
        elif yn == 'n' or yn == 'N':
            menu('nie')
        else:
            return 0
    yes_or_no(a)
def menu(k):
    cls()
    if k == 'tak':
        print('Niepoprawna akcja')
    print('Wybierz akcję: 1. Dodawanie 2. Odejmowanie 3. Mnożenie 4. Dzielenie 5. Wyjdź')
    x = input()
    if x=='1':
        dodawanie()
    elif x=='2':
        odejmowanie()
    elif x=='3':
        mnozenie()
    elif x=='4':
        dzielenie()
    elif x=='5':
        return 0
    else:
        blad = 'tak'
        menu(blad)
menu('nie')