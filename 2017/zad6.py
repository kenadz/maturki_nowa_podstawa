f = open('dane.txt', 'r')

lista = []
for i in range(200):
    wiersz = f.readline()
    wiersz = wiersz.split(" ")
    wiersz = list(map(int, wiersz))
    # for j in range(len(wiersz)):
    #    wiersz[j] = int(wiersz[j])
    lista.append(wiersz)

f.close()

najjasniejszy = 0
najciemniejszy = 255

ilosc_wierszy = 0
# zad 1
for wiersz in lista:
    for pixel in wiersz:
        if pixel > najjasniejszy:
            najjasniejszy = pixel
        if pixel < najciemniejszy:
            najciemniejszy = pixel
    # zad 2
    lewa = wiersz[0:160]
    prawa = wiersz[319:159:-1]
    if lewa != prawa:
        ilosc_wierszy += 1

# zad 3

kontrastujace = 0

for y in range(200):
    for x in range(320):
        if x > 0 and abs(lista[y][x] - lista[y][x - 1]) > 128: # w lewo
            kontrastujace += 1
            continue
        if x < 319 and abs(lista[y][x] - lista[y][x + 1]) > 128: # w prawo
            kontrastujace += 1
            continue
        if y > 0 and abs(lista[y][x] - lista[y - 1][x]) > 128: # w górę
            kontrastujace += 1
            continue
        if y < 199 and abs(lista[y][x] - lista[y + 1][x]) > 128: # w dół
            kontrastujace += 1
            continue


# zad 4

dl_najdl = 0

for x in range(320):
    dl_badanego = 0
    wartosc_pixela = -1
    for y in range(200):
        if lista[y][x] == wartosc_pixela:
            dl_badanego += 1
            if dl_badanego > dl_najdl:
                dl_najdl = dl_badanego
        else:
            wartosc_pixela = lista[y][x]
            dl_badanego = 1

f = open('wyniki6.txt', 'w')
f.write('zad 6.1\n')
f.write(f'najjaśnieszy {najjasniejszy} \n')
f.write(f'najciemniejszy {najciemniejszy} \n')
f.write(f'zad 6.2 ilosc {ilosc_wierszy}\n')
f.write(f'zad 6.3 {kontrastujace}\n')
f.write(f'zad 6.4 {dl_najdl}\n')
f.close()