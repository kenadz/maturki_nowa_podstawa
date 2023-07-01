def liczenie(ciag_binarny):
    ilosc_jedynek = 0
    for znak in ciag_binarny:
        if znak == "1":
            ilosc_jedynek += 1

    return ilosc_jedynek

liczby = []

f = open("liczby.txt", "r")

for i in range(1000):
    linia = f.readline()
    liczby.append(linia[:-1])

f.close()
podzielne_przez_2 = 0
podzielne_przez_8 = 0
ilosc_liczb = 0
for liczba in liczby:
    if liczba.count("1") < liczba.count("0"):  # .count(x) - zlicza ilość wystąpień fragmentów x w ciągu
        ilosc_liczb += 1

    if liczba[-1] == "0":
        podzielne_przez_2 += 1

    if liczba[-3:] == "000":
        podzielne_przez_8 += 1


print(ilosc_liczb)
print(podzielne_przez_2)
print(podzielne_przez_8)
