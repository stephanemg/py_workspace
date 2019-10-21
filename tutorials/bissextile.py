#test sur années bissextiles
import os

def testBissextile(annee):
    if annee % 400 == 0 or (annee % 100 != 0 and annee % 4 == 0):
        bissextile = True
    else:
        bissextile = False
    return bissextile

    
try:
    annee = int(input('Saisissez une année : '))
except ValueError:
    print("Erreur lors de la conversion de l'année")
else:
    bissextile = testBissextile(annee)
    if (bissextile == True):
        print('Bissextile')
    else:
        print('Non Bissextile')
finally:
    os.system("pause")


