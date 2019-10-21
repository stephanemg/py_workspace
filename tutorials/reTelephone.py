'''
Created on Nov 6, 2019

@author: steph
on verifie l'entrée d'un numéro de tel de cette forme :
0X[ -.]XX[ -.]XX[ -.]XX[ -.]XX
'''

import re
import unittest



class TestPattern(unittest.TestCase):
    
    def test_cas_nominal_sans_tirets(self):
        num = '0112233445'
        res = appliqueRE(num)
        self.assertTrue(res)
        
    def test_cas_nominal_avec_tirets(self):
        num = '01-12-23-34-45'
        res = appliqueRE(num)
        self.assertTrue(res)
        
    def test_cas_nominal_avec_points(self):
        num = '01.12.23.34.45'
        res = appliqueRE(num)
        self.assertTrue(res)
        
    def test_cas_nominal_avec_espaces(self):
        num = '01 12 23 34 45'
        res = appliqueRE(num)
        self.assertTrue(res)
        
    def test_cas_invalide_avec_un_caractere_texte(self):
        num = '0X 12 23 34 45'
        res = appliqueRE(num)
        self.assertFalse(res)


pattern = '^0[0-9]([ -.]?[0-9]{2}){4}$'

def inputTelNumber():
    print ('entrez le numéro de téléphone :')
    return input()

def appliqueRE(param):
    if re.match(pattern, param) is not None:
        return True
    else:
        return False
    
#tests



if __name__ == '__main__':
    unittest.main()
    '''
    v = inputTelNumber()
    if appliqueRE(v) == True:
        print('Numéro ok')
    else:
        print ('Numéro incorrect')
    
'''