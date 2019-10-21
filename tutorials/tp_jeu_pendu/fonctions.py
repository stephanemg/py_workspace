
import pickle
import unittest
import donnees
import random
import os

class NomError(Exception):
    """exception pour un nom utilisateur saisi non conforme"""
    pass

class LettreError(Exception):
    """exception pour une lettre saisie non conforme (pas une lettre de l'alphabet)"""
    pass

def charger_scores():
    """cette fonction charge les scores enregistrés si le fichier existe
    on retourne un dictionnaire, soit l'objet unpickled soit un objet vide"""
    nom_fichier = 'scores.bin'
    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'rb') as scores:
            return pickle.load(scores)
    else:
        return {}


def enregistrer_scores(score):
    """cette fonction enregistre les scores dans le fichier mon_fichier_scores. Elle recoit en parametre
    le dictionnaire de scores a enregistrer"""
    with open("scores.bin", "wb") as scores:
        pickle.dump(score, scores)

def saisir_nom_utilisateur():
    "cette fonction retourne juste la saisie utilisateur"
    nom = input()
    return nom

def recup_nom_utilisateur():
    """chargée de récupérer le nom de l'utilisateur. teste la validité du nom qui doit comporter
    4 caracteres minimum, chiffres et lettres exclusivement. lance une exception NameError si echec"""
    print("Veuillez entrer un nom d'utilisateur, 4 caracteres minimum, chiffres et lettres exclusivement :")
    nom = saisir_nom_utilisateur()
    if len(nom) < 4 or not nom.isalnum():
        print('Ce nom est invalide')
        raise NomError
    return nom


def recup_lettre():
    """fonction chargée de recuperer une lettre saisie par l'utilisateur. Si la chaine saisie n'est pas 
    une lettre, on raise une NameError"""
    print('Veuillez saisir une lettre :')
    l = input()
    if not l.isalnum() or l is None:
        raise NomError
    return l


def choisir_mot():
    """fonction retourne le mot choisi dans la liste des mots liste_mots.utilise la fonction choice du
    module random"""
    return random.choice(donnees.liste_mots)


def recup_mot_masque(mot_complet, lettres_trouvees):
    """fonction qui retourne un mot masqué, tout ou en partie, en fonction :
    -du mot d'origine (type str)
    -des lettres déja trouvées (type list)

    on remplace les lettres non trouvées par *"""
    final = []
    for letter in mot_complet:
        try:
            index = lettres_trouvees.index(letter)
            final.append(letter)
        except ValueError:
            final.append('*')
    return "".join(final)

class AllTest(unittest.TestCase):
    """lancement global de toutes les fonctions de test du jeu"""
    def test_scores_nominal(self):
        """fonction de test du module scores, on genere un score pour un utilisateur fictif (steph),
        on l'enregistre et on le recharge"""
        scores = {"steph":5}
        enregistrer_scores(scores)
        scores = charger_scores()
        self.assertEqual(scores["steph"], 5)


    def test_choisir_mot(self):
        "teste la fonction choisir_mot, verifie son cas nominal, donc retourne un mot non vide"
        mot = choisir_mot()
        self.assertIsNotNone(mot)

    def test_recup_mot_masque(self):
        """teste la fonction recup_mot_masque, avec un mot d'origine pendu et les lettres trouvées
        pd, le mot resutant devant etre p**d*"""
        mot = recup_mot_masque('pendu', 'pd')
        self.assertEqual(mot, 'p**d*')

if __name__ == '__main__':
    unittest.main()

