#Calculul perimetrului si al ariei unui triunghi. Fie a, b si c trei valori reale, care reprezintã lungimile laturilor unui triunghi. Scrieti un program care sã calculeze si sã afiseze perimetrul si aria triunghiului, iar apoi afiseaza rezultatele intr-un mod clar si bine structurat.

import math
import time

a = float(input ("Introduceti lungimea laturii a: "))
b = float(input ("Introduceti lungimea laturii b: "))
c = float (input ("Introduceti lungimea laturii c: "))
print("Laturile triunghiului sunt: a =", a, ", b =", b, ", c =", c, "Se calcueaza perimetrul si aria triunghiului.")

calcul_perimetru = a + b + c
semiperimetru = calcul_perimetru / 2
calcul_arie = math.sqrt(semiperimetru * (semiperimetru - a) * (semiperimetru - b) * (semiperimetru - c))
time.sleep(1)
print("Perimetrul triunghiului este: ", calcul_perimetru)
time.sleep(1)
print("Aria triunghiului este: ", calcul_arie)
print ("Program incheiat.")
