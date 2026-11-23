import auswertung
import daten

MINDESTEINSATZ = 5
ERLAUBTE_WOERTER = ["rot", "schwarz", "gerade", "ungerade"]

#einlesen im loop schaut ob die Wette richtig eingegeben wird. mit.strip und.lower werden 
#  Falscheingaben korrigiert.

def ist_gueltige_wette(eingabe):
    if eingabe in ERLAUBTE_WOERTER:
        return True
    try:
        zahl = int(eingabe)
    except ValueError:
        return False
    else:
        return 0 <= zahl <= 36


def wette_einlesen():
    eingabe = input("Worauf setzt du? (0-36, rot, schwarz, gerade, ungerade):")
    while not ist_gueltige_wette(eingabe):
        print("ungültige Zahl")
        eingabe = input("Worauf setzt du? (0-36, rot, schwarz, gerade, ungerade):")

    if eingabe in ERLAUBTE_WOERTER:
        return eingabe
    return int(eingabe)

def ist_gueltiger_einsatz(eingabe, restguthaben):
    try:
        einsatz = int(eingabe)
    except ValueError:
        return False
    else:
        return MINDESTEINSATZ <= einsatz <= restguthaben


def einsatz_einlesen(restguthaben):
    text= f"Einsatz (CHF{MINDESTEINSATZ}bis{restguthaben}):"
    eingabe = input(text)
    while not ist_gueltiger_einsatz(eingabe, restguthaben):
        print("ungültiger Einsatz")
        eingabe = input(text)
    return int(eingabe)


def wetten_anzeigen(wetten, restguthaben):
    print("Deine Wetten:")
    for wette in wetten:
        print(f"CHF {wette["einsatz"]} auf {wette["auf"]}")
    print(f"Restguthaben: CHF {restguthaben}")

def runde(spieler, name):
    guthaben = spieler[name]["guthaben"]
    

if guthaben < MINDESTEINSATZ:
    print("Game Over - Guthaben ist zu klein.")
    return

#dictionary für die wetten wenn runde läuft und neue wette false dann runde wird beendet.
#loop um eine wette nach der anderen zu setzen:

wetten = []
restguthaben = guthaben
runde_laeuft = True
neue_wette = True

while runde_laeuft:
    if neue_wette:
        auf = wette_einlesen()
        einsatz = einsatz_einlesen(restguthaben)
        wetten.append({"auf": auf, "einsatz": einsatz})
        restguthaben = restguthaben - einsatz
        wetten_anzeigen(wetten, restguthaben)
        neue_wette = False
    wahl = input("weiter / drehen / abbrechen?")

    if wahl == "weiter":
        if restguthaben < MINDESTEINSATZ:
            print("Dein Guthaben reicht für keine weitere Wette.")
        else:
            neue_wette = True

    elif wahl == "drehen":
        if len(wetten) == 0:
            print("Keine Wette gesetzt")
        else:
            zahl = auswertung.drehen()
            auswertung.auswerten(spieler, name, wetten, zahl)
            daten.speichern(spieler)
            if spieler[name]["guthaben"] < MINDESTEINSATZ:
                print("Game Over - dein Guthaben reicht nicht mehr zum spielen.")
            runde_laeuft = False

    elif wahl == "abbrechen":
        print("Wetten gelöscht")
        runde_laeuft = False

    else:
        print("Bitte weiter, drehen oder abbrechen eingeben.")


