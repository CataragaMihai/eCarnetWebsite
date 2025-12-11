#Simulam aruncarea unui zar cu libraria random
import random as r 


def aruncare_zar():
    zar = r.randint(1,6)
    return zar

n = int(input("De cate ori doriti sa aruncati zarul? "))
for i in range(n):
    print("Aruncarea numarul ", i+1, "a zarului a dat: ", aruncare_zar())

