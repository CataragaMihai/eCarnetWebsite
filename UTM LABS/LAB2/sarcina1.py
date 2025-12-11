#1. Operații aritmetice

#Scrieți un program care:

#citește două numere și afișează: suma lor, produsul lor, maximul dintre ele.
#citește un număr și verifică dacă este par sau impar.
#afișează toate numerele de la 1 la n utilizând bucla for (unde  este citit de la tastatură).
#calculează suma numerelor de la 1 la n folosind bucla while.

import time 

#---------------Punctul 1-------------------

print ("Primul punct...")
time.sleep(1)

num_1 = float(input("Introduceți primul număr: "))
num_2 = float(input("Introduceți al doilea număr: "))

sum_num = num_1 + num_2
prod = num_1 * num_2
max_num = max(num_1, num_2)
print("Suma:", sum_num)
print("Produsul:", prod)
print("Maximul:", max_num)

#---------------Punctul 2-------------------

print ("Al doilea punct...")
time.sleep(1)
num = int(input("Introduceți un număr: "))
if num % 2 == 0:
    print("Numărul " ,num, "este par.")
else:
    print("Numărul " ,num, "este impar.")

#---------------Punctul 3-------------------

print ("Al treilea punct (for loop)... ")
time.sleep(1)

n = int(input("Introduceți număr n, adică câte numere se for afișa: "))
for i in range (1, n + 1):
    print(i)

#---------------Punctul 4-------------------

print ("Al patrulea punct (while loop)... ")
print ("Calculăm suma numerelor de la 1 la n (n =",n,")...")
time.sleep(1)

i = 1
suma = 0

while i <= n:
    suma = suma + i
    i = i + 1

print("Suma numerelor de la 1 la n este:", suma)
time.sleep(1)

#End message

print("Toate punctele au fost rezolvate cu succes!")