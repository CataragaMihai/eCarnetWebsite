import math as m
import time 

num = int(input("Introduceti un numar pentru a-i calcula radicalul: "))
print("Radicalul numarului ", num, "este: ", m.sqrt(num))

time.sleep(1)
print("Calculam valoarea lui pi...")
time.sleep(1)
print("Valoarea lui pi este: ", m.pi)

time.sleep(1)

print("Introduceti doua numere pentru a ridica la putere sub forma x^y:")
x = int(input("x = "))
y = int(input("y = "))
print(x, "la puterea", y, "este: ", m.pow(x,y))