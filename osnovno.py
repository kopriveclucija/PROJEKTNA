from datetime import date

class Model:
    def __init__(self):
        self.spisek = Zavihki('Edini spisek')

class Zavihki:
    def __init__(self, ime):
        self.ime = ime
        self.naloge = []
    
    def stevilo_opravljenih(self):
        stevilo = None 

#class Dolocena_naloga:
#    def __init__(self, ime, besedilo)
