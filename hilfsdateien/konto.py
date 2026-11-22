#import main
from hilfsdateien  import daten

def registrieren (spieler):
    print("Benutzername muss mindestens zwei Zeichen lang sein")
    benutzername = input("Gib deinen neuen Benutzernamen ein:")
    while len(benutzername) <=1: #Schleife damit der Benutzer mindest zwei Zeichen lang ist. 
        print("Benutzername zu kurz")
        benutzername = input("Gib deinen neuen Benutzernamen ein:")
    while benutzername.lower() in spieler:
        print("Benutzername bereits vorhanden")
        benutzername = input("Gib deinen neuen Benutzernamen ein:")

    print("Passwort muss mindest 6 Zeichen lang sein")
    passwort = input("Gib dein neues Passwort ein:")
    while len(passwort) < 6: #Schleife damit das Passwort mindest sechs Zeichen lang ist. 
        print("Passwort zu kurz")
        passwort = input("Gib dein neues Passwort ein:")

    spieler[benutzername.lower()] = { #neuer Spieler ins Dictionary eintragen. 
        "name": benutzername, 
        "passwort": passwort,  
        "guthaben": 100,  
        "spiele": 0, 
        "gewinne": 0,  
        "verluste": 0,  
    }
    daten.speichern(spieler)    #Spieler in die Datei speichern
    print("Benutzer erstellt und Startguthaben von 100 CHF zugewiesen")


def login (): 
    benutzer_eingabe = input("Gib dein Benutzer ein:")
    passwort_eingabe = input("Gib dein Passwort ein:")
    with open(spiel_datei, 'r', encoding='utf-8') as file:
        benutzername_datei = file.read
    while benutzer_eingabe and passwort_eingabe != benutzername_datei: 
        print("Login fehlgeschlagen, User oder Passwort falsch")
        benutzer_eingabe = input("Gib dein Benutzer ein:")
        passwort_eingabe = input("Gib dein Passwort ein:")
    print("Login erfolgreich")
    return(benutzer_eingabe, passwort_eingabe)
    
login()

def statistik (): # Mit User ausfüllen, in diesem sind alle Spielerdaten gespeichert
   # print(user.(anzahl_spiele))
   # print (user.(Guthaben))
   return()