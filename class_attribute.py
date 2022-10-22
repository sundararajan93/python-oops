class Movie:

    id_counter = 1

    def __init__(self, name, rating):
        self.id = Movie.id_counter
        self.name = name
        self.rating = rating

        Movie.id_counter += 1

my_favorite_movie = Movie("Vikram", 4.8)
your_favorite_movie = Movie("Bahubali", 4.7)

print(my_favorite_movie.id, my_favorite_movie.name, my_favorite_movie.rating)
print(your_favorite_movie.id, your_favorite_movie.name, your_favorite_movie.rating)

