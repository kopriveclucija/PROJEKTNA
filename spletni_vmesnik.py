import bottle
import os
from osnovno import Model, Naloga


def nalozi_uporabnikovo_stanje():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    if uporabnisko_ime:
        return Model.preberi_iz_datoteke(uporabnisko_ime)
    else:
        bottle.redirect("/prijava/")


def shrani_uporabnikovo_stanje(stanje):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    stanje.shrani_v_datoteko(uporabnisko_ime)


@bottle.get('/')
def osnovna_stran():
    model = nalozi_uporabnikovo_stanje()
    return bottle.template('base.html',
                           resenih=model.stevilo_opravljenih_nalog(),
                           stevilo_nalog=len(model.naloge), vse_naloge=model.naloge, uporabnisko_ime=bottle.request.get_cookie("uporabnisko_ime"))


@bottle.get("/registracija/")
def registracija_get():
    return bottle.template("registracija.html", napake={}, polja={}, uporabnisko_ime=None)


@bottle.post("/registracija/")
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime že obstaja."}
        return bottle.template("registracija.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie(
            "uporabnisko_ime", uporabnisko_ime, path="/")
        model = Model.naredi_svezega()
        model.shrani_v_datoteko(uporabnisko_ime)
        bottle.redirect("/")


@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.html", napake={}, polja={}, uporabnisko_ime=None)


@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    print(uporabnisko_ime)
    if not os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime ne obstaja."}
        return bottle.template("prijava.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie(
            "uporabnisko_ime", uporabnisko_ime, path="/")
        bottle.redirect("/")


@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    bottle.redirect("/")


@bottle.post('/dodaj/')
def dodaj_novo_nalogo():
    model = nalozi_uporabnikovo_stanje()
    ime = bottle.request.forms.getunicode('ime')
    besedilo = bottle.request.forms.getunicode('besedilo')
    resitev = bottle.request.forms.getunicode('resitev')
    polja = {'ime': ime}
    napake = model.preveri_podatke_nove_naloge(ime)
    if napake:
        return bottle.template('dodaj_nalogo.html', napake=napake, polja=polja, resenih=model.stevilo_opravljenih_nalog(),
                               stevilo_nalog=len(model.naloge), vse_naloge=model.naloge, uporabnisko_ime=bottle.request.get_cookie("uporabnisko_ime"))
    else:
        naloga = Naloga(ime, besedilo, resitev)
        model.dodaj_novo_nalogo(naloga)
        model.shrani_v_datoteko(bottle.request.get_cookie("uporabnisko_ime"))
    bottle.redirect("/pregled_nalog/")


@bottle.get('/pregled_nalog/')
def vse_naloge_na_strani():
    model = nalozi_uporabnikovo_stanje()
    return bottle.template('pregled_nalog.html',
                           resenih=model.stevilo_opravljenih_nalog(),
                           stevilo_nalog=len(model.naloge), vse_naloge=model.naloge,
                           uporabnisko_ime=bottle.request.get_cookie("uporabnisko_ime"))


@bottle.post('/preklici/')
def preklici():
    bottle.redirect("/pregled_nalog/")


@bottle.get("/posamezna_naloga/<ud:int>")
def posamezna_naloga(ud):
    model = nalozi_uporabnikovo_stanje()
    moja_resitev = bottle.request.forms.getunicode('moje_resitev')
    naloga = model.naloge[ud]
    polja = {'moja resitev': moja_resitev}
    return bottle.template('posamezna_naloga.html', naloga=naloga,  polja=polja, uporabnisko_ime=bottle.request.get_cookie("uporabnisko_ime"), vse_naloge=model.naloge,)


bottle.run(reloader=True, debug=True)
