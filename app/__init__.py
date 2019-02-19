from flask import Flask
from flask_debug import Debug

from config import Config

app = Flask(__name__)
Debug(app)
app.config.from_object(Config)
app.run(debug=True)

from app import routes