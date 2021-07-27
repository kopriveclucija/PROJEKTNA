from datetime import date
import json

class Model:
    def __init__(self, zacetni_seznam_nalog, tema):
        self.naloge = zacetni_seznam_nalog # Seznam objektov "Naloga"
        self.tema = tema

    def dodaj_novo_nalogo(self, naloga):
        self.naloge.append(naloga)
    #doda nalogo v __init__

    def v_slovar(self):

        seznam_nalog = [
            naloga.v_slovar() for naloga in self.naloge 
        ]

        return {
            "naloge": seznam_nalog,
            "tema": self.tema,
        }


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
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Model.iz_slovarja(slovar)


#{
#    "naloge": 
#        [{podatki naloge 1:}, {podatk naloge 2}, ..],
#    "začetek": ...
#}


class Naloga:
    def __init__(self, ime, besedilo, pravilna_resitev, moja_resitev=None):
        self.ime = ime
        self.besedilo = besedilo
        self.pravilna_resitev = pravilna_resitev
        self.moja_resitev = moja_resitev

    def je_resena(self):
        return self.pravilna_resitev.lower() == self.moja_resitev.lower()

    def stevilo_resenih_nalog(self):
        stevilo = 0
        for naloga in self.naloge:
            if naloga.je_resena():
                stevilo += 1
        return stevilo
    #koliko nalog je resenih 

    def katere_naloge_so_resene(self):
        sez = []
        for naloga in self.naloge:
            if naloga.resena_naloga():
                sez.append(naloga)
        return sez
    #katere naloge so resene (seznam)

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


n1 = Naloga("Napoleon", "Kdaj se je rodil", "Nekoč")
n2 = Naloga('New York', "Kje lezi", "Amerika")
n3 = Naloga('Olimpijske igra', "Kdo je osvoji zlato medaljo za Slovenijo", "Benjamin Savšek")
n4 = Naloga('Olimpijske igra', "Kdo je osvoji zlato medaljo za Slovenijo", "Benjamin Savšek")

seznam = [n1, n2, n3, n4]

m = Model(seznam, "test")

