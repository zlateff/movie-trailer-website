import webbrowser


class Movie():
    """Class Movie for creating movie objects.

    Attributes:
        title: The title of the movie.
        storyline: Short storyline of the movie.
        poster_image_url: URL for the movie's poster image.
        trailer_youtube_url: URL for the movie's YouTube trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Inits Movie with title, storyline, poster, and trailer."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens and plays the movie's trailer"""
        webbrowser.open(self.trailer_youtube_url)
