def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Introduceti un numar pentru a-i calcula factorialul: "))
print("Factorialul numarului", n, "este:", factorial(n))