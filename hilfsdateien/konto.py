#import main
#from hilfsdateien  import daten

def registrieren ():
    benutzername = input("Gib deinen neuen Benutzernamen ein:")
    while benutzername == "": #min. 2 bei Benutzername länge
        print("Benutzername darf nicht leer sein")
        benutzername = input("Gib deinen neuen Benutzernamen ein:")
    # while Benutzername in Liste von allen user | ihr die Liste von allen User einfügen, darf nicht den gleichen Usernamen haben. 
    passwort = ""
    while passwort_laenge <= 6:
        print("Passwort muss mindest 6 Zeichen lang sein")
        passwort = input("Gib dein neues Passwort ein:")
        passwort_laenge = len(passwort)
    print("Benutzer erstellt und Startguthaben von 100 CHF zugewiesen")
    startguthaben = 100
    return(benutzername, passwort, startguthaben)
registrieren()
#user = {benutzernamen: passwort, startguthaben }

def login (): #Muss dann den User einfügen, aktuell noch nicht vorhanden
    benutzer_eingabe = input("Gib dein Benutzer ein:")
    passwort_eingabe = input("Gib dein passwort ein:")
    while benutzer_eingabe and passwort_eingabe not in "test": #Test mit dem User ersetzten. Dieser muss noch erstellt werden
        print("Login fehlgeschlagen, User oder Passwort falsch")
        benutzer_eingabe = input("Gib dein Benutzer ein:")
        passwort_eingabe = input("Gib dein passwort ein:")
    print("Login erfolgreich")
    return(benutzer_eingabe, passwort_eingabe)
    
login()

def statistik (): # Mit User ausfüllen, in diesem sind alle Spielerdaten gespeichert
   # print(user.(anzahl_spiele))
   # print (user.(Guthaben))
   return()