from math import *

# 5! = 1*2*3*4*5
def silnia(liczba):
    i = 1
    wynik = 1
    while i <= liczba:
        wynik *= i
        i += 1
    return wynik

def suma_silni_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += silnia(liczba % 10)
        liczba //= 10
    return suma

def czy_potega_3(liczba):
    i = 1
    while i < liczba:
        i *= 3
    if liczba == i:
        return True
    else:
        return False

def NWD(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c

    return a


print(suma_silni_cyfr(343))



f = open('liczby.txt', 'r')

lista = list(map(int, f.readlines()))

#for liczby in range(500):
#    lista.append(int(f.readline()))

f.close()

liczby_suma_silni = []
potegi_3 = 0

# zad 1
for liczba in lista:
    if czy_potega_3(liczba):
        potegi_3 += 1
# zad 2
    if suma_silni_cyfr(liczba) == liczba:
        liczby_suma_silni.append(liczba)

# zad 3
dl_najdl_ciagu = 0
poczatek_najdl_ciagu = 0
nwd_najdl_ciagu = 0

for i in range(len(lista)):
    dl_badanego_ciagu = 1
    poczatek_badanego_ciagu = i
    nwd_badanego_ciagu = lista[i]
    for j in range(i + 1, len(lista)):
        nwd_badanego_ciagu = NWD(nwd_badanego_ciagu, lista[j])
        dl_badanego_ciagu += 1
        if nwd_badanego_ciagu > 1:
            if dl_badanego_ciagu > dl_najdl_ciagu:
                dl_najdl_ciagu = dl_badanego_ciagu
                nwd_najdl_ciagu = nwd_badanego_ciagu
                poczatek_najdl_ciagu = poczatek_badanego_ciagu
        else:
            break

f = open('wynik4.txt', 'w', )
f.write(f'zad 4.1 {potegi_3}\n')
f.write(f'zad 4.2\n')
for liczba in liczby_suma_silni:
    f.write(str(liczba) + "\n")
f.write(f'zad 4.3\n')
f.write(f'pierwsza liczba ciągu {lista[poczatek_najdl_ciagu]}\n')
f.write(f'długość ciągu {dl_najdl_ciagu}\n')
f.write(f'nwd ciągu {nwd_najdl_ciagu}\n')
f.close()




