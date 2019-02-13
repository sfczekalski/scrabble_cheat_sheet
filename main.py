ALFABET = {
    'a': 1,
    'e': 1,
    'i': 1,
    'n': 1,
    'o': 1,
    'r': 1,
    's': 1,
    'w': 1,
    'z': 1,

    'c': 2,
    'd': 2,
    'k': 2,
    'l': 2,
    'm': 2,
    'p': 2,
    't': 2,
    'y': 2,

    'b': 3,
    'g': 3,
    'h': 3,
    'j': 3,
    'ł': 3,
    'u': 3,

    'ą': 5,
    'ę': 5,
    'f': 5,
    'ó': 5,
    'ś': 5,
    'ż': 5,

    'ć': 6,

    'ń': 7,

    'ź': 9
}

WOREK = ['a','a','a','a','a','a','a','a','a','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i',
         'n','n','n','n','n','o','o','o','o','o','o', 'r','r','r','r','s','s','s','s','w','w','w','w','z','z','z','z','z',
          'c','c','c','d','d','d','k','k','k','l','l','l','m','m','m','p','p','p','t','t','t','y','y','y','y',
          'b','b','g','g','h','h','j','j','ł','ł','u','u','ą','ę','f','ó','ś','ż','ć','ź','ń'
        ]

def parse_file():
    wszystkie = []
    with open('/home/stas/PycharmProjects/scrabble/slownik/sjp-odm-20190110/odm.txt') as fp:
        for line in fp:
            line = fp.readline()
            splitted = line.split(',')
            for s in splitted:
                wszystkie.append(s.splitlines()[0].lower())

    return wszystkie

import random
def losuj(n):
    #losuj n liter
    wylosowane = []
    for i in range(n):
        wylosowane.append(random.choice(WOREK))

    print('Wylosowałem następujące litery:')
    print(wylosowane)
    return wylosowane


def sprawdz_wartosc(litera):
    return ALFABET[litera]


def wybierz_najlepsze(mozliwosci):
    najlepsze = mozliwosci[0]

    #oblicz wartosci
    wartosci = []
    for slowo in mozliwosci:
        wartosc = 0
        for litera in slowo:
            wartosc += sprawdz_wartosc(litera)
        wartosci.append(wartosc)

    #sprawdz ktore slowo ma najwyzsza wartosc
    najwyzsza = wartosci[0]
    for wart in wartosci:
        if wart > najwyzsza:
            najwyzsza = wart

    #zwroc slowo ktorego wartosc jest najwyzsza
    najlepsze = mozliwosci[wartosci.index(najwyzsza)]
    return najlepsze, najwyzsza


def mozliwosci(litery, SLOWNIK):
    from itertools import permutations
    perms = [''.join(j) for i in range(1, len(litery) + 1) for j in permutations(litery, i)]
    poprawne = []
    for s in perms:
        if s in SLOWNIK:
            poprawne.append(s)
            #print(s)
    return poprawne


def wygeneruj_slowo(litery, SLOWNIK):
    mozliwe = mozliwosci(litery, SLOWNIK)
    #print('Mogę ułożyć następujące słowa: ')
    #print(mozliwosci)
    najlepsze, punkty = wybierz_najlepsze(mozliwe)
    print('Wybralem slowo: {} gdyż uzyskam za nie najwięcej punktów, to jest {} '.format(najlepsze,punkty))
    return najlepsze, punkty


def przygotuj_slownik():
    SLOWNIK = set(parse_file())
    return SLOWNIK

def dobierz_litery(liczba):
    #in case there is no enough letters in WOREK
    if len(WOREK) < liczba:
        liczba = len(WOREK)

    # get letters from the user.
    print('Wprowadź swoje litery:')
    wyjscie = [x for x in input().split()[:liczba]]

    return wyjscie


def operate():
    SLOWNIK = przygotuj_slownik()
    #litery = dobierz_litery(7)
    litery = losuj(7)
    wygeneruj_slowo(litery, SLOWNIK)

operate()
