import os
import time
from models import *
import game

def print_menu():
    print("""_____                              
  /     \ _____    ____ ______ ___.__.
 /  \ /  \\__  \  /    \\____ <   |  |
/    Y    \/ __ \|   |  \  |_> >___  |
\____|__  (____  /___|  /   __// ____|
        \/     \/     \/|__|   \/     """)
    print("1. Lancer le jeu")
    print("2. Voir les scores")
    print("3. Exit\n")

def recup_n_valide(min, max, message):
    while True:
        try:
            value = int(input(message))
            if value < min or value > max:
                print(f"La valeur doit être comprise en {min} & {max}.\n")
            else:
                return value
        except ValueError:
            print("La valeur donnée est invalide..\n")

def recup_pseudo():
    while True:
        value = input("Veuillez y inscrire votre pseudonyme : ")
        if len(value) < 3 or len(value) > 20:
            print("\nVotre pseudo doit contenir entre 3 & 20 caractères..\n")
        else:
            return value
        
def afficher_perso():
    for i, personnage in enumerate(personnages, start=1):
        print(f"\n {i}. {personnage["nom"]} --- ATK : {personnage["ATK"]}, DEF : {personnage["DEF"]}, PV : {personnage["PV"]}")
            
def choisir_perso():
    equipe = []
    for i in range(3):
        os.system("cls")
        afficher_perso()
        print(f"\nChoisissez votre personnage n°{i+1} : ")
        choix = recup_n_valide(1, len(personnages), "Entrer le numéro du personnage : ")
        equipe.append(personnages[choix-1])
        print(f"\nVous avez choisi : {personnages[choix-1]['nom']}")
        personnages.pop(choix-1)
    return equipe

def afficher_equipe(equipe):
    os.system("cls")
    print("\nVotre équipe se compose de :")
    for personnage in equipe:
        print(f"{personnage['nom']} - ATK: {personnage['ATK']}, DEF: {personnage['DEF']}, PV: {personnage['PV']}")

def lancer_jeu():
    # dmd pseudo
    pseudo = recup_pseudo()
    # afficher personnages
    
    # choisir 3 perso > equipe
    equipe = choisir_perso()

    # afficher equipe
    afficher_equipe(equipe)
    time.sleep(5)

    # lancer combat
    game.combat()
    


def aff_score():
    pass

def main():
    os.system("cls")
    print_menu()
    choix = recup_n_valide(1, 3, "Entrer dans le menu : ")
    if choix == 1:
        os.system("cls")
        lancer_jeu()
    elif choix == 2:
        os.system("cls")
        aff_score()
    else:
        pass

if __name__ == "__main__":
    main()