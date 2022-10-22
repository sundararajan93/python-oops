class Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title

my_movie = Movie("Vikram", 4.8)
print("My favorite movie is ", my_movie.get_title())