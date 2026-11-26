# ==================================================
# main.py
# Startet das Programm: Startmenü und Hauptmenü
# ==================================================

from hilfsdateien import daten  # Import der anderen Dateien
from hilfsdateien import konto
from hilfsdateien import roulette


# --------------------------------------------------
# Hauptmenü (nach dem Login)
# --------------------------------------------------

def hauptmenü(spieler, name):
    # while-Schleife: das Menü kommt immer wieder, bis man sich ausloggt
    while True:
        print()
        print("=" * 40)
        print("HAUPTMENÜ".center(40))  # .center(40) setzt den Text in die Mitte der Linie
        print("-" * 40)
        print("Spieler: ", spieler[name]["name"])
        print("Guthaben: CHF", spieler[name]["guthaben"])
        print("-" * 40)
        print("1  Roulette")
        print("2  Statistik")
        print("3  Ausloggen")
        print("=" * 40)

        auswahl = int(input("Auswahl (1, 2, 3): "))

        if auswahl == 1:  # ruft die Funktion runde in roulette.py auf
            while True:  # Endlosschleife, endet nur mit break
                roulette.runde(spieler, name)
                wahl = input("Weiterspielen? (ja/nein): ").strip().lower()
                if wahl != "ja":  # alles ausser ja heisst: zurück
                    break  # Schleife verlassen, zurück ins Hauptmenü

        elif auswahl == 2:  # ruft die Funktion statistik in konto.py auf
            konto.statistik(spieler, name)
            input("Drücke Enter, um zurück zum Hauptmenü zu kommen ")

        elif auswahl == 3:  # zurück zum Startmenü
            print()
            print("Sie wurden ausgeloggt.")
            break

        else:
            print("Ungültige Eingabe, bitte 1, 2 oder 3 eingeben.")


# --------------------------------------------------
# Startmenü (vor dem Login)
# --------------------------------------------------

def startmenü(spieler):
    # while-Schleife: das Menü kommt immer wieder, bis man beendet
    while True:
        print()
        print("=" * 40)
        print("ONLINE CASINO".center(40))
        print("-" * 40)
        print("1  Registrieren")
        print("2  Login")
        print("3  Beenden")
        print("=" * 40)

        auswahl = int(input("Auswahl (1, 2, 3): "))

        if auswahl == 1:  # ruft die Funktion registrieren in konto.py auf
            konto.registrieren(spieler)

        elif auswahl == 2:  # ruft die Funktion login in konto.py auf
            name = konto.login(spieler)
            if name is not None:  # wenn der Login geklappt hat, Hauptmenü öffnen
                hauptmenü(spieler, name)

        elif auswahl == 3:  # Programm beenden
            print()
            print("Auf Wiedersehen!")
            break

        else:
            print("Ungültige Eingabe, bitte 1, 2 oder 3 eingeben.")


# --------------------------------------------------
# Programmstart
# --------------------------------------------------

spieler = daten.laden()  # beim Start alle Spieler aus spieler.txt laden
startmenü(spieler)       # Programm starten mit den geladenen Spielern
