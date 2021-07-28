import bottle
import os
from osnovno import Model, Naloga

IME_DATOTEKE = "stanje.json"
try:
    moj_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moj_model = Model()

def prikaz_naloge(naloga):
    if naloga.naloga_je_resena():
        return f'{naloga.ime}'
    else:
        pass

def ze_resene_naloge():
    if moj_model.aktualna_naloga:
        for naloga in moj_model.aktualna_naloga.naloge:
            if naloga.naloga_je_resena():
                print(f'{prikaz_naloge(naloga)}')


@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna_stran.html', resenih=moj_model.stevilo_opravljenih_nalog(), stevilo_nalog=len(moj_model.naloge),)
 
@bottle.post('/dodaj/')
def dodaj_novo_nalogo():
    ime = bottle.request.forms.getunicode['ime']
    besedilo = bottle.request.forms.getunicode['besedilo']
    resitev = bottle.request.forms.getunicode['resitev']
    naloga = Naloga(ime, besedilo, resitev)
    moj_model.dodaj_novo_nalogo(naloga)
    moj_model.shrani_v_datoteko()
    bottle.redirect('/uspesno-dodajanje/')

@bottle.get('/uspesno-dodajanje/')
def uspesno_dodajanje():
    return 'Uspešno si dodal.'

bottle.run(reloader=True, debug=True)
