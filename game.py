from models import *
import main
import os
import random



def combat():
    # afficher le nombre de vague
    i = 0
    while True:
        os.system("cls")
        i+=1
        print(F"+++++++++++++++ Vague n°{i} +++++++++++++++")
        ennemi = random.choice(ennemis)
        ennemis.remove(ennemi)
        print(f"\n{ennemi["nom"]} --- ATK : {ennemi["ATK"]}, DEF : {ennemi["DEF"]}, PV : {ennemi["PV"]}")

        break


    # pour chaq vague faire combattre les perso de l'équipe contre des ennemis
    # si l'équipe gagne passer a la vague suivante
    # si l'équipe perd afficher le score et revenir au menu

combat()
