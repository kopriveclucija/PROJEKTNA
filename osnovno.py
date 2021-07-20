from datetime import date
import json

class Model:
    def __init__(self):
        self.naloga = Naloga('Edini spisek')
    
class Naloga:
    def __init__(self, ime):
        self.ime = ime
        self.naloge = []
    #self.besedilo = besedilo
    #self.resitev = resitev
    #self.resena = False

    def dodaj_nalogo(self, naloga):
        self.naloge.append(naloga) 
    #doda nalogo v __init__

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
    #katere naloge so resene seznam

class Posameznanaloga:
    def __init__(self, ime, besedilo, resitev):
        self.ime = ime
        self.besedilo = besedilo
        self.resitev = resitev
        self.resena = False

    def opravi_nalogo(self):
        self.resena = True

    def resena_naloga(self):
        return self.resena
