'''
Created on Nov 5, 2019

@author: steph
'''

def generic_function(**params):
    for i in enumerate(params):
        print('parametre passé : ', i)
        print('la variable est :', i[0])
        print('le contenu est :', i[1])

if __name__ == '__main__':
    generic_function(test = 5, prenom = 'steph')