from datetime import date
import json

class Model:
    def __init__(self):
        self.naloge = []

    def dodaj_novo_nalogo(self, naloga):
        self.naloge.append(int(len(self.naloge)+1))
        self.naloga = naloga
    #doda nalogo v __init__
    
#class Naloga:
#    def __init__(self, ime):
#        self.ime = ime
#        self.naloge = []
#    
#
#    def stevilo_resenih_nalog(self):
#        stevilo = 0
#        for naloga in self.naloge:
#            if naloga.resena_naloga():
#                stevilo += 1
#        return stevilo
#    #koliko nalog je resenih
#
#    def katere_naloge_so_resene(self):
#        sez = []
#        for naloga in self.naloge:
#            if naloga.resena_naloga():
#                sez.append(naloga)
#        return sez
#    #katere naloge so resene (seznam)

class Posameznanaloga:
    def __init__(self, ime, besedilo, pravilna_resitev, moja_resitev=None):
        self.ime = ime
        self.besedilo = besedilo
        self.pravilna_resitev = pravilna_resitev
        self.moja_resitev = moja_resitev
        self.resena = (pravilna_resitev.lower == moja_resitev.lower)

    def resena_naloga(self):
        return self.pravilna_resitev.lower == self.moja_resitev.lower

    def stevilo_resenih_nalog(self):
        stevilo = 0
        for naloga in self.naloge:
            if naloga.resena_naloga():
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

