# IsIt_Streaming
Is a CLI application that enables you to check for movies or tv shows in Netflix in different regions.
Having recently purchase a VPN subscription to unlock contents of Netflix, the switching from 
one region to another was putting too much effort. IsIt_Streaming helps to check the availability of
the movie or tvshow that you are looking for with just a command! 

# How To Run?
## Installation
Requires FireFox, Python, `pip3` and `virtualenv` to be installed on your machine.
1. Install `virtualenv` globally using `pip3` with `pip3 install virtualenv`.
2. Create a `virtualenv` named `".env"` with `virtualenv .env`.
3. Activate the `virtualenv` with `source .env/bin/activate`.
4. Install dependencies with `pip3 install -r requirements.txt`.
5. run `sh setup.sh`

## Usage - to search for a movie
> run `sh run.sh -l $movie_name`

example - `sh run.sh -l spiderman`

