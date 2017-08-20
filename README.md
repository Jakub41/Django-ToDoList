# Django To Do List

## Intro

A simple to do list done in Django with a Flask Rest API and MongoDB for the backend.

## Installation:

1.) Use pip to install all of the requirements by running pip install -r requirements.txt
2.) Start your local mongo database
3.) Start the API in the api directory by running `python app.py`
4.) In the todolist directory, run `python manage.py migrate`
4.) Start the Django app in the todolist directory by running `python manage.py runserver`
5.) The Django app will be running at http://localhost:8000
6.) The Flask API with be running at http://localhost:5000

## Technologies Used:

1.) Django is used to run a web application that is serving the static views for the application.
2.) Flask is used to run an API that is connected to the MongoDB, and it exposes RESTful endpoints
    for managing the todolist tasks.
3.) All API calls on the static pages are made using AJAX via the Axios library.
4.) There is no JavaScript framework used. Jquery and vanilla JavaScript are responsible for modifying the Domain

## Why Technologies Were Selected

Django is an excellent Python framework for rapidly building web applications. It makes setting up authentication
simple and comes with a built in admin panel. Flask is a great Python micro-framework for web requests, and makes
it the perfect choice for a small RESTful API. MongoDB was selected as the backend because unlike a traditional
relational database, MongoDB allows for the storing of JSON documents, providing much more flexibility in saving
data.