
import copy
import json

def prazno_polje(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def ustrezno(sudoku, n, pozicija):
    vrstica, stolpec = pozicija
    
    #vrstica
    for j in range(len(sudoku[0])):
        if sudoku[vrstica][j] == n and j != stolpec:
            return False
    
    #stolpec
    for i in range(len(sudoku)):
        if sudoku[i][stolpec] == n and i != vrstica:
            return False
    
    #kvadrat
    smv = 3 * (vrstica // 3)      #spodnja meja vrstice
    zmv = smv + 3
    sms = 3 * (stolpec // 3)
    zms = sms + 3

    for i in range(smv, zmv):
        for j in range(sms, zms):
            if sudoku[i][j] == n and (i, j) != pozicija:
                return False
    return True


def reševanje(sudoku):
    if not prazno_polje(sudoku):
        return True
    polje = prazno_polje(sudoku)
    vrstica, stolpec = polje

    for n in range(1, 10):
        if ustrezno(sudoku, n, polje):
            sudoku[vrstica][stolpec] = n
            
            if reševanje(sudoku):
                return True
            sudoku[polje[0]][polje[1]] = 0
            
    return False 

def rešitev(sudoku):
    reš = copy.deepcopy(sudoku)
    reševanje(reš)
    return reš



def shrani_v_datoteko(ime_datoteke, sudoku, rešitev, st_napak, točke):
    with open(ime_datoteke, "w") as dat:
        slovar = {"sudoku": sudoku, 'rešitev': rešitev, 'st_napak': st_napak, 'točke': točke }
        json.dump(slovar, dat)


def preberi_iz_datoteke(ime_datoteke):
    with open(ime_datoteke) as dat:
        slovar = json.load(dat)
        return slovar


         

            
    





