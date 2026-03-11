from models import *
import main
import os
import random
import time
from pymongo import MongoClient


equipe = []
ennemi = ""
vague = 0
value = 0



def pause():
    time.sleep(1.1)

def recup_pseudo():
    #global value
    while True:
        value = input("Veuillez y inscrire votre pseudonyme : ")
        if len(value) < 3 or len(value) > 20:
            print("\nVotre pseudo doit contenir entre 3 & 20 caractères..\n")
        else:
            return value
        
def afficher_perso():
    for i, personnage in enumerate(personnages, start=1):
        print(f"{i}. {personnage["nom"]} --- ATK : {personnage["ATK"]}, DEF : {personnage["DEF"]}, PV : {personnage["PV"]}")
            
def choisir_perso():
    #global equipe
    #equipe = []
    for i in range(3):
        os.system("cls")
        print(f"\nChoisissez votre personnage n°{i+1} : ")
        print("")
        afficher_perso()
        choix = main.recup_n_valide(1, len(personnages), "\nEntrer le numéro du personnage : ")
        equipe.append(personnages[choix-1])
        print(f"\nVous avez choisi : {personnages[choix-1]['nom']}")
        personnages.pop(choix-1)
    return equipe

def afficher_equipe(equipe):
    os.system("cls")
    print("\nVoici les stats de votre équipe :")
    for personnage in equipe:
        print(f"{personnage['nom']} - ATK: {personnage['ATK']}, DEF: {personnage['DEF']}, PV: {personnage['PV']}")

def choisir_ennemi():
    if ennemis == []:
        print(f"\n\n\n\n\n\n\nBRAVOOO, votre équipe à gagné à la manche {vague} !\n")
        pause()
        main.main()
    x = random.choice(ennemis)
    ennemis.remove(x)
    print(f"\n{x["nom"]} apparait --- ATK : {x["ATK"]}, DEF : {x["DEF"]}, PV : {x["PV"]}\n")
    return x  


def attaquer_ennemi(ennemi):
    #global equipier, equipe
    # si l'opps meurt l'equipe gagne
    while ennemi["PV"] >= 0:
        for equipier in equipe:
            # si l'opps tue le perso
            if equipier["PV"] <= 0:
                print(f"\nVotre {equipier["nom"]} est mort...\n")
                equipe.remove(equipier)
                break
            print(f"{equipier["nom"]} attaque {ennemi["nom"]} et lui inflige {equipier["ATK"]} de dégâts")
            ennemi["PV"] -= equipier["ATK"] 
            print(f"{ennemi["nom"]} à désormais {ennemi["PV"]} PV")
            pause()
        if ennemi["PV"] <= 0:
            print(f"\nVotre {equipier["nom"]} vient d'atomiser {ennemi["nom"]} !\n")
            pause()
            print("\n\nVous passez a la prochaine vague..\n")
            time.sleep(3)
            break
        # l'ennemi attaque un perso de l'equipe
        attaquer_perso()    

def ajouter_score():
    c = MongoClient("mongodb://localhost:27017")
    db = c.MonPy
    score = [{"pseudo" : value, "points" : vague}]
    s = db.scoreboards_db.insert_many(score)
    db.close

def attaquer_perso():

    ennemi = x

    # verifier que tt les membres de l'équipe soit vivant
    if mort():
        print(f"Vous avez perdu la partie à la partie à la manche {vague}...")
        ajouter_score()
        pause()
        input("\n\n\n\n\n\n\nAppuyez sur une touche pour revenir au menu...")
        main.main()

    # choisis un membre de l'équipe au hasard
    perso_a_attaquer = random.choice(equipe)
    # affiche qu'il va lui faire des degats
    print(f"\n{ennemi["nom"]} à choisit d'attaquer {perso_a_attaquer["nom"]} et lui inflige {ennemi['ATK']} dégâts !")
    # print(f"\n{perso_a_attaquer["nom"]} --- ATK : {perso_a_attaquer["ATK"]}, DEF : {perso_a_attaquer["DEF"]}, PV : {perso_a_attaquer["PV"]}")
    #on retire les pv au membre de l'équipe et affiche pv restants
    perso_a_attaquer["PV"] -= ennemi['ATK']
    print(f"\n{perso_a_attaquer["nom"]} à désormais {perso_a_attaquer["PV"]} PV\n")
    pause()
    
def mort():
    print("OUI")
    return equipe == []

def combat():
    #global ennemi
    #global vague
    vague = 0
    while True:
        # afficher le nombre de vague
        os.system("cls")
        vague+=1
        print(F"+++++++++++++++ Vague n°{vague} +++++++++++++++")

        # choisis un ennemi aléatoirement et l'affiche
        ennemi = choisir_ennemi()
        print(ennemi["nom"])

        # chaq perso de l'equipe attaq l'opps
        attaquer_ennemi(ennemi)
    
        #break # raccourcir le combat pr debug
    print(f"BRAVOOO, votre équipe à gagné la partie !!")
    ajouter_score()
    pause()
    input("\n\n\n\n\n\n\nAppuyez sur une touche pour revenir au menu...")
    main.main()




    # pour chaq vague faire combattre les perso de l'équipe contre des ennemis
    # si l'équipe gagne passer a la vague suivante
    # si l'équipe perd afficher le score et revenir au menu


