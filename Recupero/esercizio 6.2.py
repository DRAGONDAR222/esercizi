''' 
Scrivere un programma in Python che legga dall’utente una serie di nomi di persona (stringhe). L'inserimento dei nomi deve terminare quando l’utente inserisce un nome già inserito in precedenza, oppure sono stati inseriti 30 nomi distinti. Inoltre, si deve porre il vincolo che ciascun nome sia una stringa di lunghezza inferiore a 20 caratteri e che non venga inserita una stringa vuota.

Al termine dell'inserimento, il programma deve:
- stampare quanti nomi sono stati inseriti in totale;
- stampare il nome più lungo tra quelli inseriti;
- stampare la lunghezza del nome più lungo.

Se ci sono più nomi con la stessa lunghezza massima, puoi scegliere uno qualsiasi tra quelli più lunghi.

Esempio:
Inserisci un nome: Dora
Inserisci un nome: Marcella
Inserisci un nome: Teresa
Inserisci un nome: Valentina
Inserisci un nome: Dora
 
Hai inserito 4 nomi distinti.
Il più lungo è Valentina con 9 caratteri.
'''


def stampa_nomi() -> None:

    names: list[str] = []
    longest_name: str = ''

    while True:

        name: str = input('Inserisci un nome\n').strip()
        longest_name = name if len(name) >= len(longest_name) else longest_name

        if name and len(name) < 20:
            if name in names or len(names) >= 30:
                print(f'Hai inserito {len(names)} distinti.')
                print(f'Il più lungo è {longest_name} con {len(longest_name)} caratteri.')
                return
            
            else:
                names.append(name)
        else:
            print('Nome inserito non valido => assicurati che non sia vuoto o più lungo di 20 caratteri')