#pour un nombre 3.99999999 affiche 3,999

import math

def affiche_flottant(nombre = 0):
    if type(nombre) is not float:
        raise TypeError("le paramètre attendu doit être un flottant")
    if nombre > 0:
        partie_entiere, partie_flottante = str(nombre).split('.')
        return ",".join([partie_entiere, partie_flottante[:3]])

#si le module est lancé en autonome
if __name__ == '__main__':
    print ('resultat : ', affiche_flottant(3.9999999))