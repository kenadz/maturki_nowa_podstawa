def rozne_litery(wyraz):
    unikalne = []

    for znak in wyraz:
        if znak not in unikalne:
            unikalne.append(znak)
    return len(unikalne)

def rozne_litery2(wyraz):
    wystapienia = []
    for i in range(26):
        wystapienia.append(0)

    # 0 .. 25
    # wystapienia[0] = 0, wystapienia[1] = 0,...
    # 0 - A
    # 1 - B
    # 2 - C
    # 25 - Z

    for znak in wyraz:
        wystapienia[ord(znak) - ord('A')] += 1

    ilosc = 0
    for liczba in wystapienia:
        if liczba > 0:
            ilosc += 1

    return ilosc

def rozne_litery3(wyraz):
    return len(set(wyraz))

def roznica_liter(wyraz):
    return ord(max(wyraz)) - ord(min(wyraz))

f = open("sygnaly.txt", "r")

#lista = [x[:-1] for x in f.readlines()]

lista = []


for i in range(1000):
    lista.append(f.readline()[:-1])

f.close()

przeslanie = ''
roznica_10 = []

for sygnal in lista[39::40]:
    #print(sygnal)
    przeslanie += sygnal[9]

slowo_rozne_litery = ""
for sygnal in lista:
    if rozne_litery(sygnal) > rozne_litery(slowo_rozne_litery):
        slowo_rozne_litery = sygnal

    if roznica_liter(sygnal) <= 10:
        roznica_10.append(sygnal)

f = open("wyniki4.txt", 'w')

f.write(f'4.1 {przeslanie}\n')
f.write(f'4.2 {slowo_rozne_litery} {rozne_litery(slowo_rozne_litery)}\n')
f.write('4.3\n')
#for wyraz in roznica_10:
#    f.write(f'{wyraz}\n')
f.write("\n".join(roznica_10))

f.close()