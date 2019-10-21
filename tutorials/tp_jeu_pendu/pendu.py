import fonctions

nombre_coups_restants = 8

# on recupere le nom de l'utilisateur
nom = fonctions.recup_nom_utilisateur()

# on recupere les scores

scores = fonctions.charger_scores()

# si le fichier score existe, on recupere le score eventuel de l'utilisateur
score_utilisateur = 0

if scores != None:
    score_utilisateur = scores[nom]

print('Bienvenue au jeu du pendu,', nom, ', votre score actuel est de : ', score_utilisateur)

# on demarre le jeu, on tire un mot au hasard dans la table des mots
mot = fonctions.choisir_mot()

# on cree le mot actuel en cours de divination, en remplacant tous ses caracteres par *
mot_actuel = fonctions.recup_mot_masque(mot, '*')


lettres_trouvees = []

while True:
    # on demande a l'utilisateur de deviner une lettre du mot
    print('Le mot a deviner est : ', mot_actuel)
    print('Nombre de coups restants : ', nombre_coups_restants)
    try:
        l = fonctions.recup_lettre()
        # on verifie si la lettre est présente dans le mot en cours de divication
        if mot_actuel.find(l) != -1:
            # l'utilisateur a deja trouvé ces lettres, on decompte un coup et on l'avertit
            nombre_coups_restants -= 1
            print('Vous avez déja trouvé cette lettre, on continue')
            continue
        if mot.find(l) != -1:
            # l'utilisateur a trouvé une nouvelle lettre, on les demasque dans le mot actuel
            lettres_trouvees.append(l)
            mot_actuel = fonctions.recup_mot_masque(mot, lettres_trouvees)
            print('Vous avez trouvé une nouvelle lettre dans le mot : ', mot_actuel)
            # on teste si l'utilisateur a trouvé toutes les lettres
            if (mot_actuel.find('*') == -1):
                print('Vous avez gagné !')
                break
            else:
                continue
        else:
            # l'utilisateur n'a pas trouvé de nouvelle lettre, on descends son nombre de coups restants
            nombre_coups_restants -= 1
            if (nombre_coups_restants <= 0):
                print("Vous avez perdu !")
                break
            print('Echec ! On continue')

    except fonctions.NomError:
        continue

score_utilisateur += nombre_coups_restants
print('Votre score du jeu est de  : ', nombre_coups_restants)
print('Votre score utilisateur actualisé est de : ', score_utilisateur)
scores[nom] = score_utilisateur
# on enregistre le score utilisateur
fonctions.enregistrer_scores(scores)
