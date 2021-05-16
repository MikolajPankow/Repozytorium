import os
import requests
from bs4 import BeautifulSoup
cls = lambda: os.system('cls')
def kurseuro():
    result = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=PLN&To=EUR")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    kurs = soup.find_all(attrs={'class': 'unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx'})
    wymiana = 0
    for krs in kurs:
        wymiana = krs.text.split()
    print(wymiana[0],wymiana[1],wymiana[2],wymiana[3],wymiana[4])
    menu('nie')
def kursdolara():
    result = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=PLN&To=USD")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    kurs = soup.find_all(attrs={'class': 'unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx'})
    wymiana = 0
    for krs in kurs:
        wymiana = krs.text.split()
    print(wymiana[0], wymiana[1], wymiana[2], wymiana[3], wymiana[4])
    menu('nie')
def kursfranka():
    result = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=PLN&To=CHF")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    kurs = soup.find_all(attrs={'class': 'unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx'})
    wymiana = 0
    for krs in kurs:
        wymiana = krs.text.split()
    print(wymiana[0], wymiana[1], wymiana[2], wymiana[3], wymiana[4])
    menu('nie')
def kursyuana():
    result = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=PLN&To=CNY")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    kurs = soup.find_all(attrs={'class': 'unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx'})
    wymiana = 0
    for krs in kurs:
        wymiana = krs.text.split()
    print(wymiana[0], wymiana[1], wymiana[2], wymiana[3], wymiana[4])
    menu('nie')
def menu(blad):
    cls()
    print('Kurs złotego na: 1. Euro 2. Dolar Amerykański 3. Frank Szwajcarski 4. Yuan 5. Wyjdź')
    if blad == 'tak':
        print('Niepoprawna akcja')
    x = input()
    if x=='1':
        kurseuro()
    elif x=='2':
        kursdolara()
    elif x=='3':
        kursfranka()
    elif x=='4':
        kursyuana()
    elif x=='5':
        return 0
    else:
        blad = 'tak'
        menu(blad)
menu('nie')