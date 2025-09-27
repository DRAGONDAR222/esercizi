'''Crea un sistema di gestione di una libreria personale, in cui ogni libro ha un titolo, uno o più autori e un numero ISBN.
1. Classe LibraryManager:

Gestisce tutte le operazioni legate ai libri.
Attributi:

    books: dict[str, dict[str, list[str]]]
    Dizionario che ha per chiave il titolo del libro e per valore un dizionario con:

        "authors": lista di autori (list[str])

        "isbn": lista contenente un solo elemento, il numero ISBN (list[str])

Metodi:

    add_book(title: str, authors: list[str], isbn: str) -> dict | str
    Aggiunge un nuovo libro. Se il libro esiste già (cioè il titolo è già presente), restituisce:
    "Errore: il libro esiste già."
    Altrimenti, aggiunge il libro e restituisce solo il dizionario del nuovo libro.

    add_author(title: str, author: str) -> dict | str
    Aggiunge un autore a un libro esistente. Se il libro non esiste, restituisce "Errore: il libro non esiste."
    Se l’autore è già presente, restituisce "Errore: l'autore esiste già."

    remove_author(title: str, author: str) -> dict | str
    Rimuove un autore dal libro.
    Gestisce gli stessi errori del metodo precedente, incluso l’errore se l’autore non è nella lista.

    update_isbn(title: str, new_isbn: str) -> dict | str
    Aggiorna il numero ISBN del libro.
    Se il libro non esiste, restituisce "Errore: il libro non esiste."

    list_books() -> list[str]
    Restituisce la lista dei titoli di tutti i libri presenti.

    list_authors(title: str) -> list[str] | str
    Mostra gli autori di un libro specifico.
    Se il libro non esiste, restituisce "Errore: il libro non esiste."

    search_book_by_author(author: str) -> list[str] | str
    Cerca tutti i titoli di libri scritti da un autore specifico.
    Se nessun libro viene trovato, restituisce "Nessun libro trovato per questo autore."'''


class LibraryManager:
    def __init__(self):
        self.books: dict[str, dict[str, list[str]]] = {}

    def add_book(self,title: str, authors: list[str], isbn: str) -> dict | str:
        if title in self.books:
            return f"Errore: il libro esiste già."
        else:
            self.books[title] = {'authors':authors,'isbn':[isbn]}
            return {title:self.books[title]}
        
    def add_author(self,title: str, author: str) -> dict | str:
        if title in self.books:
            if author not in self.books[title]['authors']:
                self.books[title]['authors'].append(author)
                return {title:self.books[title]}
            else:
                return "Errore: l'autore esiste già."
        else: 
            return "Errore: il libro non esiste."
        
    def remove_author(self,title: str, author: str) -> dict | str:
        if title in self.books:
            if author in self.books[title]['authors']:
                self.books[title]['authors'].remove(author)
                return {title:self.books[title]}
            else:
                return "Errore: l'autore non esiste."
        else: 
            return "Errore: il libro non esiste."
        
    def update_isbn(self,title: str, new_isbn: str) -> dict | str:
        if title in self.books:
            self.books[title]['isbn'][0] = new_isbn
            return {title:self.books[title]}
        else:
            return "Errore: il libro non esiste."
        
    def list_books(self) -> list[str]:
        
        return [libro for libro in self.books]

    def list_authors(self,title: str) -> list[str] | str:
        if title in self.books:
            return [author for author in self.books[title]['authors']]
        else:
            return "Errore: il libro non esiste."

    def search_book_by_author(self,author: str) -> list[str] | str:
        lista_libri:list[str] = []
        for libro in self.books:
            if author in self.books[libro]['authors']:
                    lista_libri.append(libro)

        if lista_libri:
            return lista_libri
        return "Nessun libro trovato per questo autore."


