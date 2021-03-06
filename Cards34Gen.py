#by judi_Co
author = "judi_Co"
Version = "1.2"

import random

#==========================================
#dictionnaire des carte
#cards dictionary
Cards = {
    "As": ["As", 14],  
    "7": ["7", 7], 
    "8": ["8", 8], 
    "9": ["9", 9], 
    "10": ["10", 10], 
    "Valet": ["Valet", 11], 
    "Dame": ["Dame", 12], 
    "Roi": ["Roi", 13]
}

jokersCards = {"Jokers1": ["Jokers", 15], "Jokers2": ["Jokers", 15]}

#==========================================
#initialisation des liste de carte
#cards liste init
def piocheD(jokers=False, Cards=Cards):
    Piques = {}
    for cle, Valeur in Cards.items():
        Piques[f"{cle} de Piques"] = Valeur

    Carreaux = {}
    for cle, Valeur in Cards.items():
        Carreaux[f"{cle} de Carreaux"] = Valeur

    Coeurs = {}
    for cle, Valeur in Cards.items():
        Coeurs[f"{cle} de Coeurs"] = Valeur

    Tréfles = {}
    for cle, Valeur in Cards.items():
        Tréfles[f"{cle} de Tréfles"] = Valeur


    #==========================================
    #Pile de cartes
    #Stack of cards
    Pile = {}

    Pile.update(Piques)
    Pile.update(Carreaux)
    Pile.update(Coeurs)
    Pile.update(Tréfles)
    if jokers == True:
        Pile.update(jokersCards)

    #==========================================
    #mélanger la pile de carte
    #shuffle cards
    Keys = list(Pile.keys())
    random.shuffle(Keys)
    pioche = {}
    for key in Keys:
        pioche.update({key:Pile[key]})
    return pioche

#==========================================
#afficher les carte
#cards display
def piocheL(jocker=False, pioche = piocheD()):
    if jocker == True:
        pioche = piocheD(True)
    for cle in pioche.keys():
        Cles = list(pioche)
    return Cles

#===============================
def piocheLD(jocker=False,pioche=piocheD()):
    if jocker == True:
        pioche = piocheD(True)
    D = pioche
    for L in pioche.keys():
        L = list(pioche)

    return L, D

#==========================================
#ajouter True en variable dans les appelle de fonction pour ajouter les jocker
#add True as a variable in the function calls to add the wildcards

#stocker les cartes
#stock cards
#Liste = piocheL()
#Liste = piocheL(True)
#dictionnaire = piocheD()
#dictionnaire = piocheD(True)
#List, dic = piocheLD()
#List, dic = piocheLD(True)

#afficher les cartes sous forme de Liste
#display maps in List form
#print(piocheL())
#print(piocheL(True))

#afficher les cartes sous forme de dictionnaire
#display maps in dictionary form
#print(piocheD())
#print(piocheD(True))

#piocheLD() retourne à une liste et un dictionnaire identiques
#piocheLD() return to an identical list and dictionary
#print(piocheDl())        #no arg = list and dictionary
#print(piocheLD()[0])     #[0] = List
#print(piocheLD()[1])     #[1] = dictionary
#print(piocheLD(True))    #no arg and True = list, dictionary and jocker
#print(piocheLD(True)[0]) #[0] and True = list and jocker
#print(piocheLD(True)[1]) #[1] and True = dictionary and jocker

#==========================================
