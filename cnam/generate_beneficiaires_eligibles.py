import csv
import random
import string
from datetime import date

#fichier des beneficiaires eligibles


def generate_code_grand_regime():
    'genere un code grand regime de 2 digits'
    return ''.join(random.choice('123456789') for x in range(2))

def generate_code_caisse_rattachement():
    'genere un code caisse de 3 digits'
    return ''.join(random.choice(string.digits) for x in range(3))

def generate_code_centre_rattachement():
    'genere un code centre de rattachement de 4 caracteres'
    return ''.join(random.choice(string.digits) for x in range(4))

def generate_date_naissance():
    'genere une date de naissance au format jj/mm/aaaa'
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day.strftime("%d/%m/%Y")

def generate_rang_naissance():
    'genere un rang de naissance de 1 caractere'
    return ''.join(random.choice(string.digits) for x in range(1))

def random_nir_generator(size=13, chars=string.digits):
    b=[str(random.choice([1,2]))]
    return ''.join(b) + ''.join(random.choice(string.digits) for x in range(size-1))

with open('./beneficiaires_eligibles.csv', 'w', newline='') as csvfile:
    i=0
    while (i < 200):
        filewriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([generate_code_grand_regime(), generate_code_caisse_rattachement(),
        generate_code_centre_rattachement(), random_nir_generator(), generate_date_naissance(),
        generate_rang_naissance(), random_nir_generator()])
        i += 1
