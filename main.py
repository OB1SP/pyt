import os
import time
import game
from models import *
from pymongo import MongoClient

def print_menu():
    print("""\n\n$$\      $$\                                               
$$$\    $$$ |                                              
$$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\       
$$\$$\$$ $$ | \____$$\ $$  __$$\ $$  __$$\ $$ |  $$ |      
$$ \$$$  $$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ |  $$ |      
$$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      
$$ | \_/ $$ |\$$$$$$$ |$$ |  $$ |$$$$$$$  |\$$$$$$$ |      
\__|     \__| \_______|\__|  \__|$$  ____/  \____$$ |      
                                 $$ |      $$\   $$ |      
                                 $$ |      \$$$$$$  |      
                                 \__|       \______/       \n\n\n\n\n""")
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

    print("Voici le scoreboards des pro joeurs : ")
    scores = refresh_score()
    for i, score in enumerate(scores, start=1):
        time.sleep(.3)
        print(f"{i}. {score["pseudo"]} : {score["points"]} points")
        
    input("\n\n\n\n\n\n\nAppuyez sur une touche pour revenir au menu...")
    main()

def main():
    os.system("cls")
    print_menu()
    choix = recup_n_valide(1, 3, "\n\n\n\n\n\nEntrer dans le menu : ")
    if choix == 1:
        os.system("cls")
        lancer_jeu()
    elif choix == 2:
        os.system("cls")
        aff_score()
    else:
        print("\n\n\n\n\n\nBye bye looser")
        exit()

if __name__ == "__main__":
    main()