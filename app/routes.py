import datetime

import requests
from dateutil.relativedelta import relativedelta
from flask import render_template

import util
from app import app
from config import Config
from forms import UserPreferencesForm
from app.models.movie import Movie
from app.models.results import Results
from twilio.rest import Client


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Homepage')


@app.route('/all_movies')
def all_movies():
    movies_in_theaters = _fetch_movies()
    return render_template('all_movies.html', title='All Movies', result=Results(None, None, movies_in_theaters))


@app.route('/form', methods=['GET', 'POST'])
def user_preferences_form():
    form = UserPreferencesForm(meta={'csrf': False})
    if form.validate_on_submit():
        matching_movies = _fetch_matching_movies(form.genres_checkbox.data)
        chosen_genres_names = _checklist_mapping(form.genres_checkbox.data)
        user_results = Results(form.phone_number.data, chosen_genres_names, matching_movies)
        _send_sms(user_results)
        return render_template('results.html', result=user_results)
    return render_template('form.html', title='Trang\'s Movie App', form=form)


def _fetch_matching_movies(chosen_genres):
    """
    Fetch all movies that are in theaters that match the given genres
    :return:
    """
    chosen_genres = [int(g) for g in chosen_genres]   # Turn all items in the chosen genres list to ints for comparison
    return filter(lambda m: set(m.genres) & set(chosen_genres) != set([]), _fetch_movies())


def _fetch_movies():
    """
    Make request to TheMovieDB API to get all movies that are in theaters
    In theaters meaning the movie's release date was a month ago up until today
    :return:
    """
    # Base url
    tmdb_base = 'https://api.themoviedb.org/3'
    tmdb_api_key = 'api_key=' + Config.MOVIE_DB_KEY
    search_query = '/discover/movie?'

    # Calculate time frame
    now = datetime.datetime.now()
    date_format = '%Y-%m-%d'
    released_after_date = (now - relativedelta(months=1)).strftime(date_format)
    released_after = 'primary_release_date.gte=' + released_after_date
    released_before = 'primary_release_date.lte=' + now.strftime(date_format)

    # Make GET request
    request = tmdb_base + search_query + released_after + '&' + released_before + '&' + tmdb_api_key
    response = requests.get(request)

    # Convert json to Movie objects
    movies = [Movie(movie['id'], movie['title'], movie['genre_ids'], movie['vote_average'], movie['overview']) for movie in response.json()['results']]
    return movies


def _checklist_mapping(chosen_genres):
    all_genres = util.read_in_genres_from_csv()
    return [all_genres[cg] for cg in chosen_genres]


def _send_sms(user_results):
    if len(user_results.movies) > 0:
        client = Client(Config.ACCOUNT_SID, Config.AUTH_TOKEN)
        client.messages.create(
            from_='+18036102506',
            body=_construct_sms(user_results.movies),
            to=user_results.phone_number
        )


def _construct_sms(matching_movies):
    pretty_print_movies = '- ' + '\n- '.join(sorted(_remove_unicode(*matching_movies)))
    return 'Thank you for using Trang\'s Movie App!\n' \
           'Here is a reminder to see these movies:\n' + str(pretty_print_movies)


def _remove_unicode(*movies):
    return [m.title.encode('UTF8') for m in movies]
