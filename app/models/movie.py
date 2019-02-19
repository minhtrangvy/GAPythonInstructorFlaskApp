class Movie:
    def __init__(self, id, title, genres, rating, overview, poster_url=None):
        self.id = id
        self.title = title
        self.genres = genres
        self.rating = rating
        self.overview = overview
        if poster_url:
            self.poster_url = 'http://image.tmdb.org/t/p/w185/' + poster_url
        else:
            self.poster_url = None

    def __str__(self):
        return str(self.__dict__)
