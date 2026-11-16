
DATEI = "hilfsdateien/spieler.txt"  # Pfad zur Datei, nur hier festgelegt (Programm aus dem Hauptordner starten)

def zeile_verarbeiten(zeile):  # macht aus einer Textzeile ein Spieler-Dictionary
    zeile = zeile.strip()  # entfernt Zeilenumbruch \n und Leerzeichen am Rand
    if zeile == "":  # ist die Zeile leer?
        return None  # dann kein Spieler: None zurückgeben

    teile = zeile.split(";")  # zerlegt die Zeile am Strichpunkt in eine Liste
    if len(teile) != 6:  # verlangt genau 6 Felder
        return None  # falsche Anzahl Felder: Zeile ist fehlerhaft

    name = teile[0]  # 1. Feld: Benutzername
    passwort = teile[1]  # 2. Feld: Passwort
    if name == "":  # ein Spieler ohne Namen ist ungültig
        return None  # leerer Name: Zeile ist fehlerhaft

    try:  # versuchen, die vier Zahlenfelder umzuwandeln
        guthaben = int(teile[2])  # 3. Feld: Guthaben als ganze Zahl
        spiele = int(teile[3])  # 4. Feld: Anzahl Spiele
        gewinne = int(teile[4])  # 5. Feld: Anzahl Gewinne
        verluste = int(teile[5])  # 6. Feld: Anzahl Verluste
    except ValueError:  # z.B. int("abc") geht nicht
        return None  # keine gültige Zahl: Zeile ist fehlerhaft

    eintrag = {  # Dictionary wird gebaut
        "name": name, 
        "passwort": passwort,  
        "guthaben": guthaben,  
        "spiele": spiele, 
        "gewinne": gewinne,  
        "verluste": verluste,  
    }
    return eintrag  # fertigen Spieler zurückgeben


def zeile_erstellen(eintrag):  # macht aus einem Spieler-Dictionary eine Textzeile
    zeile = (f"{eintrag['name']};{eintrag['passwort']};{eintrag['guthaben']};"  # Werte mit ; verbinden
             f"{eintrag['spiele']};{eintrag['gewinne']};{eintrag['verluste']}\n")  # \n = neue Zeile am Ende
    return zeile  # z.B. "Ruben;geheim1;100;0;0;0\n"


def laden():  # liest alle Spieler aus der Datei
    spieler = {}  # leeres Dictionary, Schlüssel = Name in Kleinbuchstaben
    try:  # versuchen, die Datei zu öffnen
        with open(DATEI, "r", encoding="utf-8") as datei:  # "r" = lesen; with schliesst automatisch
            for zeile in datei:  # Datei Zeile für Zeile durchgehen
                eintrag = zeile_verarbeiten(zeile)  # Zeile in Spieler umwandeln
                if eintrag is None:  # war die Zeile fehlerhaft?
                    continue  # dann überspringen, nächste Zeile
                schluessel = eintrag["name"].lower()  # "Ruben" wird zu "ruben" 
                if schluessel in spieler:  # gibt es diesen Namen schon?
                    continue  # Duplikat überspringen, die erste Zeile zählt
                spieler[schluessel] = eintrag  # Spieler ins Dictionary legen
    except FileNotFoundError:  # Datei existiert noch nicht (z.B. erster Start)
        with open(DATEI, "w", encoding="utf-8") as datei:  # "w" erstellt eine neue leere Datei
            pass  # nichts hineinschreiben
    return spieler  # alle gültigen Spieler zurückgeben (oder leeres Dictionary)


def speichern(spieler):  # schreibt alle Spieler in die Datei
    with open(DATEI, "w", encoding="utf-8") as datei:  # "w" überschreibt die ganze Datei
        for eintrag in spieler.values():  # jeden Spieler durchgehen (nur die Werte)
            datei.write(zeile_erstellen(eintrag))  # Spieler als Zeile in die Datei schreiben

