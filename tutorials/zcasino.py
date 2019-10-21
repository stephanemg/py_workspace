#tp de jeu de roulette

import math
import random

#on lui donne 1000 euros pour commencer
argent = 1000

def lanceRoulette():
    """Fonction tirant un nombre entier aléatoire de 0 a 49
    """
    return random.randrange(0,51)

def mise(mise):
    gain = 0
    try:
        numero = int(input('Saisissez un numero : '))
        if numero < 1 or numero > 49:
            print ("Veuillez saisir un numero entre 1 et 49")
            return 0
        pairMise = True if numero % 2 == 0 else False
    except ValueError:
        print("Erreur lors de la saisie du numero misé")
    else:
        nombre = lanceRoulette()
        print ("Le numéro tiré est : " , nombre)
        pairNumero = True if nombre % 2 == 0 else False
        if numero == nombre:
            gain = mise * 3
            print ("Vous avez gagné : " , gain)
            return gain
        elif pairNumero == pairMise:
            gain  = math.ceil(mise / 2)
            print ("Vous avez gagné : " , gain)
            return gain
        else:
            print ("Vous n'avez rien gagné ! ")
            return 0
try:
    m = int(input('Saisissez une mise : '))
except ValueError:
    print("Erreur lors de la saisie de la mise")
else:
    while m > 0 or m > argent:
        gain = mise(m)
        if gain > 0:
            argent += gain
        else:
            argent -= m
        print ("Vous disposez maintenant de ", argent, " euros")
        if argent <= 0:
            print("vous etes ruiné ! C'est la fin de la partie")
            break
        m = int(input('Saisissez une mise : '))




    