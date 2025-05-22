'''Exercise 3: Library Management System 
Create a Book class containing the following attributes: title, author, isbn. The book class must contains the following methods:

__str__, method to return a string representation of the book.

from_string, a class method to create a Book instance from a string in the format "title, author, isbn". It means that you must use the class reference cls to create a new object of the Book class using a string.

Example: 
book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book_str)
In this case, divina_commedia should be an instance of the Book class with:

title = "La Divina Commedia"

author = "D. Alighieri"

isbn = "999000666"

Create a Member class with the following attributes: name, member_id, borrowed_books. The member class must contain the following methods:

borrow_book, to add a book to the borrowed_books list.

return_book, to remove a book from the borrowed_books list.

__str__, method to return a string representation of the member.

from_string, a class method to create a Member instance from a string in the format "name, member_id". It means that you must use the class reference cls to create a new object of the Member class using a string.

Create a Library class with the following attributes: books, members, total_books (i.e., a class attribute to keep track of the total number of Book instances). The library class must contain the following methods:

add_book, to add a book to the library and increment total_books.

remove_book, to remove a book from the library and decrement total_books.

register_member, to add a member to the library.

lend_book, to lend a book to a member. It should check if the book is available and if the member is registered.

__str__, method to return a string representation of the library with the list of books and members.

library_statistics,  a class method to print the total number of books.

Finally, write a simple driver program. After creating a library, you should begin by creating instances of Book and Member. Wherever appropriate, use class methods (such as from_string) to instantiate objects from strings, improving clarity and modularity.

Once your objects are created, simulate some basic library operations:

Register new members to the library. This could involve adding Member objects to a collection maintained by the library.

Add books to the library’s collection.

Lend books to members. This will involve marking a book as borrowed and associating it with a specific member.

At each significant step, print the state of the library to track how it changes:

before lending any book,
after books have been lent.'''




class Book:
 
    def __init__(self,title:str, author:str, isbn:int):
        self.title:str = title
        self.author:str = author
        self.isbn:int = isbn

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    @classmethod
    def from_string(cls, book_string: str):
        title, author, isbn = book_string.split(", ")
        return cls(title, author, int(isbn))

class Member:

    def __init__(self,name:str, member_id:int):
        self.name:str = name
        self.member_id:int = member_id
        self.borrowed_books:list[Book] = []

    def borrow_book(self, new_book:Book) -> None:
        self.borrowed_books.append(new_book)

    def return_book(self,returning_book:Book) -> None:
        for book in self.borrowed_books:
            if book.isbn == returning_book.isbn:
                self.borrowed_books.remove(book)
                library.books.append(book)
                break

    def __str__(self):
        return f"Name: {self.name}, Member_id: {self.member_id}, Borrowed_books: {self.borrowed_books}"

    @classmethod
    def from_string(cls, member_string:str):
        name, member_id = member_string.split(", ")          
        return cls(name, int(member_id))

class Library:
    total_books:list[Book] = []
    
    def __init__(self):
        self.members:list[Member] = []
        self.books:list[Book] = []

    def add_book(self,new_book:Book) -> None:
        self.total_books.append(new_book)
        self.books.append(new_book)

    def remove_book(self,book_to_remove:Book) -> None:
        if book_to_remove in self.total_books:
            self.total_books.remove(book_to_remove)
            self.books.remove(book_to_remove)

    def register_member(self, new_member:Member) -> None:
        self.members.append(new_member)

    def lend_book(self,book_to_lend:Book, member_to_recive:Member) -> None:
        if book_to_lend in self.books and member_to_recive in self.members:
            member_to_recive.borrow_book(book_to_lend)
            self.books.remove(book_to_lend)
    
    def __str__(self) -> str:
        return f"List of books: {self.books}, List of members: {self.members}"
    
    @classmethod
    def library_statistics(cls) -> str:
        num_books:int = len(cls.total_books)
        return f"Total number of books: {num_books}"


# **Programma principale per testare il sistema di gestione della biblioteca**
if __name__ == "__main__":
    # Creazione della biblioteca
    library = Library()

    # Creazione di libri usando il metodo di classe from_string
    book1 = Book.from_string("La Divina Commedia, D. Alighieri, 999000666")
    book2 = Book.from_string("1984, George Orwell, 9780451524935")
    book3 = Book.from_string("Il Nome della Rosa, U. Eco, 123456789")

    # Creazione di membri usando il metodo di classe from_string
    member1 = Member.from_string("Mario Rossi, 1001")
    member2 = Member.from_string("Anna Bianchi, 1002")

    # Registrazione dei membri nella biblioteca
    library.register_member(member1)
    library.register_member(member2)

    # Aggiunta di libri alla collezione della biblioteca
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Stato iniziale della biblioteca
    print("\n📚 **Stato iniziale della biblioteca:**")
    print(f"Libri disponibili: {', '.join(book.title for book in library.books)}")
    print(f"Membri registrati: {', '.join(member.name for member in library.members)}")

    # Prestito di un libro a un membro
    library.lend_book(book1, member1)
    library.lend_book(book2, member2)

    # Stato della biblioteca dopo il prestito dei libri
    print("\n📖 **Stato della biblioteca dopo il prestito dei libri:**")
    print(f"Libri disponibili: {', '.join(book.title for book in library.books)}")
    print(f"Libri presi in prestito da {member1.name}: {', '.join(book.title for book in member1.borrowed_books)}")
    print(f"Libri presi in prestito da {member2.name}: {', '.join(book.title for book in member2.borrowed_books)}")

    # Restituzione di un libro
    member1.return_book(book1)  

    # Stato della biblioteca dopo la restituzione di un libro
    print("\n🔄 **Stato della biblioteca dopo la restituzione di un libro:**")
    print(f"Libri disponibili: {', '.join(book.title for book in library.books)}")
    print(f"Libri presi in prestito da {member1.name}: {', '.join(book.title for book in member1.borrowed_books)}")

    # Visualizzazione delle statistiche della biblioteca
    print("\n📊 **Statistiche della biblioteca:**")
    print(Library.library_statistics())



