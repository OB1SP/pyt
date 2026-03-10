import os
import time
from models import *
import game
from pymongo import MongoClient




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

def lancer_jeu():
    # dmd pseudo
    pseudo = game.recup_pseudo()
    # afficher personnages
    
    # choisir 3 perso > equipe
    equipe = game.choisir_perso()

    # afficher equipe
    game.afficher_equipe(equipe)
    time.sleep(3.5)

    # lancer combat
    game.combat()

def aff_score():
    c = MongoClient("mongodb://localhost:27017")
    db = c.MonPy
    r = db.scoreboard.find()
    for s in r:
        print(s)

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
        print("Bye bye looser")
        exit()

if __name__ == "__main__":
    main()