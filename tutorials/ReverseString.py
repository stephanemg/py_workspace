'''
Created on Oct 31, 2019

@author: steph
'''
class ReverseString(str):
    '''
    classe string avec un iterateur qui parcours la chaine de droite a gauche
    '''
    def __iter__(self):
        '''
        on renvoie un iterateur parcourant de droite a gauche
        '''
        return IterReverse(self)
    
class IterReverse:
    '''
    un itérateur parcourant la chaine de la derniere au premier element
    '''
    def __init__(self, chaineAParcourir):
        '''
        On se positionne a la fin de la chaine a parcourir
        '''
        self.chaineAParcourir = chaineAParcourir
        self.position = len(chaineAParcourir)
        
    def __next__(self):
        '''
        On retourne le caractere a gauche de la chaine pour la prochaine iteration
        si on est a la fin, on raise une exception StopOperation
        '''
        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.chaineAParcourir[self.position]
    
if __name__ == "__main__":
    rev = ReverseString('Steph')
    for l in rev:
        print(l)
    
        
        