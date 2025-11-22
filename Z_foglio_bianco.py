class Movie:

    movie_id:str
    title:str
    director:str
    is_rented:bool

    def __init__(self,movie_id,title,director,is_rented):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self):

        if self.is_rented == False:
            self.is_rented = True

        else:
            print(f"Il film '{self.title}' è già noleggiato.")

    def return_movie(self):

        if self.is_rented == True:
            self.is_rented = False
        
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")


class Customer:

    customer_id:str
    name:str 
    rented_movies:list[Movie]

    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = []


    def rent_movie(self,movie:Movie):
        if movie in self.rented_movies:
            print(f"Il film '{movie.title}' è già noleggiato.")
        else:
            self.rented_movies.append(movie)


    def return_movie(self,movie:Movie):
        if movie in self.rented_movies:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
        else:
            self.rented_movies.remove(movie)

    
class VideoRentalStore:

    movies:dict
    customers:dict

    def __init__(self):
        self.movies = {}
        self.customers = {}


    def add_movie(self,movie_id: str, title: str, director: str):
        if movie_id not in self.movies:
            print(f"Il film con ID '{movie_id}' esiste già.")
        else:
            self.movies[movie_id]= Movie(movie_id,title,director)

    def register_customer(self,customer_id: str, name: str):
        if customer_id not in self.customers:
            print(f"Il cliente con ID '{customer_id}' è già registrato.")
        else:
            self.customers[customer_id]= Movie(customer_id,name)

    def rent_movie(self,customer_id: str, movie_id: str):
        if customer_id not in self.customers or movie_id not in self.movies:
            print("Cliente o film non trovato.")
        else:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)

    def return_movie(self,customer_id: str, movie_id: str):
        if customer_id not in self.customers or movie_id not in self.movies:
            print("Cliente o film non trovato.")
        else:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)

    def get_rented_movies(self,customer_id: str): 
        if customer_id not in self.customers:
            print("Cliente non trovato.")    
        else:
            customer = self.customers[customer_id]
            return customer.rented_movies

        
        
            


# da terminare