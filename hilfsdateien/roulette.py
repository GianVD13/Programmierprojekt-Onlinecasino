# ==================================================
# roulette.py
# Eine Runde Roulette: Wetten setzen, drehen oder abbrechen
# ==================================================

from hilfsdateien import auswertung
from hilfsdateien import daten


# --------------------------------------------------
# Einstellungen
# --------------------------------------------------

MINDESTEINSATZ = 5
ERLAUBTE_WOERTER = ["rot", "schwarz", "gerade", "ungerade"]


# --------------------------------------------------
# Wette einlesen
# --------------------------------------------------

def ist_gueltige_wette(eingabe):  # prüft, ob die Eingabe eine erlaubte Wette ist
    if eingabe in ERLAUBTE_WOERTER:
        return True

    try:
        zahl = int(eingabe)
    except ValueError:
        return False
    else:
        return 0 <= zahl <= 36


# Einlesen im Loop: schaut, ob die Wette richtig eingegeben wird.
# Mit .strip() und .lower() werden Falscheingaben korrigiert.
def wette_einlesen():
    text = "Worauf setzt du? (0-36, rot, schwarz, gerade, ungerade): "
    eingabe = input(text).strip().lower()

    while not ist_gueltige_wette(eingabe):
        print("Ungültige Wette.")
        eingabe = input(text).strip().lower()

    if eingabe in ERLAUBTE_WOERTER:
        return eingabe
    return int(eingabe)


# --------------------------------------------------
# Einsatz einlesen
# --------------------------------------------------

def ist_gueltiger_einsatz(eingabe, restguthaben):  # prüft, ob der Einsatz im erlaubten Bereich ist
    try:
        einsatz = int(eingabe)
    except ValueError:
        return False
    else:
        return MINDESTEINSATZ <= einsatz <= restguthaben


def einsatz_einlesen(restguthaben):
    text = f"Einsatz (CHF {MINDESTEINSATZ} bis {restguthaben}): "
    eingabe = input(text)

    while not ist_gueltiger_einsatz(eingabe, restguthaben):
        print("Ungültiger Einsatz.")
        eingabe = input(text)

    return int(eingabe)


# --------------------------------------------------
# Wetten anzeigen
# --------------------------------------------------

def wetten_anzeigen(wetten, restguthaben):
    print("-" * 40)
    print("Deine Wetten:")

    for wette in wetten:
        print(f"  CHF {wette['einsatz']} auf {wette['auf']}")

    print(f"Restguthaben: CHF {restguthaben}")
    print("-" * 40)


# --------------------------------------------------
# Eine Runde spielen
# --------------------------------------------------

def runde(spieler, name):
    guthaben = spieler[name]["guthaben"]

    print()
    print("=" * 40)
    print("ROULETTE".center(40))
    print("-" * 40)
    print(f"Guthaben:       CHF {guthaben}")
    print(f"Mindesteinsatz: CHF {MINDESTEINSATZ}")
    print("=" * 40)

    if guthaben < MINDESTEINSATZ:
        print("Game Over - Guthaben ist zu klein.")
        return

    # Liste für alle Wetten dieser Runde
    wetten = []
    restguthaben = guthaben

    # Solange runde_laeuft True ist, läuft die Schleife weiter.
    # neue_wette = True heisst: als Nächstes wird eine neue Wette eingelesen.
    runde_laeuft = True
    neue_wette = True

    while runde_laeuft:

        # neue Wette einlesen und in die Liste legen
        if neue_wette:
            auf = wette_einlesen()
            einsatz = einsatz_einlesen(restguthaben)
            wetten.append({"auf": auf, "einsatz": einsatz})
            restguthaben = restguthaben - einsatz
            wetten_anzeigen(wetten, restguthaben)
            neue_wette = False

        wahl = input("mehr einsetzen / drehen / abbrechen? ")

        if wahl == "mehr einsetzen ":
            if restguthaben < MINDESTEINSATZ:
                print("Dein Guthaben reicht für keine weitere Wette.")
            else:
                neue_wette = True

        elif wahl == "drehen":
            if len(wetten) == 0:
                print("Keine Wette gesetzt.")
            else:
                zahl = auswertung.drehen()
                auswertung.auswerten(spieler, name, wetten, zahl)
                daten.speichern(spieler)

                if spieler[name]["guthaben"] < MINDESTEINSATZ:
                    print("Game Over - dein Guthaben reicht nicht mehr zum Spielen.")
                runde_laeuft = False

        elif wahl == "abbrechen":
            print("Wetten gelöscht.")
            runde_laeuft = False

        else:
            print("Bitte weiter, drehen oder abbrechen eingeben.")
