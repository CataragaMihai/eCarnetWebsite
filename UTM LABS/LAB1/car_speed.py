#Determinarea vitezei medii a unui automobil
distanta_km = float(input("Introduceți distanța parcursă (km): "))
timp_ore = float(input("Introduceți durata deplasării (ore): "))

viteza_ms = (distanta_km * 1000) / (timp_ore * 3600)
print("Viteza medie este:", viteza_ms, "m/s")


#prin functie 
def viteza_medie(distanta,timp):
    viteza = distanta / timp
    return viteza
    
    
distanta = float(input("Introduceți distanța parcursă (km): "))
timp = float(input("Introduceți durata deplasării (ore): "))
print("Viteza medie este:", viteza_medie(distanta*1000,timp*3600), "m/s")