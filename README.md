# GAPythonInstructorFlaskApp
This is for GA's Python Instructor position. 
This app is a movie app! Read more about the actual purpose of the app in index.html<br>
Here we will dive a little deeper into the requirements of the coding challenge and how this repo meets those requirements.

## Requirements
- At least 3 routes with views, at least one GET and one POST
    - The 3 routes can be found in routes.py: /index, /form, /all_movies
    - The form one can handle both GET and POST and the rest are by default only handle GET requests
- Data pulled from at least 1 API
    - Pulled data from The Movie DB API 
    - Also used the Twilio SMS API to send text messages
- Clean HTML and CSS
- Python concepts:
    - [dictionary](/gaproject/util.py#L9), [set](/gaproject/__init__.py#L60), or tuple
    - [**args](/gaproject/__init__.py#L126), kwargs, or *kwargs
    - A [class](/gaproject/models)
    - user input or [reading content from a file](/gaproject/util.py)
- Comments
    - There is this README as well as some inline comments littered through the code where necessary
    
## Routes
### /, /index
Returns the Home page that describes what the app is about and how to nagivate it.
### /all_movies
Lists all the movies that are currently in theaters. More specifically, it lists all movies that were released within the last month.
### /form
Renders a form where the user can input their phone number and choose their favorite movie genres.

## Instructions
1. An email will be sent with the Twilio Auth, please do: `export AUTH_TOKEN='21xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'`
2. Install all of the dependencies by running `python setup.py install`. If that doesn't work, install each of these libraries independently. 
    - `pip istall flask`
    - `pip install python-dateutil`
    - `pip install requests`
    - `pip install twilio`
    - `pip install WTForms`
3. Set `export FLASK_APP=gaproject` 
4. Be in the `/GAPythonInstructorFlaskApp` folder and run `flask run`
5. Go to localhost:5000 to experience the web app :)
