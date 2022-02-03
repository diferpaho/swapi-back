# SW API GraphQL

## Description

Test BackEnd Software Engineer - LQN

## Part 1 - Logic exercises

### Description
Logic exercises developed in Python

#### Running the script

To execute the script of section A execute the following command:
```
python3 part1-logic/partA.py
```

To execute the script of section B execute the following command:
```
python3 part1-logic/partB.py
```

## Part 2 - Mini project

### Description

Project containing a GraphQL API for a website to
Star Wars fans.

### Requirements
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

### Setup

Clone the project
```
git clone https://github.com/gustav0/swapi.git
```

Move into de repo and install dependencies
```
pip install -r requirements.txt
```

Run migrations and load fixtures
```
python manage.py migrate
python manage.py load_fixtures
```

#### Running the server
```
python manage.py runserver
```
If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

#### Runing the tests
```
python manage.py test
```
#### Support

This project is based on Django, for more information you can access https://www.djangoproject.com/

You can find more information about graphql at https://graphql.org/

#### Generate a docker image

You can use the following command in terminal to build the project image.

```
docker build .
```

