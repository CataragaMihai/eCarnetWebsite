#Exercițiu de sinteză

#Scrieți un program care:

#permite utilizatorului să aleagă tipul ecuației (gradul I sau II) printr-un meniu (if/elif),
#rezolvă ecuația aleasă apelând logica implementată anterior,
#repetă meniul până când utilizatorul alege opțiunea „ieșire” (folosind while).

def ecuatie_grad_I():
 a = float(input("Introduceți coeficientul a: "))
 b = float(input("Introduceți coeficientul b: "))
 if a != 0:
    x = -b / a
    if x == 0:
        x = 0
        print("Soluția ecuației este: x =", x)    
 elif b == 0:
    print("Ecuația are infinite soluții.")
 else:
   print("Ecuația nu are soluție.")

def ecuatie_grad_II():
 a = float(input("Introduceți coeficientul a: "))
 b = float(input("Introduceți coeficientul b: "))
 c = float(input("Introduceți coeficientul c: "))
 if a == 0:
    if b != 0:
        x = -c / b
        if x == 0:
            x = 0
        print("Ecuația este de gradul I. Soluția ecuației este: x =", x)
    elif c == 0:
        print("Ecuația are infinite soluții.")
    else:
        print("Ecuația nu are soluție.")

 else:
    D = b**2 - 4*a*c
    print("Discriminantul D =", D)
    if D < 0:
        print("Ecuația nu are soluții reale.")
    elif D == 0:
        x = -b / (2*a)
        if x == 0:
            x = 0
        print("Ecuația are o soluție dublă: x =", x)
    else:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        if x1 == 0:
            x1 = 0
        if x2 == 0:
            x2 = 0
        print("Ecuația are două soluții distincte: x1 =", x1, "și x2 =", x2)

while True:
    print("\nMeniu:")
    print("1. Rezolvă o ecuație de gradul I (ax + b = 0)")
    print("2. Rezolvă o ecuație de gradul II (ax^2 + bx + c = 0)")
    print("3. Ieșire")
    choice = input("Alegeți o opțiune (1/2/3): ")
    if choice == '1':
        ecuatie_grad_I()
    elif choice == '2':
        ecuatie_grad_II()
    elif choice == '3':
        print("Ieșire din program.")
        break
    else:
        print("Opțiune invalidă. Vă rugăm să alegeți din nou.")
    