class Results:
    def __init__(self, phone_number, chosen_genres, movies):
        self.phone_number = phone_number
        if chosen_genres:
            self.chosen_genres = ', '.join(chosen_genres)
        else:
            self.chosen_genres = None
        self.movies = movies
