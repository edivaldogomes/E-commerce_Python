# E-commerce_Python

# Steps to Dockerize

Creation of the Dockerfile.
Creation of the docker-compose.yml file.
Initialization of containers with selected images using the command:
$ docker-compose run web django-admin startproject core .
Bring up the containers using the command:
$ docker-compose up
Stop the containers using the command:
$ docker-compose down

# To compile the program

1.  Fork the repository.

2.  Ensure Docker Desktop is installed on your system.

3.  Run the following command to build the container image:
    $ docker-compose build

4.  Start the Docker container using the following command:
    $ docker-compose up

5.  Access the URL in your web browser:
    http://localhost:8000

6.  If you want to create a new app, use the following command:
    $ docker-compose run web python manage.py startapp "app name"

7.  To verify that the program is functioning properly, try accessing this URL. You should see the message "Hello Delphin Project" on your screen:
    http://localhost:8000/category/hello/

8.  If you've installed a new dependency, update the requirements.txt file with the command:
    $ docker-compose run web pip freeze > requirements.txt

9.  To rebuild the image, you can also use these commands:
    $ docker-compose build -> Build the image i docker desktop
    $ docker-compose up -> Run the container
    $ docker-compose down -> Delete all change of database

            -----RUN-----

    docker-compose run web
    docker-compose run web python manage.py startapp subcategory
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser
    docker-compose run web python manage.py collectstatic
