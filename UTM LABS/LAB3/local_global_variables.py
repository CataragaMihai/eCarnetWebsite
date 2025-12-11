x = 2 #variabila globala 
#in conditie esete mentinat ca n este numarul de ordine după lista grupei, iar eu sunt numarul 2 pe lista)

def functie():
    x = 2 * 2 #variabila locala
    print("Valoarea variabilei locale x este: ", x)
functie()

print("Valoarea variabilei globale x este: ", x)