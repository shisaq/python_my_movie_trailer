import webbrowser

# create Movie class to build all instances of videos
class Movie():
    """This provides the available movie variables"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__ (self, movie_title, movie_storyline, movie_cover, movie_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_cover
        self.trailer_youtube_url = movie_youtube_url
