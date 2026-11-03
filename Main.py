from hilfsdateien import daten #Import der anderen Dateien
from hilfsdateien import konto
from hilfsdateien import roulette



def hauptmenü(spieler, name): #Definition vom Hauptmenü mit while Schleife man kann auswählen was man will
    while True:
        print("Spieler:", spieler[name]["name"])
        print("Guthaben: CHF", spieler[name]["guthaben"])
        print("1 Roulette")
        print("2 Statistik")
        print("3 Ausloggen")
        auswahl = input("Auswahl (1,2,3): ")

        if auswahl == "1": #Ruft die Funktion roulette.runde in Roulette auf
            roulette.runde(spieler, name)
        elif auswahl == "2": #Ruft die Funktion konto.statisktik in Statistik auf
            konto.statistik(spieler, name)
        elif auswahl == "3": #kommt zurück zum Startmenü
            print ("Sie wurden ausgeloggt")
            break
        else:
            print("Ungültige Eingabe, bitte 1,2 oder 3 eingeben.")



def startmenü(spieler): #Das Startmenü definiert mit einer while schleife kann man auswählen was man will
    while True:
        print ("1 Registrieren")
        print ("2 Login")
        print ("3 Beenden")
        auswahl = input("Auswahl (1,2,3): ")

        if auswahl == "1": # wenn 1 wird die Funktion registieren aus der Datei Konto aufgerufen
            konto.registrieren(spieler)
        elif auswahl == "2": # wenn 2 wird die Funktion Login aus der Datei Konto aufgerufen
            name = konto.login(spieler)
            if name is not None: #wenn Name nicht None ist wird das Hauptmenü aufgerufen
                hauptmenü(spieler, name)
        elif auswahl == "3": # wenn 2 wird Break
            print ("Auf Wiedersehen")
            break
        else:
            print("Ungültige Eingabe, bitte 1,2 oder 3 eingeben.")

startmenü({"Jonas": {"name": "Jonas", "guthaben": 100}})