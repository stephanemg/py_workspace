'''
Created on Oct 30, 2019

@author: steph
'''

class MonException(Exception):
    '''
    exception manuelle
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.message = params
        
    def __str__(self):
        return self.message
    
if __name__ == "__main__":
    try:
        raise MonException('ca marche pas')
    except MonException as err:
        print('exception levée')
        print(err)
        