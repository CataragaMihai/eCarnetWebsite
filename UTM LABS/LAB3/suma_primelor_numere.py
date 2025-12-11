def suma():
    total = 0 
    n = int(input("Introduceti un numar n pentru a calcula suma primelor n numere naturale: "))
    if n<0:
        print("Numarul trebuie sa fie pozitiv")
        return
    for i in range(1,n+1):
        total +=i
    print("Suma primelor", n, "numere naturale este: ", total)
suma()