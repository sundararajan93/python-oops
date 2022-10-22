class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Invalid Rating Given!!!")

    @rating.deleter
    def rating(self):
        del self._rating

my_fav_movie = Movie("RRR", 4.7)

print("Rating: ", my_fav_movie.rating)

my_fav_movie.rating = 4.9
print("Rating", my_fav_movie.rating)

# del my_fav_movie.rating
# print("Rating: ", my_fav_movie.rating)