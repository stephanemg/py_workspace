class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self._lieu_residence = "Paris"

    def get_lieu_residence(self):
        print("On accede a l'attribut lieu de residence")
        return self._lieu_residence

    def set_lieu_residence(self, nouvelle_residence):
        print("Attention, il semble que {} demenage a {}".format(self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence

    lieu_residence = property(get_lieu_residence, set_lieu_residence)

if __name__ == "__main__":
    personne = Personne('stephane', 'martin')
    print ('Actuellement {} {} habite a {}'.format(personne.prenom, personne.nom, personne.lieu_residence))
    personne.lieu_residence = "Berlin"