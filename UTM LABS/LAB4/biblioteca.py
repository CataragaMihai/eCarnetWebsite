'''
Notițe:

#Arrays 

#Lists
my_list = [1, 2, 3, 4, 5]
# ---> ordered, mutable, can contain duplicates

#Sets
my_set = {1, 2, 3, 4, 5}
# ---> unordered, mutable, cannot contain duplicates

#Tuples
my_tuple = (1, 2, 3, 4, 5)
# ---> ordered, immutable, can contain duplicates

#Dictionaries
my_dictionary = {
    "Name": "Mihai",
    "Age": 19,
    "City": "Chisinau"
}
# ---> unordered, mutable, can contain duplicates

'''

import csv
import json

f = open("carti.csv", "r", encoding="utf-8")
reader = csv.DictReader(f)
carti = []
for linie in reader:
    carti.append(linie)
f.close()

genuri_unice = set()
autori_carti = {}
gen_numar = {}

for carte in carti:
    titlu = carte["Titlu"]
    autor = carte["Autor"]
    gen = carte["Gen"]
    an = int(carte["An"])

    # adăugăm genul în set
    genuri_unice.add(gen)

    # autor → listă cărți
    if autor not in autori_carti:
        autori_carti[autor] = []
    autori_carti[autor].append(titlu)

    # gen → număr cărți
    if gen not in gen_numar:
        gen_numar[gen] = 1
    else:
        gen_numar[gen] += 1

AN_MIN = 1900
AN_MAX = 2000
filtru = []
for carte in carti:
    an = int(carte["An"])
    if an >= AN_MIN and an <= AN_MAX:
        filtru.append(carte)

# Scrie în filtru.json
f = open("filtru.json", "w", encoding="utf-8")
json.dump(filtru, f, indent=4, ensure_ascii=False)
f.close()

# transformăm dicționarul într-o listă de perechi
top_autori = []
for autor in autori_carti:
    numar = len(autori_carti[autor])
    top_autori.append([autor, numar])

for i in range(len(top_autori) - 1):
    for j in range(i + 1, len(top_autori)):
        if top_autori[i][1] < top_autori[j][1]:
            aux = top_autori[i]
            top_autori[i] = top_autori[j]
            top_autori[j] = aux

# Scriem în top_autori.csv
f = open("top_autori.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(f)
writer.writerow(["Autor", "Numar_carti"])
for autor, numar in top_autori:
    writer.writerow([autor, numar])
f.close()

total_carti = len(carti)
numar_genuri = len(genuri_unice)
autor_top = top_autori[0][0]
numar_top = top_autori[0][1]

print("=== STATISTICI ===")
print("Total cărți:", total_carti)
print("Genuri distincte:", numar_genuri)
print("Autorul cu cele mai multe titluri:", autor_top, "cu", numar_top, "cărți\n")