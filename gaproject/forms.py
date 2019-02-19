import util
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField
from wtforms import StringField, SubmitField
from wtforms import widgets


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class UserPreferencesForm(FlaskForm):
    all_genres = util.read_in_genres_from_csv()
    phone_number = StringField('Phone Number (+12223334444 format)')
    genres_checkbox = MultiCheckboxField('Choose some genres you would like to watch:', choices=all_genres.items())
    submit = SubmitField('Submit')
