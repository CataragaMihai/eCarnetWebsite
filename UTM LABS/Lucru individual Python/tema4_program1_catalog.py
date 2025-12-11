# Program cu o lista de studenti, cu notele lor. Dupa calcularea mediei se determina statutul studentului 
from tema3_functii_simple import suma
import csv 

def calculare_medie(note):
    print('====Calcularea mediei===')
    return suma(note)/len(note)

def calculare_status(medie, nota_trecere: float = 5.0):
    print('====Determinarea statutului studentului în dependență de medie====')
    if medie >= nota_trecere:
        return "Statut: Admis"
    else:
        return "Statut: Respins"


nume_fisier = ''

def scriere_in_excel():
    '''
    Va primi o listă de dicționare cu keys:
    - 'nume'
    - 'note'
    Calculează media și statutul și salvează rezultatele într-un fișier CSV.
    '''
    with open(nume_fisier, "w", newline = "", encoding  = "utf-8") as f:
        writer = csv.writer(f)
        #pentru a scrie primul row