# ==================================================
# konto.py
# Registrieren, Login und Statistik der Spieler
# ==================================================

from hilfsdateien import daten


# --------------------------------------------------
# Registrieren
# --------------------------------------------------

def registrieren(spieler):
    print()
    print("=" * 40)
    print("REGISTRIEREN".center(40))
    print("=" * 40)

    # Benutzername eingeben
    print("Benutzername muss mindestens zwei Zeichen lang sein.")
    benutzername = input("Gib deinen neuen Benutzernamen ein: ")

    while len(benutzername) <= 2:  # Schleife, damit der Benutzername mindestens zwei Zeichen lang ist
        print("Benutzername zu kurz.")
        benutzername = input("Gib deinen neuen Benutzernamen ein: ")

    while benutzername.lower() in spieler:  # Schleife, damit der Benutzername noch nicht vergeben ist
        print("Benutzername bereits vorhanden.")
        benutzername = input("Gib deinen neuen Benutzernamen ein: ")

    print("-" * 40)

    # Passwort eingeben
    print("Passwort muss mindestens 6 Zeichen lang sein.")
    passwort = input("Gib dein neues Passwort ein: ")

    while len(passwort) < 6:  # Schleife, damit das Passwort mindestens sechs Zeichen lang ist
        print("Passwort zu kurz.")
        passwort = input("Gib dein neues Passwort ein: ")

    # neuen Spieler ins Dictionary eintragen
    spieler[benutzername.lower()] = {
        "name": benutzername,
        "passwort": passwort,
        "guthaben": 100,
        "spiele": 0,
        "gewinne": 0,
        "verluste": 0,
    }

    daten.speichern(spieler)  # Spieler in die Datei speichern

    print("-" * 40)
    print("Benutzer erstellt.")
    print("Startguthaben: CHF 100")
    print("=" * 40)


# --------------------------------------------------
# Login
# --------------------------------------------------

def login(spieler):
    print()
    print("=" * 40)
    print("LOGIN".center(40))
    print("=" * 40)

    # Benutzername prüfen
    benutzer_eingabe = input("Gib deinen Benutzernamen ein: ")

    while benutzer_eingabe.lower() not in spieler:
        print("Login fehlgeschlagen, Benutzer nicht vorhanden.")
        benutzer_eingabe = input("Gib deinen Benutzernamen ein: ")

    name = benutzer_eingabe.lower()  # im Dictionary sind die Namen klein geschrieben

    # Passwort prüfen
    passwort_eingabe = input("Gib dein Passwort ein: ")

    while passwort_eingabe != spieler[name]["passwort"]:
        print("Passwort falsch.")
        passwort_eingabe = input("Gib dein Passwort ein: ")

    print("-" * 40)
    print("Login erfolgreich.")
    return name


# --------------------------------------------------
# Statistik
# --------------------------------------------------

def statistik(spieler, name):
    print()
    print("=" * 40)
    print("STATISTIK".center(40))
    print("-" * 40)
    print("Spieler:      ", spieler[name]["name"])
    print("Guthaben:      CHF", spieler[name]["guthaben"])
    print("Anzahl Spiele:", spieler[name]["spiele"])
    print("Gewinne:      ", spieler[name]["gewinne"])
    print("Verluste:     ", spieler[name]["verluste"])
    print("=" * 40)
