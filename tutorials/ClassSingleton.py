'''
Created on Nov 4, 2019

@author: steph

'''

def singleton(classe_definie):
    instances = {}
    def get_instance():
        if classe_definie not in instances:
            #creation de premiere classe stockee dans dico instances
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance

@singleton
class Test:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print('Init ok')
        
        
if __name__ == "__main__":
    t = Test()
    f = Test()
    if t is f:
        print('egalité des deux classes')