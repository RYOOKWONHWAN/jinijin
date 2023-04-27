from tkinter import *
import recommend


def get_movies():
    movies = "The Super Mario Bros,Shazam!,Ant-Man and the Wasp: Quantumania,Avatar: The Way of Water,Creed III"
    movie_list2 = []
    movie_list1 = movies.split(',')
    for movie in movie_list1:
        movie = movie.strip()
        movie_list2.append(movie)

    # recommendation algorithm
    print(movie_list2)
    result = recommend.main(movie_list2)

    return result


print(get_movies())
