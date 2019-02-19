class Movie:
    def __init__(self, id, title, genres, rating, overview):
        self.id = id
        self.title = title
        self.genres = genres
        self.rating = rating
        self.overview = overview

    def __str__(self):
        return str(self.__dict__)
