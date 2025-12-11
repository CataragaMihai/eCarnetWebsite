
print('Exercițiul 4:')

while True:
        try:
            num1 = int(input('\nIntroduceți primul număr: '))
            num2 = int(input('Introduceți al doilea număr: '))
            num3 = int(input('Introduceți al treilea număr: '))
            break
        except ValueError:
            print("\nEroare: te rog introdu un număr întreg valid.\n")


if num1 > num2 and num1 > num3:
        print('\nPrimul număr este cel mai mare')
elif num2 > num3 and num2 > num1:
        print('\nAl doilea număr este cel mai mare')
elif num1 == num2 == num3:
        print('\nNumerele sunt egale între ele')
        
else:
        print('\nAl treilea număr este cel mai mare')

print('='*40)