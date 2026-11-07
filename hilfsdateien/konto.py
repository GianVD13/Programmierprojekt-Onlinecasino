#import main
#from hilfsdateien  import daten

def registrieren ():
    Benutzername = input("Gib deinen neuen Benutzernamen ein:")
    while Benutzername == "":
        print("Benutzername darf nicht leer sein")
        Benutzername = input("Gib deinen neuen Benutzernamen ein:")
    # while Benutzername in Liste von allen user | ihr die Liste von allen User einfügen, darf nicht den gleichen Usernamen haben. 
    passwort = input("Gib dein neues Passwort ein:")
    passwort_länge = len(passwort)
    while passwort_länge <= 6:
        print("Passwort muss mindest 6 Zeichen lang sein")
        passwort = input("Gib dein neues Passwort ein:")
        passwort_länge = len(passwort)









registrieren()
    


        


