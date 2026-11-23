# ==================================================
# auswertung.py
# Drehen, Farbe bestimmen und eine Runde auswerten
# ==================================================

import random  # Modul für Zufallszahlen


# --------------------------------------------------
# Einstellungen
# --------------------------------------------------

# Alle roten Zahlen (US08). Alle anderen Zahlen ausser 0 sind schwarz.
ROTE_ZAHLEN = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


# --------------------------------------------------
# Drehen und Farbe
# --------------------------------------------------

def drehen():  # dreht das Roulette (US09)
    zahl = random.randint(0, 36)  # zufällige ganze Zahl von 0 bis und mit 36
    return zahl  # gefallene Zahl zurückgeben


def farbe(zahl):  # gibt die Farbe einer Zahl zurück (US09)
    if zahl == 0:  # die 0 ist grün
        return "Grün"
    elif zahl in ROTE_ZAHLEN:  # steht die Zahl in der Liste der roten Zahlen?
        return "Rot"
    else:  # alle anderen Zahlen sind schwarz
        return "Schwarz"


# --------------------------------------------------
# Auszahlung einer Wette
# --------------------------------------------------

def auszahlung(wette, zahl):  # berechnet, wie viel eine Wette zurückgibt (US07 + US08)
    auf = wette["auf"]  # worauf gesetzt wurde, z.B. 17 oder "rot"
    einsatz = wette["einsatz"]  # wie viel gesetzt wurde, z.B. 10

    if auf == zahl:  # Wette auf eine Zahl und genau diese Zahl ist gefallen
        return einsatz * 36  # 35-facher Gewinn + Einsatz zurück (CHF 10 -> CHF 360)

    if zahl == 0:  # bei 0 verlieren rot, schwarz, gerade und ungerade
        return 0

    if auf == "rot" and farbe(zahl) == "Rot":  # auf Rot gesetzt und Rot gefallen
        return einsatz * 2  # doppelter Einsatz zurück (CHF 10 -> CHF 20)
    if auf == "schwarz" and farbe(zahl) == "Schwarz":  # auf Schwarz gesetzt und Schwarz gefallen
        return einsatz * 2
    if auf == "gerade" and zahl % 2 == 0:  # % 2 == 0 heisst: Zahl ist gerade
        return einsatz * 2
    if auf == "ungerade" and zahl % 2 == 1:  # % 2 == 1 heisst: Zahl ist ungerade
        return einsatz * 2

    return 0  # in allen anderen Fällen ist die Wette verloren


# --------------------------------------------------
# Ganze Runde auswerten
# --------------------------------------------------

def auswerten(spieler, name, wetten, zahl):  # wertet eine ganze Runde aus (US09 + US10)
    print()
    print("=" * 40)
    print("ERGEBNIS".center(40))
    print("-" * 40)
    print(f"Die Kugel fällt auf: {zahl} ({farbe(zahl)})")  # z.B. "14 (Rot)"
    print("-" * 40)

    gesetzt = 0  # Summe aller Einsätze dieser Runde
    ausbezahlt = 0  # Summe aller Auszahlungen dieser Runde

    for wette in wetten:  # jede Wette einzeln anschauen
        betrag = auszahlung(wette, zahl)  # wie viel bekommt man für diese Wette?
        auf = wette["auf"]  # für die Ausgabe
        einsatz = wette["einsatz"]  # für die Ausgabe

        if betrag > 0:  # Wette hat gewonnen
            print(f"  CHF {einsatz} auf {auf}: gewonnen, du bekommst CHF {betrag}")
        else:  # Wette hat verloren
            print(f"  CHF {einsatz} auf {auf}: verloren")

        gesetzt = gesetzt + einsatz  # Einsatz dazuzählen
        ausbezahlt = ausbezahlt + betrag  # Auszahlung dazuzählen

    # neues Guthaben: Einsätze weg, Auszahlungen dazu
    spieler[name]["guthaben"] = spieler[name]["guthaben"] - gesetzt + ausbezahlt

    # Statistik (US10): eine Drehung = ein Spiel, egal wie viele Wetten
    spieler[name]["spiele"] = spieler[name]["spiele"] + 1
    if ausbezahlt > gesetzt:  # mehr zurückbekommen als gesetzt = Gewinn
        spieler[name]["gewinne"] = spieler[name]["gewinne"] + 1
    else:  # sonst = Verlust
        spieler[name]["verluste"] = spieler[name]["verluste"] + 1

    neues_guthaben = spieler[name]["guthaben"]  # für die Ausgabe
    print("-" * 40)
    print(f"Neues Guthaben: CHF {neues_guthaben}")
    print("=" * 40)
