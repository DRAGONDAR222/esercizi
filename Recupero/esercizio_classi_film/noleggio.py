from movie_genre import Azione
from movie_genre import Commedia
from movie_genre import Drama

class Noleggio:

    __film_list:list[Azione|Commedia|Drama] 
    __rented_film:dict[int,list[Azione|Commedia|Drama]]

    def __init__(self,film_list:list[Azione|Commedia|Drama] ):
        self.__rented_film = {}
        self.__film_list = film_list


    def isAvailable(self,film:Azione|Commedia|Drama) -> bool:
        if film in self.__film_list:
            print(f'il film scelto è disponibile:{film.getTitle()}!')
            return True
        else:
            print(f'il film scelto non è disponibile:{film.getTitle()}!')
            return False
        

    def rentAMovie(self,film:Azione|Commedia|Drama,clientID:int) -> None:
        self.__rented_film[clientID] = []
       
        if film in self.__film_list:
            self.__film_list.remove(film)

            self.__rented_film[clientID].append(film)

            print(f'Il cliente {clientID} ha noleggiato {film.getTitle()}!')

        else:
            print(f' Non è possibile nolegiare il film {film.getTitle()}!')


    def giveBack(self,film:Azione|Commedia|Drama,clientID:int,days:int) -> None:
        
        self.__rented_film[clientID].remove(film)
        self.__film_list.append(film)

        penale:int = film.calcolaPenaleRitardo(days)

        print(f'Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penale} euro!')


    def printMovies(self) -> None:
        for film in self.__film_list:
            print(f'{film.getTitle()} - {film.getGenere()} -')

    
    def printRentMovies(self, clientID:int) -> None:
        for film in self.__rented_film[clientID]:
            print(f'{film.getTitle()} - {film.getGenere()}')

