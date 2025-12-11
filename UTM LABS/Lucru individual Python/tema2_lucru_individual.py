import time as t 
import math as m
import random as r
'''
Exerciții cu if:
1. Determinam paritatea unui numar 
2. Determinam varsta potrivita
3. Determinam daca un numar este pozitiv, negativ sau zero
4. Determinam cel mai mare numar din trei numere 
5. Verificam daca o litera este o vocala 
'''

while True: 
    print('='*20, '5 exerciții simple cu if', '='*20)
    print('\nExercițiul 1:')
    # Ex1
    while True:
        try:
            num: int = int(input('\nIntroduceți un număr să determinăm dacă este par sau impar: '))
            break
        except ValueError:
            print("\nEroare: te rog introdu un număr întreg valid.\n")

    if num % 2 == 0:
        print('\nNumărul este par')
    else:
        print('\nNumărul este impar')

    print('='*40)


    # Ex2
    print('\nExercițiul 2:')

    print('\nHai să aflăm dacă ai vârsta potrivită pentru a conduce!')
    while True:
        try:
            varsta = int(input('\nIntroduceți vârsta: '))
            break
        except ValueError:
            print("\nEroare: te rog introdu un număr întreg valid.\n")

    if varsta < 10:
        print('\nEști prea tânăr să ai acces la calculator')
    elif varsta < 18:
        print('\nTrebuie să mai creșteți!')
    elif varsta > 90:
        print('Wow, esți bătrân, poți conduce totuși dăcă mai e fizic posibil')
    else:
        print('\nAi grijă la volan!')

    print('='*40)

    # Ex3
    print('\nExercițiul 3:')

    while True:
        try:
            numar = int(input('\nIntroduceți oricare număr doriți: '))
            break
        except ValueError:
            print("\nEroare: te rog introdu un număr întreg valid.\n")

    if numar > 0:
        print('\nEste un număr pozitiv\n')

    elif numar < 0:
        print('\nEste un număr negativ\n')

    else:
        print('\nNumărul este 0')

    print('='*40)

    # Ex 4
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

    # Ex 5
    print('\nExercițiul 5:')

    litera = input('\nIntroduceți o literă: ').lower()

    vocale = "aăâeioîu"

    if litera in vocale:
        print(f'\nLitera {litera} este o vocală\n')
    else:
        print(f'\nLitera {litera} nu este o vocală\n')


    t.sleep(1)
    # 5 exercitii cu for 
    print('='*20, '5 exerciții simple cu for loop', '='*20)


    '''
    Exerciții cu for loop:
    1. Suma primelor n numere 
    2. Afișează tabla înmulțirii pentru un număr
    3. Numără vocalele dintr-un cuvânt
    4. Afișează toate numerele pare între 1 și 100
    5. Afișarea primelor n pătrate perfecte
    '''

    # Ex1 
    print('\nExercițiul 1')

    ex1 =  int(input('\nIntroduceți numărul n de cifre pentru care vom calcula suma lor: '))

    suma = 0

    for i in range(1, ex1 +1):
        suma += int(i)

    print(f'\nSuma de la 1 la {ex1} este {suma}\n')

    print('='*40)

    # Ex2 
    print('\nExercițiul 2')
    print('\nVom afișa tabla înmulțirii pentru un număr')
    numarul  = int(input('\nIntroduceți numărul: '))

    result = 0

    for i in range(1,11):
        result = i * numarul
        print(f'{i} * {numarul} = {result}')

    print('='*40)

    # Ex3
    print('\nExercițiul 3')

    lista_vocale: str = "aăâeioîu"

    cuvant = input("\nIntroduceți un cuvânt și programul va număra vocalele: ").lower()

    nr_vocale = 0
    vocala = ''

    for litera in cuvant:
        if litera in lista_vocale:
            nr_vocale += 1

    for vocala in cuvant:
        if vocala in lista_vocale:
            print(f'Avem vocala "{vocala}"')

    print('\nNumărul de vocale este: ', nr_vocale)
    print('='*40)

    # Ex4
    print('\nExercițiul 4')
    print('\nCalculăm toate numerele pare între 1 si n!')

    limita = int(input('\nIntroduceți n: '))

    num = 0

    for num in range(1, limita + 1):
        if num % 2 == 0:
            print('Avem numărul par: ', num)

    print('\nExercițiu finalizat!\n')
    print('='*40)


    # Ex5
    print('\nExercițiul 5')

    print('\nHai să calculăm primele n numere pătrate perfecte!')
    prag = int(input("\nn = "))

    numar1 = 0 

    for numar1 in range(1, prag + 1):
        numar1 = m.pow(numar1,2)
        print(int(numar1))

    print('\nExercițiu finalizat!\n')

    t.sleep(1)
    # 5 exercitii cu while 
    print('='*20, '5 exerciții simple cu while', '='*20)
    
    '''
    Exerciții cu while 
    1. Numărat de la 1 la n
    2. Citim până se introduce un număr pozitiv
    3. Suma cifrelor unui număr
    4. Ghicirea numărului
    5. Descompunerea în cifre a unui număr
    '''

    # Ex1
    print('\nExercițiul 1:')

    print('\nHai să numărăm de la 1 până la n!')
    numar2 = int(input('\nIntroduceți n --> '))

    counting = 1

    while counting <= numar2:
        print(counting)
        counting += 1

    print('\nExercițiu finalizat!\n')
    print('='*40)
    
    # Ex2
    print('\nExercițiul 2:')
    print('\nVom continua să întrebăm aceeași întrebare până veți introduce un număr negativ.')
    positive = int(input(('\nIntroduceți un număr --> ')))

    while positive > 0:
        positive = int(input(('\nIntroduceți un număr --> ')))

    print('\nExercițiu finalizat!\n')
    print('='*40)

    # Ex3
    print('\nExercițiul 3:')

    print('\nIntroduceți un număr din cel puțin două cifre.')
    calc = int(input('\nNumărul --> '))

    if calc <= 9:
        print(f'\nAi introdus o singură cifră, suma cifrelor numărului {calc} este {calc}\n')

    else:
        suma: int = 0
        calc1 = calc 
        while calc > 0:
            last_digit = calc % 10
            calc =  calc // 10
            suma += last_digit

        print(f'\nSuma cifrelor numărului {calc1} este {suma}\n')
   
    print('\nExercițiu finalizat!\n')
    print('='*40)

    # Ex4
    print('\nExercițiul 4:')
    print('\nVei ghici un număr din intervalul 1 și n')
    cap = int(input('\nIntroduceți n --> '))

    print('-'*40)
    random_num = r.randint(1, cap)
    print(f'\nS-a generat un număr random din intervalul (1, {cap}.')
    guess = int(input('\nGhiciți numărul --> '))

    while guess != random_num:
        print('Ai ghicit greșit, încearcă din nou!')
        guess = int(input('Ghiciți numărul --> '))

    print(f'\nBravo, ai ghicit! Numărul era {random_num}')

    print('\nExercițiu finalizat!\n')
    print('='*40)

     # Ex5
    print('\nExercițiul 5:')
    print('\nHai să descompunem în cifre un număr n')
    last_num = int(input('\nIntroduceți n --> '))
    print(f'\nNumărul: {last_num}')
    digits = 0

    while last_num > 0:
        digits = last_num % 10
        print(f'Cifra {digits}')
        last_num = last_num // 10

    print('\nExercițiu finalizat!\n')
    print('='*40)

    print('\nAi terminat cu succes toate exercțiile!')
    print('-'*40)

    choice = input('\nDoriți sa reluați exercițiille? (Da/Nu) --> ').strip().lower()
    if choice == 'da':
        break_loop = False
        continue
    elif choice == 'nu':
        break_loop = True
        break
    else: 
        print('\nOpțiune invalidă, răspunde din nou! ')

    if break_loop:
        break
    else:
        continue