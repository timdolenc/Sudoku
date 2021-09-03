from sudoku_koncni import prazno_polje, ustrezno, reševanje, rešitev
from primeri import primer1, dverešitvi
import random
import copy



def izpolnjen():
    sudoku = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
    # naključno izpolni poševne tri kvadrate
    for k in range(3):
        sez = list(range(1, 10))
        for i in range(3 * k, 3 * k + 3):
            for j in range(3 * k, 3 * k + 3):
                n = random.choice(sez)
                if ustrezno(sudoku, n, (i, j)):
                    sudoku[i][j] = n
                    sez.remove(n)
    return dokončaj(sudoku)


def dokončaj(sudoku):
    '''dokonča poševno izpolnjen sudoku, podobno kot funkcija reševanje le da izbira naključne int, ne gre od 1 do 9'''
    if not prazno_polje(sudoku):
        return sudoku
    i, j = prazno_polje(sudoku)
    sez = list(range(1, 10))
    random.shuffle(sez)
    for n in sez:
        if ustrezno(sudoku, n, (i, j)):
            sudoku[i][j] = n

            if reševanje(sudoku):
                dokončaj(sudoku)
                return sudoku
            sudoku[i][j] = 0

    return False

def rešuj_po_polju(sudoku, i, j):
    for n in range(1, 10):
        if ustrezno(sudoku, n, (i, j)):
            sudoku[i][j] = n
            if reševanje(sudoku):
                return sudoku
            sudoku[i][j] = 0
    return False

def index_ktega_praznega(sudoku, k):
    h = 1
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                if h == k:
                    return (i, j)
                h += 1
    return False

def stevilo_praznih_polj(sudoku):
    k = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                k += 1
    return k

def sez_v_str(sudoku):
    x = ''
    for i in range(9):
        for j in range(9):
            x += str(sudoku[i][j])
    return x


def vse_rešitve(sudoku):
    sez = []
    for k in range(1, stevilo_praznih_polj(sudoku) + 1):
        i, j = index_ktega_praznega(sudoku, k)
        kopija = copy.deepcopy(sudoku)
        reš = rešuj_po_polju(kopija, i, j)
        v_str = sez_v_str(reš)
        sez.append(v_str)
    return list(set(sez))

def st_rešitev(sudoku):
    return len(vse_rešitve(sudoku))

def index_para(vrstica, stolpec):
    i = 8 - vrstica
    j = 8 - stolpec
    return i, j

def polja(k):
    sez = []
    while len(sez) < k:
        i = random.randint(0, 4)
        j = random.randint(0, 8)
        if (i, j) not in sez and not (i == 4 and j > 4):
            sez.append((i, j))
            sez.append(index_para(i, j))
    return sorted(sez)


def izprazni_polja(sudoku, k):
    #opomba: če je k sod bo izpraznilo k polj, če pa je k lih pa k + 1 polj, to ni tako važno ker bo k vedno sod
    while stevilo_praznih_polj(sudoku) < k:
        i = random.randint(0, 4)
        j = random.randint(0, 8)
        p1 = i, j
        i2, j2 = index_para(i, j)
        kopija = copy.deepcopy(sudoku)
        kopija[i][j] = 0
        kopija[i2][j2] = 0
        if st_rešitev(kopija) == 1:
            sudoku = kopija
    return sudoku


def generiraj(težavnost=1): #težavnost je od 1 do 3
    sudoku = izpolnjen()
    if težavnost == 0:
        sudoku = izprazni_polja(sudoku, 6)
    elif težavnost == 1:
        sudoku = izprazni_polja(sudoku, 32)
    elif težavnost == 2:
        sudoku = izprazni_polja(sudoku, 42)
    elif težavnost == 3:
        sudoku = izprazni_polja(sudoku, 50)
    return sudoku



        






