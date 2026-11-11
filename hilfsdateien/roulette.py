import auswertung
import daten

MINDESTEINSATZ = 5
ERLAUBTE_WOERTER = ["rot", "schwarz", "gerade", "ungerade"]

#einlesen im loop schaut ob die Wette richtig eingegeben wird. mit.strip und.lower werden 
#  Falscheingaben korrigiert.


def wette_einlesen():
    while True:
        eingabe = input("Worauf setzt du? (0-36, rot, schwarz, gerade, ungerade):")
        eingabe = eingabe.strip().lower()
        if eingabe in ERLAUBTE_WOERTER:
            return eingabe
        try:
            zahl = int(eingabe)
            if 0 <= zahl <= 36:
                return zahl
        except ValueError:
            pass
        print("Ungültige Zahl")

def einsatz_einlesen(restguthaben):
    while True:
        eingabe = input(f"Einsatz (CHF{MINDESTEINSATZ} bis {restguthaben}):").strip()
        try:
            einsatz = int(eingabe)
            if MINDESTEINSATZ <= einsatz <= restguthaben:
                return einsatz
        except ValueError:
            pass

        print("Ungültiger Einsatz")

def summe_einsaetze(wetten):
    summe = 0
    for wette in wetten:
        summe += wette["einsatz"]
    return summe

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


