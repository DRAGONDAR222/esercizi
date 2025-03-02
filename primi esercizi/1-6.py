'''1-6. Inserire all'interno di un dizionario il menu' di un ristorante, che viene specificato alla fine della traccia di questo esercizio.

Aggiungere in un nuovo dizionario chiamato ordine, un primo, un secondo, un contorno, una bevanda ed un dolce preso dal menu'. 

Stampare a schermo il conto totale che il cliente dovrà pagare. 

ITS Bakery Menu':

Pizza: 9.00 euro

Pasta: 10.50 euro

Zuppa : 7.00 euro

Hamburger: 15.50 euro

Cotoletta: 10.00 euro

Salmone: 20.20 euro

Patatine Fritte: 5.50 euro

Patate al forno: 5.50 euro

Verdura del giorno: 7.00 euro

Cheesecake: 6.00 euro

Tiramisu': 6.00 euro

Focaccia con Nutella: 6.00 euro

Coca Cola: 3.50 euro

Acqua: 1.50 euro

Vino: 5.00 euro'''



menù = {                                                  # i dizionari permettono l'associazione di un termine "str" ad un elemento numerico "float" e si inizializzano con le {}
    "pizza": 9.00,
    "pasta": 10.50,
    "zuppa": 7.00,
    "hamburger": 15.50,
    "cotoletta": 10.00,
    "salmone": 20.20,
    "patatine fritte": 5.50,
    "patate al forno": 5.50,
    "verdura del giorno": 7.00,
    "cheesecake": 6.00,
    "tiramisù": 6.00,
    "focaccia": 6.00,
    "coca cola": 3.50,
    "acqua": 1.50,
    "vino": 5.00 
}

ordine = {
    "pizza": 9.00,
    "hamburger": 15.50,
    "patatine fritte": 5.50,
    "cheesecake": 6.00,
    "coca cola": 3.50,
}

sum = ordine["cheesecake"] + ordine["coca cola"] + ordine["pizza"] + ordine["patatine fritte"] + ordine["hamburger"]            # il + somma i vari float 
print(sum , "euro")                                                                                                             # virgola permette di scrivere più elementi, nonchè di tipologie diverse
