'''list = [1,2,3,4]
tuple = (1,2,3,4)
set = {1,2,3,4}
dictionary = {
    1 : 'one',
    2 : 'two'
}

print(dictionary.get(1))'''

def calc(a,b,c):
    s = a + b + c
    avg = s / 3
    return s, avg

a = float(input(" a  = "))
b = float(input(" b  = "))
c = float(input(" c  = "))

s, avg = calc(a,b,c)
print(f"\nSuma este {s} si media aritmetica este {avg}\n")