'''

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

carti = []
linii_ignorate = 0


try:
    f = open("carti.csv", "r", encoding="utf-8")
except FileNotFoundError:
    print("Eroare: fișierul 'carti.csv' nu a fost găsit.")
except PermissionError:
    print("Eroare: nu am permisiune să citesc fișierul 'carti.csv'.")
else:
    # dacă deschiderea a reușit, citim liniile
    with f:
        reader = csv.DictReader(f)
        for idx, linie in enumerate(reader, start=2):  # linia 2 = prima după header
            titlu = (linie.get("Titlu") or "").strip()
            autor = (linie.get("Autor") or "").strip()
            gen = (linie.get("Gen") or "").strip()
            an_str = (linie.get("An") or "").strip()

            # validare câmpuri necompletate
            if not titlu or not autor or not gen or not an_str:
                print(f"Avertizare: linia {idx} are câmpuri goale. Linia a fost ignorată.")
                linii_ignorate += 1
                continue

            # validare an (trebuie să fie număr întreg)
            try:
                an = int(an_str)
            except ValueError:
                print(f"Avertizare: anul este invalid la linia {idx}. Linia a fost ignorată.")
                linii_ignorate += 1
                continue

            # dacă totul e ok, adăugăm cartea în listă
            carti.append({
                "Titlu": titlu,
                "Autor": autor,
                "Gen": gen,
                "An": an
            })
finally:
    print("Finalizare operație citire fișier (try/except/else/finally).")

print(f"Cărți valide încărcate: {len(carti)}. Linii ignorate: {linii_ignorate}.\n")

# dacă nu s-a putut încărca nimic, nu are rost să continuăm
if not carti:
    print("Nu există cărți valide în colecție. Programul se oprește.")
else:
    genuri_unice = set()
    autori_carti = {}
    gen_numar = {}

    for carte in carti:
        titlu = carte["Titlu"]
        autor = carte["Autor"]
        gen = carte["Gen"]
        an = carte["An"]     # deja este int

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

    # interval de ani (poți lăsa așa sau poți cere de la tastatură)
    an_min = 1900
    an_max = 2000
    filtru = []
    for carte in carti:
        an = carte["An"]
        if an_min <= an <= an_max:
            filtru.append(carte)

    # === Scriem în filtru.json cu tratare de erori ===
    try:
        f = open("filtru.json", "w", encoding="utf-8")
        json.dump(filtru, f, indent=4, ensure_ascii=False)
        f.close()
        print("Fișierul 'filtru.json' a fost salvat cu succes.")
    except OSError as e:
        print(f"Eroare la scrierea fișierului 'filtru.json': {e}")

    # transformăm dicționarul într-o listă de perechi
    top_autori = []
    for autor in autori_carti:
        numar = len(autori_carti[autor])
        top_autori.append([autor, numar])

    # sortare descrescătoare după număr de cărți (păstrez bubble sort-ul tău)
    for i in range(len(top_autori) - 1):
        for j in range(i + 1, len(top_autori)):
            if top_autori[i][1] < top_autori[j][1]:
                aux = top_autori[i]
                top_autori[i] = top_autori[j]
                top_autori[j] = aux

    # === Scriem în top_autori.csv cu try/except ===
    try:
        f = open("top_autori.csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(f)
        writer.writerow(["Autor", "Numar_carti"])
        for autor, numar in top_autori:
            writer.writerow([autor, numar])
        f.close()
        print("Fișierul 'top_autori.csv' a fost salvat cu succes.")
    except OSError as e:
        print(f"Eroare la scrierea fișierului 'top_autori.csv': {e}")

    # === STATISTICI ===
    total_carti = len(carti)
    numar_genuri = len(genuri_unice)

    if top_autori:
        autor_top = top_autori[0][0]
        numar_top = top_autori[0][1]
    else:
        autor_top = "N/A"
        numar_top = 0

    print("\n=== STATISTICI ===")
    print("Total cărți:", total_carti)
    print("Genuri distincte:", numar_genuri, "->", genuri_unice)
    print("Autorul cu cele mai multe titluri:", autor_top, "cu", numar_top, "cărți\n")