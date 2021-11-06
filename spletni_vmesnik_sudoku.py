import bottle
import os
from pathlib import Path
from sudoku_koncni import reševanje, rešitev, preberi_iz_datoteke, shrani_v_datoteko
from generator2 import generiraj



bottle.TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

os.chdir(Path(__file__).parent)

IME_DATOTEKE = 'stanje.json'
try:
    slovar = preberi_iz_datoteke(IME_DATOTEKE)
    sud = slovar['sudoku']
    res = slovar['rešitev']
    st_napak = slovar['st_napak']
    točke = slovar['točke']

except FileNotFoundError:
    sud = generiraj(1)
    res = rešitev(sud)
    st_napak = 0
    točke = 0
    
nova_igra = True

@bottle.get('/')
def osnovna_stran():
    return bottle.template("osnovna_stran_za_spreminjat.tpl", sudokuseznam=sud, rešitev=res, napake=st_napak, score=točke, nova_igra=nova_igra)


@bottle.get('/dodaj/')
def dodaj_st():
    global st_napak, točke
    for k in range(81):
        i = k // 9
        j = k % 9
        try:
            stevilka = bottle.request.query[f'cell-{k}']
        except:
            continue
        if stevilka.isnumeric() and rešitev(sud)[i][j] == int(stevilka): 
            sud[i][j] = int(stevilka)
            točke += 1
        else:
            st_napak += 1
        shrani_v_datoteko('stanje.json', sud, res, st_napak, točke)
        bottle.redirect('/')

@bottle.get('/nova-igra-1')
def nova():
    global sud, st_napak, res, nova_igra

    sud = generiraj(1)
    res = rešitev(sud)
    st_napak = 0
    nova_igra = False
    bottle.redirect('/')

@bottle.get('/nova-igra-2')
def nova():
    global sud, st_napak, res, nova_igra

    sud = generiraj(2)
    res = rešitev(sud)
    st_napak = 0
    nova_igra = False
    bottle.redirect('/')

@bottle.get('/nova-igra-3')
def nova():
    global sud, st_napak, res, nova_igra

    sud = generiraj(3)
    res = rešitev(sud)
    st_napak = 0
    nova_igra = False
    bottle.redirect('/')



bottle.run(debug=True, reloader=True)
