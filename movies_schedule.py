current_movies = {'The Grinch':'11:00am', 
'The Matrix: Unloaded':'2:00pm',
'Spoderman:Some Way Home':'4:00pm',
'Croation Pie':'7:30pm'}

print("Here are the available movies you can watch:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("What movie is that? We don't have it...")
else:
    print(movie, 'is playing at', showtime)