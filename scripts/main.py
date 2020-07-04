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

    
    return parser

def parse_options():
    parser = set_options()
    (option, args) = parser.parse_args()

    return (option, args)

def main():
    (option, arg) = parse_options()

    if option.lookup:
        opts.lookup_movie(arg)
    elif option.new:
        opts.new_movie(arg)


if __name__ == '__main__':
    main()

