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
    - **args, kwargs, or *kwargs
    - A class
    - user input or reading content from a file
- Comments
    - There is this README as well as some inline comments littered through the code where necessary

## Routes
### / or /index
### /all_movies
### /form

## Instructions
1. An email will be sent with the Twilio Auth, please do: `export AUTH_TOKEN='21xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'`
2. 