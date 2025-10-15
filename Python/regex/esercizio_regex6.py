'''6. Verifica un codice prodotto
Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.

Esempio:

check_product_code("PROD-9876-ZX")  # True
check_product_code("PROD-99-ZX")    # False'''


import re

def check_product_code(code) -> bool:
    return bool(re.fullmatch(r'PROD-\d{4}-[A-Z]{2}',code))   # il "bool()" permette di passare da None a False e...

print(check_product_code("PROD-9876-ZX"))  # True
print(check_product_code("PROD-99-ZX"))    # False
