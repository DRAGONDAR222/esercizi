'''Una pioggia di lettere si stacca dal soffitto: conta i sussurri autentici ignorando il rumore delle luci e del metallo. Invoca `letter_count(text)` per restituire un dizionario con le occorrenze di ogni lettera alfabetica in minuscolo, ignorando simboli, numeri e spazi. Mantieni la firma e soddisfa i test.'''

def letter_count(text: str) -> dict[str,int]:
    my_dict: dict[str,int] = {}

    for lettera in text.lower():
        if lettera.isalpha():
            if lettera in my_dict:
                my_dict[lettera] += 1
            else:
                my_dict[lettera] = 1

    return my_dict
