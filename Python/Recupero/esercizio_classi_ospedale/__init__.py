from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

if __name__ == "__main__":
    # Creo due dottori
    dottore1 = Dottore("Mario", "Rossi", "Pediatra", 100.0)
    dottore1.setAge(45)   # età valida > 30

    dottore2 = Dottore("Luigi", "Bianchi", "Cardiologo", 150.0)
    dottore2.setAge(50)   # età valida > 30

    # I dottori si presentano
    dottore1.doctorGreet()
    dottore2.doctorGreet()

    # Creo i pazienti
    paziente1 = Paziente("Anna", "Verdi", "P001")
    paziente2 = Paziente("Marco", "Neri", "P002")
    paziente3 = Paziente("Luca", "Gialli", "P003")
    paziente4 = Paziente("Sara", "Blu", "P004")

    lista_pazienti1 = [paziente1, paziente2, paziente3]  # 3 pazienti
    lista_pazienti2 = [paziente4]                        # 1 paziente

    # Creo le fatture
    fattura1 = Fattura(lista_pazienti1, dottore1)
    fattura2 = Fattura(lista_pazienti2, dottore2)

    # Stampo i salari iniziali
    print(f"\nSalario Dottore1: {fattura1.getSalary()} euro!")
    print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

    # Sposto un paziente da dottore1 a dottore2
    paziente_rimosso = fattura1.removePatient("P002")
    if paziente_rimosso:
        fattura2.addPatient(paziente_rimosso)

    # Stampo i salari aggiornati
    print(f"\nSalario Dottore1: {fattura1.getSalary()} euro!")
    print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

    # Guadagno totale dell'ospedale
    totale = fattura1.getSalary() + fattura2.getSalary()
    print(f"\nIn totale, l'ospedale ha incassato: {totale} euro!")
