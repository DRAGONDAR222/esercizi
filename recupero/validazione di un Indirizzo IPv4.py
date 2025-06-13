'''Validazione di un Indirizzo IPv4
Scrivi una funzione is_valid_ipv4(address: str) -> bool che determina se una
stringa è un indirizzo IPv4 valido. Un indirizzo IPv4 è composto da quattro numeri decimali
(ciascuno da 0 a 255) separati da punti (.). Gli zeri iniziali sono consentiti (ad esempio
192.168.001.001 è valido), ma ciascuna delle quattro parti deve essere compresa tra 0 e
255 e non deve contenere caratteri o spazi aggiuntivi.
Requisiti:
● Se non ci sono esattamente tre punti o non ci sono quattro parti numeriche,
restituisci False.
● Ciascuna parte deve contenere solo cifre (isdigit()) e, convertita in intero, deve
essere nel range [0,255][0,255][0,255].'''

import re

def is_valid_ipv4(address: str) -> bool:

    copia:list = address.split(".")
    for elemento in copia:
        
        if re.fullmatch(r"[A-Za-z]",elemento):
            return False
        else:
            if int(elemento) > 255 or int(elemento) < 0 or len(elemento) > 3:
              return False
            elif len(copia) != 4:
                return False

    punti:int = 0

    for elemento in address:
        if elemento == ".":
            punti+= 1
    

    if punti != 3:
        return False
    else:
        return True
    


print(is_valid_ipv4("192.168.0.1")) # True
print(is_valid_ipv4("255.255.255.255")) # True
print(is_valid_ipv4("256.100.10.1")) # False (256 è fuori range)
print(is_valid_ipv4("192.168.1")) # False (solo 3 parti)
print(is_valid_ipv4("192.168.1.a")) # False (parte non numerica)

        
           
        


