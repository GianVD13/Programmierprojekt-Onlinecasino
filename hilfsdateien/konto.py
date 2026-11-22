#import main
from hilfsdateien  import daten
spiel_datei = 'hilfsdateien/spieler.txt'

def registrieren ():
    print("Benutzername muss mindestens zwei Zeichen lang sein")
    benutzername = input("Gib deinen neuen Benutzernamen ein:")
    while len(benutzername) <=1: #Schleife damit der Benutzer mindest zwei Zeichen lang ist. 
        print("Benutzername zu kurz")
        benutzername = input("Gib deinen neuen Benutzernamen ein:")
    # while Benutzername in Liste von allen user | ihr die Liste von allen User einfügen, darf nicht den gleichen Usernamen haben. 
    print("Passwort muss mindest 6 Zeichen lang sein")
    passwort = input("Gib dein neues Passwort ein:")
    while len(passwort) <= 6: #Schleife damit das Passwort mindest sechs Zeichen lang ist. 
        print("Passwort zu kurz")
        passwort = input("Gib dein neues Passwort ein:")
    print("Benutzer erstellt und Startguthaben von 100 CHF zugewiesen")
    guthaben = 100
    spieler = [benutzername, passwort, guthaben, 0, 0, 0] #Eine neue Variabl erstellen, damit ich dies mit einem for einfügen kann. Die drei 0 erstellen, werden später angepasst.
    with open(spiel_datei, 'a', encoding="utf-8") as file:
        for wert in spieler:
            file.write(str(wert) + ",")
        file.write("\n")
    #Erstellt Werte in Datei eintragen. Nötige werde in string umwandeln. 
    return(benutzername, passwort, guthaben)
registrieren()

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