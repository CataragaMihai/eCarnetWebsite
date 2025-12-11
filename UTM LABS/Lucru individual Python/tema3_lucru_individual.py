#Crearea a minim 6 funcții proprii pentru calcule matematice și împărțirea codului în module separate.

import tema3_functii_simple as ts
import tema3_functii_avansat as ta

print('Prima parte: Rezolvarea de exerciții simple cu ajutorul funcțiilor!\n')

print('='*40)
print('\nCalculăm suma a două numere!\n')

num1 = int(input('Introduceti primul număr: '))
num2 = int(input('Introduceti al doilea număr: '))

rezultat =  ts.suma(num1, num2)
print(f'\nSuma lor este: {rezultat}')

print('='*40)
print('\nCalculăm media aritmetică a trei numere!\n')

num1 = int(input('\nIntroduceți primul număr: '))
num2 = int(input('Introduceți al doilea număr: '))
num3 = int(input('Introduceți al treilea număr: '))

media = ts.avg(num1, num2, num3)

print(f'\nMedia aritmetică a celor trei numere este: {media:.2f}')

print('='*40)
print('\nCalculăm media goemetrică a două numere!\n')

num1 = int(input('\nIntroduceți primul număr: '))
num2 = int(input('Introduceți al doilea număr: '))

media_geometrica = ts.geometric_avg(num1, num2)

print(f'\nMedia geometrică a celor două numere este: {media_geometrica:.2f}')
print('='*40)

print('\nA doua parte: Rezolvarea de exerciții mai complicate cu ajutorul funcțiilor!\n')
print('='*40)

print('\nCalculăm factorialul unui număr!\n')

num = int(input("Introduceti numărul: "))
answer = ta.factorial(num)
print(f'\nFactorilul este {answer}')

print('='*40)
print('\nCalculăm suma cifrelor unui număr!\n')

num = int(input("Introduceti numărul: "))
answer = ta.slicing(num)
print(f'\nSuma cifrelor este {answer}')

print('='*40)
print('\nVerificăm dacă un număr este prim sau nu!')

num = int(input("\nIntroduceti numărul: "))
answer = ta.is_prime(num)

print(answer)
print('='*40)
print('\nProgramul a luat sfârșit\n')