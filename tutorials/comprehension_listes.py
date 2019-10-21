#tri de l'inventaire en fonction de la quantité de chaque fruit, du plus grand au plus petit

inventaire = [("pommes", 22),("melons", 4),("poires", 18),("fraises", 76),("prunes", 51),]

inventaire.sort(key= lambda x:x[1], reverse=True)

print('liste triée : ', inventaire)