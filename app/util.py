import csv


def read_in_genres_from_csv():
    all_genres = {}
    with open('app/genres.csv', 'rb') as csv_file:
        genre_reader = csv.DictReader(csv_file)
        for genre in genre_reader:
            all_genres[genre['Id']] = genre['FriendlyName']
    return all_genres
