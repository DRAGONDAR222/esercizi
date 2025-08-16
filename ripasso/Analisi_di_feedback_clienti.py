'''Scrivi una funzione analizza_feedback(feedback: list[str]) -> dict che:

    Riceve una lista di stringhe, ogni stringa è un commento di un cliente.

    Conta quante volte appaiono parole positive e negative (date sotto).

    Restituisce un dizionario con:

        'totale_commenti': numero totale di commenti,

        'positivi': numero di commenti con almeno una parola positiva,

        'negativi': numero di commenti con almeno una parola negativa,

        'neutri': numero di commenti senza parole positive o negative,

        'parole_positive_usate': dizionario con le parole positive e quante volte appaiono in totale,

        'parole_negative_usate': dizionario con le parole negative e quante volte appaiono in totale.

Parole positive (da cercare):

positivi = ['bene', 'ottimo', 'perfetto', 'fantastico', 'eccellente', 'positivo', 'consiglio']

Parole negative (da cercare):

negativi = ['male', 'scarso', 'pessimo', 'terribile', 'negativo', 'problema', 'difetto']

Requisiti:

    Le parole vanno cercate case-insensitive (es. “Ottimo”, “ottimo” uguale).

    Conta solo parole intere (es. “perfetto” conta, “perfettamente” no).

    Il conteggio delle parole usate è totale su tutta la lista (non per singolo commento).

    I commenti possono contenere più parole positive o negative.

    Un commento può essere sia positivo che negativo, in questo caso conta in entrambi.

    I commenti senza nessuna parola positiva o negativa sono neutrali.'''



positivi = ['bene', 'ottimo', 'perfetto', 'fantastico', 'eccellente', 'positivo', 'consiglio']

negativi = ['male', 'scarso', 'pessimo', 'terribile', 'negativo', 'problema', 'difetto']

def analizza_feedback(feedback: list[str]) -> dict:
    my_dict:dict = {'totale_commenti': 0,
    'positivi': 0,
    'negativi': 0,
    'neutri': 0,
    'parole_positive_usate': {},
    'parole_negative_usate': {}
}
    
    feedback_pulito: list[str] = []

    for frase in feedback:
        frase_pulita = ""  
        for carattere in frase:
            if carattere.isalpha() or carattere == ' ':
                frase_pulita += carattere
        feedback_pulito.append(frase_pulita.lower()) 


    for frase in feedback_pulito:
        commento:list[str] = frase.split(" ")

        parole_positive:int = 0
        parole_negative:int = 0

        for parola in commento:

            if parola in positivi:
                parole_positive += 1

                if parola in my_dict['parole_positive_usate']:
                    my_dict['parole_positive_usate'][parola] += 1
                else:
                    my_dict['parole_positive_usate'][parola] = 1


            if parola in negativi:
                parole_negative += 1

                if parola in my_dict['parole_negative_usate']:
                    my_dict['parole_negative_usate'][parola] += 1
                else:
                    my_dict['parole_negative_usate'][parola] = 1

        if parole_positive > 0:
            my_dict['positivi'] += 1
        if parole_negative > 0: 
            my_dict['negativi'] += 1
        if parole_negative == 0 and parole_positive == 0:
            my_dict['neutri'] += 1


    return my_dict


                