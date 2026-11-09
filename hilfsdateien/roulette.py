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


