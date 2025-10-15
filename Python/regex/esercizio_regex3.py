'''3. Sostituisci tutti i numeri con '###'
Scrivi una funzione mask_numbers(text) che sostituisce tutte le sequenze di cifre con ###.

Esempio:

text = "Il codice è 12345 e la data è 2025."
mask_numbers(text)  # "Il codice è ### e la data è ###."'''


import re

def mask_numbers(text) -> str:
    return re.sub(r"\d", "#", text)

testo:str = "Il codice è 12345 e la data è 2025"
print(mask_numbers(testo))  # "Il codice è ### e la data è ###