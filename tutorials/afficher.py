def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction chargée de reproduire le comportement de print.
    
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés. 
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :
    print(chaine, end='')"""

    # on convertit le tuple parametre en liste
    parametres = list(parametres)
    
    #on convertit tous les parametres en chaine

    for i, param in enumerate(parametres):
        parametres[i] = str(param)

    #on constitue la chaine finale a partir du separateur

    chaine = sep.join(parametres)

    #on ajoute le parametre de fin a la fin de la chaine

    chaine+= fin

    #affichage final de l'ensemble
    
    print(chaine)


#mode play du module
if __name__ == '__main__':
    afficher('stephane', 'martin', sep=' ', fin='\n')

