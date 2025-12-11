# Distance convertor 

km = float(input("Write down the ditance in km to convert it to miles: "))
m = float(input("Write down the ditance in m to convert it to kilometeres: "))

km_converted = km * 0.621371
m_converted = m * 1.609344

print(f"Result: {km}km in miles is --> {km_converted:.2f}")
print(f"Result: {m}m in kilometeres is --> {m_converted:.2f}")