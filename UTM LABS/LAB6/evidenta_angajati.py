# -> sageata asta este folosita cand arati ce tip de valoare returneaza o functie
# inherintace si polimorfism

class Angajat:
    def __init__(self, nume: str, functie: str, salariu: float):
        self.nume = nume
        self.functie = functie 
        self.salariu = salariu

    def afiseaza_info(self):
        print(f'Nume: {self.nume}; Functie: {self.functie}; Salariu: {self.salariu}')

    def actualizare_salariu(self, procent: float):
        factor = 1 + procent/100
        self.salariu *= factor

    def bonus(self) -> float:
        return self.salariu *0.05

    def salariu_total(self) -> float:
        return self.salariu + self.bonus()


class Manager(Angajat):
    def __init__(self, nume: str, functie: str, salariu: float):
        super().__init__(nume, functie, salariu)
        self.subordonati = []  # listă de obiecte Angajat (sau Manager)

    def adauga_subordonat(self, angajat: Angajat):
        self.subordonati.append(angajat)

    def bonus(self) -> float:
        bonus_baza = self.salariu * 0.10
        bonus_pe_subordonat = 200 * len(self.subordonati)
        return bonus_baza + bonus_pe_subordonat

    def afiseaza_info(self):
       print(f"Nume: {self.nume}, Funcție: {self.functie}, Salariu de bază: {self.salariu:.2f} lei,"
              f" Subordonați: {len(self.subordonati)}")


def calculeaza_salariu_total_personal(lista_persoane):
    total = 0
    for persoana in lista_persoane:
        total += persoana.salariu_total()
    return total


def afiseaza_ierarhia(lista_persoane):
    print("=== IERARHIA ANGAJAȚILOR ===")
    for persoana in lista_persoane:
        persoana.afiseaza_info()
        if isinstance(persoana, Manager):
            for sub in persoana.subordonati:
                print(f"   └─ Subordonat: {sub.nume} ({sub.functie})")


def main():
    # Creăm angajati
    a1 = Angajat("Mihai", "Programator", 15000)
    a2 = Angajat("Ana", "Tester", 12000)
    a3 = Angajat("Ion", "Administrator rețea", 13000)

    
    m1 = Manager("Maria", "Manager IT", 20000)
    m2 = Manager("Andrei", "Manager Proiect", 18000)


    m1.adauga_subordonat(a1)
    m1.adauga_subordonat(a2)
    m2.adauga_subordonat(a3)

    # marim salariul
    a1.actualizare_salariu(5)   
    m1.actualizare_salariu(10)  

    
    personal = [a1, a2, a3, m1, m2]

    # ierarhia
    afiseaza_ierarhia(personal)

    # Calculăm salariul total cu bonusurile
    total = calculeaza_salariu_total_personal(personal)
    print(f"\nSalariul total de plată (inclusiv bonusuri): {total:.2f} lei\n")

if __name__ == "__main__":
    main()