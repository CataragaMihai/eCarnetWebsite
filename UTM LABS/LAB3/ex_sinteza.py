"""
Calcul factorial (folosind funcția recursivă).
Determinarea maximului a trei numere (funcție cu parametri și return).
Simulare aruncare zar (folosind random).
Afișarea datei curente (folosind datetime).
Ieșire din program.
Programul trebuie să se repete (folosind o buclă) până când utilizatorul alege opțiunea de ieșire.
"""

import random as r
from datetime import datetime as dt

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def maxim (a,b,c):
    calc = max(a,b,c)
    return calc

def aruncare_zar():
    zar = r.randint(1,6)
    return zar


while True:
    print("\nMeniu:")
    print("1. Calcul factorial")
    print("2. Determinarea maximului a trei numere")
    print("3. Simulare aruncare zar ")
    print("4. Afișarea datei curente")
    print("5. Ieșire")
    choice = input("Alegeți o opțiune (1/2/3/4/5): ")
    if choice == '1':
        n = int(input("Introduceti un numar pentru a-i calcula factorialul: "))
        print("Factorialul numarului", n, "este:", factorial(n))

    elif choice == '2':
        a =  int(input("Introduceti primul numar: "))
        b =  int(input("Introduceti al doilea numar: "))
        c =  int(input("Introduceti al treilea numar: "))
        print ("Cel mai mare numar este: ", maxim(a,b,c)) 
    
    elif choice == '3':
        n = int(input("De cate ori doriti sa aruncati zarul? "))
        for i in range(n):
            print("Aruncarea numarul ", i+1, "a zarului a dat: ", aruncare_zar())

    elif choice == '4':
        now = dt.now()
        print("Data si ora curenta este: ", now.strftime("%d-%m-%Y %H:%M:%S"))

    elif choice == '5':
        print("Ieșire din program. Mersi ca ai jucat cu mine!5\n")
        break
    else:
        print("Opțiune invalidă. Vă rugăm să alegeți din nou.")