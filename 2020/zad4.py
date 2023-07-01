def czy_pierwsza(n):
    if n < 2:
        return False
    for dzielnik in range(2, n//2 + 1):
        if n % dzielnik == 0:
            return False
    return True

def najdl_spojny_fragment(wyraz):
    litera_najdl = wyraz[0]
    dl_najdl = 1
    litera_badanego = wyraz[0]
    dl_badanego = 1
    for i in range(1, len(wyraz)):
        if wyraz[i] == litera_badanego:
            dl_badanego += 1
            if dl_badanego > dl_najdl:
                dl_najdl = dl_badanego
                litera_najdl = litera_badanego
        else:
            litera_badanego = wyraz[i]
            dl_badanego = 1

    return litera_najdl * dl_najdl

# funkcja do 4.3
# p1 - para pierwsza
# p2 - para druga
# zwaraca -1, gdy pierwsza para jest większa
# zwraca 0, gdy pary są równe
# zwraca 1, gdy druga para jest większa
def porownanie(p1, p2):
    if p1[0] > p2[0]:
        return -1
    elif p2[0] > p1[0]:
        return 1
    else:
        for i in range(len(p1[1])):
            if p1[1][i] != p2[1][i]:
                if p1[1][i] > p2[1][i]:
                    return -1
                else:
                    return 1
    return 0

f = open('pary.txt', 'r')
pary = []
for i in range(100):
    wiersz = f.readline()
    wiersz = wiersz.split(" ")
    wiersz[0] = int(wiersz[0])
    wiersz[1] = wiersz[1][:-1]
    pary.append(wiersz)
f.close()

goldbach = [] # jedna z liczb pierwszych w parze sumy
najluzsze_fragmenty = []


najm_para = [100, ""]

for para in pary:
    # zad 1
    if para[0] % 2 == 0 and para[0] > 4:
        for p in range(3, para[0]//2):
            if czy_pierwsza(p) and czy_pierwsza(para[0] - p):
                goldbach.append([para[0], p, para[0] - p])
                break
    # zad 2
    najluzsze_fragmenty.append(najdl_spojny_fragment(para[1]))

    # zad 3
    if para[0] == len(para[1]):
        if porownanie(najm_para, para) == -1:
            najm_para = para

f = open('wyniki4.txt','w')
f.write(f'4.1 \n')
for trojka in goldbach:
    f.write(f"{trojka[0]} ")
    f.write(f"{trojka[1]} ")
    f.write(f"{trojka[2]}\n")
f.write(f'4.2 \n')
for najdluzsze_frag in najluzsze_fragmenty:
    f.write(f'{najdluzsze_frag} {len(najdluzsze_frag)}\n')
f.write(f'4.3 {najm_para[0]} {najm_para[1]}')

f.close()
