from lookup import Lookup

def parse_regions(region):
    return region[0].split(',')

def lookup_movie_specified_regions(movie_name, regions):
    look = Lookup()
    look.set_movie_query_spec_regions(movie_name[0], parse_regions(regions))
    look.check_availability()

def lookup_movie(movie_name):
    look = Lookup()
    look.set_movie_query(movie_name[0])
    look.check_availability()


