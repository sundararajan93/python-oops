class Movie:

    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

# Creating instances
my_favorite_movie = Movie("Vikram", 2022, "Tamil", 4.8)
your_favorite_movie = Movie("RRR", 2022, "Telugu", 4.5)

# Accessing the instance attributes 

print("My Favorite Movie: ")
print(my_favorite_movie.title)
print(my_favorite_movie.year)
print(my_favorite_movie.language)
print(my_favorite_movie.rating)


print("Your Favorite Movie: ")
print(your_favorite_movie.title)
print(your_favorite_movie.year)
print(your_favorite_movie.language)
print(your_favorite_movie.rating)

