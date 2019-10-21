import csv
import random
import string
from datetime import date

#fichier des beneficiaires enrolés

def generate_date():
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    #format date jj/mm/aaaa
    return random_day.strftime("%d/%m/%Y")

def random_nir_generator(size=13, chars=string.digits):
    b=[str(random.choice([1,2]))]
   # a = ''.join(random.choice(string.digits) for x in range(size))
    a = ''.join(b) + ''.join(random.choice(string.digits) for x in range(size-1))
    return a

with open('./beneficiaires_enroles.csv', 'w', newline='') as csvfile:
    i=0
    while (i < 200):
        filewriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        rand = random_nir_generator()
        filewriter.writerow([rand, generate_date()])
        i += 1
