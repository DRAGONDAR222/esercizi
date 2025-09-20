from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio


if __name__ == "__main__":
    # 1) Creiamo i film singolarmente e li teniamo in variabili
    die_hard = Azione(1, "Die Hard")
    mad_max = Azione(2, "Mad Max")
    john_wick = Azione(3, "John Wick")
    gladiator = Azione(4, "Gladiator")
    dark_knight = Azione(5, "The Dark Knight")
    the_mask = Commedia(6, "The Mask")
    scary_movie = Commedia(7, "Scary Movie")
    mr_bean = Commedia(8, "Mr. Bean")
    hangover = Commedia(9, "Una notte da leoni")
    godfather = Drama(10, "The Godfather")

    # 2) Creiamo la lista di film
    films = [
        die_hard, mad_max, john_wick, gladiator, dark_knight,
        the_mask, scary_movie, mr_bean, hangover, godfather
    ]

    # 3) Creiamo l'oggetto Noleggio
    noleggio = Noleggio(films)

    # 4) Stampiamo la lista iniziale
    print("\nFilm disponibili nel negozio inizialmente:")
    noleggio.printMovies()

    print("\nQuale film vuoi noleggiare?\n")

    # 5) Cliente 1 noleggia un primo film
    cliente1 = 101
    noleggio.rentAMovie(die_hard, cliente1)

    # 6) Cliente 1 noleggia un secondo film
    noleggio.rentAMovie(the_mask, cliente1)

    # 7) Cliente 2 prova a noleggiare lo stesso film già noleggiato (The Mask)
    cliente2 = 202
    noleggio.rentAMovie(the_mask, cliente2)

    # 8) Cliente 2 noleggia un altro film disponibile
    noleggio.rentAMovie(godfather, cliente2)

    # 9) Cliente 1 restituisce il secondo film (The Mask) dopo 4 giorni
    noleggio.giveBack(the_mask, cliente1, days=4)

    # 10) Stampiamo la lista aggiornata dei film disponibili
    print("\nFilm disponibili in negozio dopo i noleggi e i resi:")
    noleggio.printMovies()

    # 11) Stampiamo i film noleggiati dai clienti
    print("\nFilm attualmente noleggiati dal cliente 101:")
    noleggio.printRentMovies(cliente1)

    print("\nFilm attualmente noleggiati dal cliente 202:")
    noleggio.printRentMovies(cliente2)
