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
    - [dictionary](../blob/master/app/util.py#L5), [set](../blob/master/app/routes.py#L46), or tuple
    - [**args](../blob/master/app/routes.py#L97), kwargs, or *kwargs
    - A [class](https://github.com/minhtrangvy/GAPythonInstructorFlaskApp/tree/master/app/models)
    - user input or [reading content from a file](https://github.com/minhtrangvy/GAPythonInstructorFlaskApp/blob/master/app/util.py)
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
2. This project has been Dockerized so that all of the necessary libraries are already included for easy installation.

    If all else fails, here are some libraries that need to be installed:
    - `pip istall flask`
    - `pip install python-dateutil`
    - `pip install requests`
    - `pip install twilio`
    - `pip install WTForms`

    I am assuming that the evaluator at the very least has Python 2.7 and pip installed. Sorry if I missed any...
3. Be in the `/GAPythonInstructorFlaskApp` folder and run `flask run`!