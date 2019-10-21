'''
Created on Nov 2, 2019

@author: steph
'''
def decorateurParametre(param):
    def monDecorateur(fonction):
        def fonction2():
            print ('fonction 2 est appelée avec le param : ', param)
            return param
        return fonction2
    return monDecorateur
    
@decorateurParametre(5)
def fonction():
    print('fonction appelée')
    


if __name__ == '__main__':
    fonction()