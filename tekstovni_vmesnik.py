from osnovno import Model, Naloga

IME_DATOTEKE = "stanje.json"
try:
    moj_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moj_model = Model()

DODAJ_NOVO_NALOGO = X
RESI_NALOGE = Y
IZHOD = 9



def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")


def izberi_moznost(moznosti):
    """Uporabniku našteje možnosti ter vrne izbrano."""
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f"Vaš vnos ni pravilen.")


def prikaz_nalog(spisek):
    vsa = spisek.stevilo_vseh()
    if zamujena:
        return f"{spisek.ime} ({zamujena}!!! + {vsa - zamujena})"
    else:
        return f"{spisek.ime} ({vsa})"


def prikaz_opravila(opravilo):
    if opravilo.zamuja():
        return f"!!!{opravilo.ime}"
    elif opravilo.rok:
        return f"{opravilo.ime} ({opravilo.rok})"
    else:
        return f"{opravilo.ime}"


def izberi_spisek(model):
    return izberi_moznost([(spisek, prikaz_spiska(spisek)) for spisek in model.spiski])


def izberi_opravilo(model):
    return izberi_moznost(
        [
            (opravilo, prikaz_opravila(opravilo))
            for opravilo in model.aktualni_spisek.opravila
        ]
    )


def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        prikazi_aktualna_opravila()
        ukaz = izberi_moznost(
            [
                (DODAJ_NOVO_NALOGO, "dodaj nov spisek"),
                (RESI_NALOGO_STEVILKA , "reši nalogo y"),
                (IZHOD, "zapri program"),
            ]
        )
        if ukaz == DODAJ_NOVO_NALOGO:
            dodaj_spisek()
        elif ukaz == RESI_NALOGO_STEVILKA:
            pobrisi_spisek()
        elif ukaz == IZHOD:
            moj_model.shrani_v_datoteko(IME_DATOTEKE)
            print("Nasvidenje!")
            break


def prikazi_pozdravno_sporocilo():
    print("Pozdravljeni!")


def prikazi_aktualna_opravila():
    if moj_model.aktualni_spisek:
        for opravilo in moj_model.aktualni_spisek.opravila:
            if not opravilo.opravljeno:
                print(f"- {prikaz_opravila(opravilo)}")
    else:
        print("Ker nimate še nobenega spiska, morate enega ustvariti.")
        dodaj_spisek()


def dodaj_spisek():
    print("Vnesite podatke novega spiska.")
    ime = input("Ime> ")
    nov_spisek = Spisek(ime)
    moj_model.dodaj_spisek(nov_spisek)


def pobrisi_spisek():
    spisek = izberi_spisek(moj_model)
    moj_model.pobrisi_spisek(spisek)


def zamenjaj_spisek():
    print("Izberite spisek, na katerega bi preklopili.")
    spisek = izberi_spisek(moj_model)
    moj_model.zamenjaj_spisek(spisek)


def dodaj_opravilo():
    print("Vnesite podatke novega opravila.")
    ime = input("Ime> ")
    opis = input("Opis> ")
    rok = None
    novo_opravilo = Opravilo(ime, opis, rok)
    moj_model.dodaj_opravilo(novo_opravilo)


def opravi_opravilo():
    opravilo = izberi_opravilo(moj_model)
    opravilo.opravi()


tekstovni_vmesnik()
