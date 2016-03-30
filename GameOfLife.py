#On Mika's idea coded by Kalle Saarela
import copy
import random

leveys = 40
korkeus = 40
matriisi = [[0 for i in range(leveys)] for j in range(korkeus)]
matriisi_uusi = copy.deepcopy(matriisi)

def alusta_matriisi():
    for x in range(leveys):
        for y in range(korkeus):
            matriisi[x][y] = random.randint(0, 1)

def tulosta_matriisi():
    for x in range(leveys):
        for y in range(korkeus):
            print matriisi[x][y],
        print
    print

def laske_naapurit(x, y):
    naapurit = 0
    for xx in range(x-1, x+2):
        for yy in range(y-1, y+2):
            if xx < 0 or yy < 0 or xx > leveys-1 or yy > korkeus-1 or x == xx and y == yy:
                continue
            if matriisi[xx][yy] == 1:
                naapurit += 1
    return naapurit

def laske_kierros():
    for x in range(leveys):
        for y in range(korkeus):
            naapurit = laske_naapurit(x, y)
            
            if matriisi[x][y] == 1:
                if naapurit < 2 or naapurit > 3:
                    matriisi_uusi[x][y] = 0
            else:
                if naapurit == 3:
                    matriisi_uusi[x][y] = 1

alusta_matriisi()
for i in range(40):
    tulosta_matriisi()
    laske_kierros()
    matriisi = copy.deepcopy(matriisi_uusi)
