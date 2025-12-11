 # Elaborarea a 3 funcții matematice un pic mai avansate 

# calcularea factorial

def factorial(n):
    result = 1
    i = 1 
    while i <= n:
        result *= i
        i+= 1
    return result 


def slicing(n):
    last_digit = 0
    sum = 0
    while n >0:
        last_digit = n % 10
        n = n //10 
        sum += last_digit
    return sum


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i<n:
        if n % i == 0:
            return f"\nNumărul {n} nu este prim."
        i+= 1
    return f"\nNumărul {n} este prim."
    
