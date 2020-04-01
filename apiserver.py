# Import your handlers here
from service import IMDB


# Configuration for web API implementation
def config(api):

    # Instantiate handlers and map routes
    api.add_route('/imdb', IMDB())
