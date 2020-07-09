import sys
import opts
from optparse import OptionParser

def set_options():
    parser = OptionParser()

    parser.add_option('-l', '--lookup', action='store_true',
                  help='Look for a movie')

    parser.add_option('-n', '--new',
                  action='store_true',
                  help='What "is" new?')

    parser.add_option('-r', '--add_region',
                action='append',
                dest='regions',
                default=[],
                help='Add region')

    return parser

def parse_options():
    parser = set_options()
    (option, args) = parser.parse_args()
    
    return (option, args)

def main():
    (option, arg) = parse_options()

    if option.lookup and option.regions:
        opts.lookup_movie_specified_regions(arg, option.regions)

    elif option.lookup:
        opts.lookup_movie(arg)

    # Todo
    # elif option.new:
    #     opts.new_movie(arg)



if __name__ == '__main__':
    main()

