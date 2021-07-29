from datetime import date
import json

class Model:
    def __init__(self, zacetni_seznam_nalog, tema):
        self.naloge = zacetni_seznam_nalog  # Seznam objektov "Naloga"
        self.aktualna_naloga = None
        self.tema = tema

    def dodaj_novo_nalogo(self, naloga):
        self.naloge.append(naloga)

    def v_slovar(self):

        seznam_nalog = [
            naloga.v_slovar() for naloga in self.naloge
        ]

        return {
            "naloge": seznam_nalog,
            "tema": self.tema,
        }

    def stevilo_opravljenih_nalog(self):
        stevilo = 0
        for naloga in self.naloge:
            if naloga.naloga_je_resena():
                stevilo += 1
        return stevilo

    def katere_naloge_so_resene(self):
        sez = []
        for naloga in self.naloge:
            if naloga.naloga_je_resena():
                sez.append(naloga["besedilo"])
        return sez
    #katere naloge so resene (seznam)

    def stevilo_vseh_nalog(self):
        return len(self.naloge)

            
    @staticmethod
    def iz_slovarja(slovar):
        sez = [
            Naloga.iz_slovarja(sl_naloga) for sl_naloga in slovar["naloge"]
        ]
        return Model(
            sez,
            slovar["tema"],

        )

    def shrani_v_datoteko(self, ime_datoteke='stanje.json'):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke='stanje.json'):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Model.iz_slovarja(slovar)

    def preveri_podatke_nove_naloge(self, ime):
        napake = {}
        if not ime:
            napake['ime'] = 'Ime ne sme bitit prazno!'
        elif len(ime) > 20:
            napake['ime'] = 'Ime lahko vsebuje najvec 20 znakov.'
        return napake


# {
#    "naloge":
#        [{podatki naloge 1:}, {podatk naloge 2}, ..],
#    "začetek": ...
# }


class Naloga:
    def __init__(self, ime, besedilo, pravilna_resitev, moja_resitev=None):
        self.ime = ime
        self.besedilo = besedilo
        self.pravilna_resitev = pravilna_resitev
        self.moja_resitev = moja_resitev

    def naloga_je_resena(self):
        return self.pravilna_resitev == self.moja_resitev

    def v_slovar(self):
        return {
            "ime": self.ime,
            "besedilo": self.besedilo,
            "pravilna resitev": self.pravilna_resitev,
            "moja resitev": self.moja_resitev,
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Naloga(
            slovar["ime"],
            slovar["besedilo"],
            slovar["pravilna resitev"],
            slovar["moja resitev"],
        )


n1 = Naloga("Napoleon", "Kdaj se je rodil?", "15.8.1769")
n2 = Naloga('New York', "Kje lezi?", "Severna Amerika")
n3 = Naloga('Olimpijske igra',
            "Kdo je osvoji zlato medaljo za Slovenijo?", "Benjamin Savsek")
n4 = Naloga(
    'You Tube', "Kako je ime prvemu videu objavlenemu na You Tubu?", "Me at the ZOO", "Me at the ZOO")
n5 = Naloga('Kardashianovi', "Koliko otrok ima Kris Jenner?", "6", "6")
n6 = Naloga('Ameriski predsedniki',
            "Kako je bilo ima prvemu ameriskemu predsedniku?", "George Washington", "George Washington")


