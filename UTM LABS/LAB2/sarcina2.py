# 2. Algoritmi și programe pentru ecuații

#2.1.    Ecuația de gradul I: ax+b=0

#Scrieți algoritmul utilizând diagrama de flux.
#Implementați programul Python care: citește coeficienții a și b, tratează separat cazurile a=0  și a≠0, 
#afișează soluțiile corecte (sau mesajele corespunzătoare).

#2.2.    Ecuația de gradul II: ax2+bx+c=0

#Scrieți algoritmul utilizând diagrama de flux.
#Implementați programul Python care: citește coeficienții a, b, c, verifică dacă ecuația este de gradul I (cazul a=0), 
#calculează și afișează discriminantul D=b2-4ac, determină soluțiile în funcție de valoarea lui D(<0, =0, >0).

#Ecuația de gradul I: ax+b=0

print(" Hai să rezolvăm o Ecuație de gradul I: ax + b = 0")
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

#Ecuația de gradul II: ax2+bx+c=0
print("\n Acum hai să rezolvăm o Ecuație de gradul II: ax^2 + bx + c = 0")
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
