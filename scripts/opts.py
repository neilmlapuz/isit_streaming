from lookup import Lookup

def lookup_movie(movie_name):
    look = Lookup(movie_name[0])
    look.check_availability()
