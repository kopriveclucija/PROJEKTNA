import bottle
import os
from osnovno import Model, Naloga

IME_DATOTEKE = "stanje.json"
try:
    moj_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moj_model = Model([], '')

@bottle.post('/')
def osnovna_stran():
    moj_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
    return bottle.template('base.html',
     resenih=moj_model.stevilo_opravljenih_nalog(),
      stevilo_nalog=len(moj_model.naloge), vse_naloge=moj_model.naloge)
 
@bottle.post('/dodaj/')
def dodaj_novo_nalogo():
    ime = bottle.request.forms.getunicode('ime')
    besedilo = bottle.request.forms.getunicode('besedilo')
    resitev = bottle.request.forms.getunicode('resitev')
    polja = {'ime': ime}
    napake = moj_model.preveri_podatke_nove_naloge(ime)
    if napake:
        return bottle.template('dodaj_nalogo.html', napake=napake, polja=polja, resenih=moj_model.stevilo_opravljenih_nalog(),
      stevilo_nalog=len(moj_model.naloge), vse_naloge=moj_model.naloge)
    else:
        naloga = Naloga(ime, besedilo, resitev)
        moj_model.dodaj_novo_nalogo(naloga)
        moj_model.shrani_v_datoteko()


@bottle.get('/uspesno-dodajanje/')
def uspesno_dodajanje():
    return 'Uspešno si dodal.'

@bottle.post('/pregled_nalog/')
def vse_naloge_na_strani():
    moj_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
    return bottle.template('pregled_nalog.html',
     resenih=moj_model.stevilo_opravljenih_nalog(),
      stevilo_nalog=len(moj_model.naloge), vse_naloge=moj_model.naloge)


@bottle.post('/preklici/')
def preklici():
    bottle.redirect("/pregled_nalog/")

@bottle.post("/posamezna_naloga/")
def posamezna_naloga():
    moj_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
    return bottle.template('posamezna_naloga.html',
     resenih=moj_model.stevilo_opravljenih_nalog(),
      stevilo_nalog=len(moj_model.naloge), vse_naloge=moj_model.naloge)


bottle.run(reloader=True, debug=True)

