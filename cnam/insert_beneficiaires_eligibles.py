import csv
import random
import string
import time
from datetime import date, datetime, timedelta
from configparser import ConfigParser
import psycopg2
from xeger import Xeger

# inserer des beneficiaires eligibles, en etat a traiter dans la base

sql = '''INSERT INTO apcv_beneficiaire (nir_individu,nir_od,date_naissance,rang_naissance,
code_grand_regime,code_caisse,code_centre,date_creation,date_ineligibilite,
ref_flux_entrant,date_import_flux_entrant) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) returning beneficiaire_id '''

sql_etat_beneficiaire = '''INSERT INTO apcv_etat_beneficiaire (beneficiaire_id,etat_id, date_changement_etat) VALUES 
(%s,%s,%s) '''

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

 
def close_base(connection, cursor):    
    if(connection):
        connection.commit()
        cursor.close()
        connection.close()


   
    

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

 
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


def generate_date_creation():
    'genere une date de naissance au format jj/mm/aaaa'
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day.strftime("%Y-%m-%d")


def generate_rang_naissance():
    'genere un rang de naissance de 1 caractere'
    return random.randrange(1, 4, 1)

def fill_nirs_hash(params, nirs):
    ''' initialise la hashtable des nirs déja présents dans la base '''
    sql = "select nir_individu from apcv_beneficiaire"
    print ('adding nirs already in the database')
    with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                records = cur.fetchall()
                for row in records:
                  #  print ('adding nir : ' + row[0])
                    nirs[row[0]] = True
    print ('nirs added')               
    


def random_nir_generator(size=13, chars=string.digits):
    reg_nir = '^[0125678][0-9]{2}(0[1-9]|1[0-2]|[23][0-9]|4[0-2]|[5-9][0-9])([0-9][0-9]|2[aAbB])(00[1-9]|0[1-9][0-9]|[1-9][0-9]{2})(00[1-9]|0[1-9][0-9]|[1-9][0-9]{2})$'
    x = Xeger(limit=13)
    nir = x.xeger(reg_nir)
    #print ('nir genere : ' + nir)
    return nir
  #  b=[str(random.choice([1,2]))]
  #  return ''.join(b) + ''.join(random.choice(string.digits) for x in range(size-1))


if __name__ == '__main__':
    conn = None
    try:
        """ Connect to the PostgreSQL database server and return cursor"""
        # read connection parameters
        params = config()
        # init hashmap stockage des nirs
        nirs = {}
        fill_nirs_hash(params, nirs)
        # init commit interval
        commit_interval = 1000
        
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                N = 0
                while N < 2000000:
                    try:
                    #genererf donnees beneficiaire
                        nir_individu = random_nir_generator()
                        if nir_individu in nirs:
                            print ('nir ' + nir_individu + " déja existant")
                            continue
                        else:
                            nirs[nir_individu] = True
                            nir_od = nir_individu
                            date_naissance = generate_date_naissance()
                            rang_naissance = generate_rang_naissance()
                            code_grand_regime = generate_code_grand_regime()
                            code_caisse = generate_code_caisse_rattachement()
                            code_centre = generate_code_centre_rattachement()
                            date_creation = generate_date_creation()
                            date_ineligibilite = None
                            ref_flux_entrant = 'APCV_ENROLES_221_20191127.csv'
                            date_import_flux_entrant = date.today()
                                
                            #insertion beneficiaire
                            cur.execute(sql, (nir_individu, nir_od, date_naissance, rang_naissance,
                                        code_grand_regime, code_caisse, code_centre, date_creation, date_ineligibilite,
                                        ref_flux_entrant, date_import_flux_entrant,))
                            benef_id = cur.fetchone()[0]
                            #insertion apcv_etat_beneficiaire a traiter
                            cur.execute(sql_etat_beneficiaire, (str(benef_id), '1', datetime.now()))
                            #si le nir commence par 2, on le met en etat traité
                            #on attend 1 sec pour l'horodatage
                            if nir_individu[0] == '2':
                                cur.execute(sql_etat_beneficiaire, (str(benef_id), '2', datetime.now() + timedelta(seconds=1)))
                            N+=1
                            if N % commit_interval == 0:
                                print ("Actuellement " + str(N) + " bénéficiaires.")
                                conn.commit()
                    except (psycopg2.DatabaseError) as error:
                        PrintException()
                        continue
            
            
                close_base(conn, cur)
        
    except (Exception) as error:
        PrintException()
        close_base(conn, cur)

