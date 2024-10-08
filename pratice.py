movies = [
    ['cars',7.2,'comedy'],
    ['toy story',8.3,'Adventure, Comdey'],
    ['Iron man',7.9,'Superhero'],
    ['Pokemon the first movie',6.3,'Anime']
]

# Example
print(movies[0][2]) #Output: comedy
print(movies[1][1]) #Output: 8.3
print(movies[2][0]) #Output: Iron man

#New movies
new_movies = ['Coco',8,'Drama'] 
movies.append(new_movies)
print(movies) #Output: [['cars', 7.2, 'comedy'], ['toy story', 8.3, 'Adventure, Comdey'], ['Iron man', 7.9, 'Superhero'], ['Pokemon the first movie', 6.3, 'Anime'], ['Coco', 8, 'Drama']]

#loops
for movie in movies:
    print("This movie called", movie)
