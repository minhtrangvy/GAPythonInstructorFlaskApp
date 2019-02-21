# GAPythonInstructorFlaskApp
This is for GA's Python Instructor position. 
This app is a movie app! Read more about the actual purpose of the app in index.html, once you've spun up the local server.

## Instructions
This app is Dockerized. This means that all the dependencies are contained in a docker image. 
All you have to do is run some Docker commands to get the web app working locally!
1. In terminal, lease run `docker build -t gaproject:latest .` in the `/GAPythonInstructorFlaskApp` directory to build the image.
2. An email will be sent with the Twilio Auth, it should look something like `21xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.    
    Run the container by running this command: 
    ```
    docker run -d -p 5000:5000 -e AUTH_TOKEN=21xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx gaproject
    ```    
    This spins up the web app!     
    
    Run `docker ps` to make sure something is running. It should look something like this:
    ```
    (venv) ~/P/m/GAPythonInstructorFlaskApp » docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
    1e1364db8a59        gaproject           "flask run --host=0.…"   4 minutes ago       Up 4 minutes        0.0.0.0:5000->5000/tcp   happy_swanson
    ```
3. Go to localhost:5000 to experience the web app :)
4. To stop the server, run `docker stop 1e1364db8a59`, where `1e1364db8a59` is the `CONTAINER ID` above.


## Requirements
Here we will dive a little deeper into the requirements of the coding challenge and how this repo meets those requirements.
- At least 3 routes with views, at least one GET and one POST
    - The 3 routes can be found in routes.py: /index, /form, /all_movies
    - The form one can handle both GET and POST and the rest are by default only handle GET requests
- Data pulled from at least 1 API
    - Pulled data from The Movie DB API 
    - Also used the Twilio SMS API to send text messages
- Clean HTML and CSS
- Python concepts:
    - [dictionary](/gaproject/util.py#L9), [set](/gaproject/__init__.py#L60), or tuple
    - [*args](/gaproject/__init__.py#L126), kwargs, or *kwargs
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