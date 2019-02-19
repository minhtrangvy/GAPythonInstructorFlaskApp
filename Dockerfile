#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
#COPY . /gaproject
#WORKDIR /gaproject
#RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["gaproject.py"]

FROM ubuntu:latest
COPY . /app
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["/routes.py"]