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

wetten = []
restguthaben = guthaben
runde_laeuft = True
neue_wette = True

#loop um eine wette nach der anderen zu setzen:
while True:
    restguthaben = guthaben - summe_einsaetze(wetten)
    auf = wette_einlesen()
    einsatz = einsatz_einlesen(restguthaben)

    #wetten speichern
    wetten.append({"auf": auf, "einsatz": einsatz})
    restguthaben = restguthaben - einsatz
    wetten_anzeigen(wetten, restguthaben)

#inner loop (menu, drehen, abbrechen)

while True:
    wahl = input("weiter / drehen / abbrechen?")


