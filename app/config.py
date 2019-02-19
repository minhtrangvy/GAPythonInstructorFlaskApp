import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fun-app-no-need'
    MOVIE_DB_KEY = 'e8dde08f9b59d0ec23beda6b2b925cfc'
    ACCOUNT_SID = 'AC7f8043a707db548475837f307db990e1'
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
