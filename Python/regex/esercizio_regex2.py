'''2. Trova tutte le email in un testo
Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.

Esempio:

text = "Contattaci a info@azienda.com oppure support@help.org"
extract_emails(text)  # ['info@azienda.com', 'support@help.org']'''


import re

def extract_emails(text: str) -> list:
    return re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)     


testo = "Contattaci a info@example.com o support@mywebsite.org per maggiori informazioni."
print(extract_emails(testo))  
# Output: ['info@example.com', 'support@mywebsite.org']
