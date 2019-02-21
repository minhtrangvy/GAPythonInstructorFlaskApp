FROM python:2.7

WORKDIR /app

# Install app dependencies
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Put everything into docker folder
COPY . /app

# Alias for FLASK_APP
ENV FLASK_APP=gaproject
ENV AUTH_TOKEN=placeholder

EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]