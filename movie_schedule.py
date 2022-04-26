current_movies = {'Star Trek': '3:00PM', 
    'Star Wars': '12:30PM', 
    'Blade Runner': '4:50PM', 
    'Alita: Battle Angle': '7:45PM'}

print("We're currently showing the folling movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)
if showtime:
    print('The showtime for', movie, 'is', current_movies[movie], '.')
else:
    print('This movie is not showing')