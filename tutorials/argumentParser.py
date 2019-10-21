'''
Created on Nov 27, 2019

@author: A507181
'''


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="le nombre à mettre au carré")
parser.add_argument("-v", "--verbose", action="store_true",
        help="augmente la verbosité")

parser.add_argument("-la", "--list_all", action="store_true",
        help="liste toutes les lignes")


args = parser.parse_args()

x = args.x
retour = x ** 2
if args.verbose:
    print("{} ^ 2 = {}".format(x, retour))
if args.list_all:
    print("active l'option list all")
else:
    print(retour)