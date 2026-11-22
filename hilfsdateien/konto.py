#import main
from hilfsdateien  import daten

def registrieren (spieler):
    print("Benutzername muss mindestens zwei Zeichen lang sein")
    benutzername = input("Gib deinen neuen Benutzernamen ein:")
    while len(benutzername) <=2: #Schleife damit der Benutzer mindest zwei Zeichen lang ist. 
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


def login (spieler): 
    benutzer_eingabe = input("Gib dein Benutzer ein:")
    while benutzer_eingabe.lower() not in spieler:
        print("Login fehlgeschlagen, Benutzer nicht vorhanden")
        benutzer_eingabe = input("Gib dein Benutzer ein:")

    user = benutzer_eingabe.lower()
    passwort_eingabe = input("Gib dein Passwort ein:")
    while passwort_eingabe != spieler[user]["passwort"]:
        print("Passwort falsch")
        passwort_eingabe = input("Gib dein Passwort ein:")
    print("Login erfolgreich")
    return(user)
    

def statistik (spieler): 

   return()