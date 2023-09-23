# Bookstore API
This is a bookstore API built with Django Rest Framework. It allows users to create and login, CRUD their own books, and only authors can CRUD their own books. It also features JWT authentication and API documentation (coreapi).

## Requirements

* Python 3.6+
* Django 3.2+
* Django Rest Framework 3.12+
* djangorestframework-jwt
* coreapi (for API documentation)


## Installation

1. Clone the repository:
```
$ git clone https://github.com/ebene88/BookStore-API-with-Django-REST-Framework.git
```
2. Navigate to the project directory:
```
$ cd bookstore-api
```
3. Create a virtual environment and activate it:
 ```
$ python3 -m venv venv
$ source venv/bin/activate
```
4. Install the required dependencies:
```
$ pip install -r requirements.txt
```
5. Collect static files:
```
$ python manage.py collectstatic
```
6. Run database migrations:
```
$ python manage.py migrate
```
7. Create a superuser:
```
$ python manage.py createsuperuser
```

8. Run the development server:
```
$ python manage.py runserver
```


## JWT Authentication

The bookstore_api uses JWT authentication to authenticate users. When a user logs in, the server generates a JWT token and returns it to the user. The user should then store the token in a secure location.

To make subsequent requests to the API, the user must include the JWT token in the Authorization header of the request. For example:
```
Authorization: Bearer <JWT token>
```
The server will verify the JWT token on each request and deny the request if the token is invalid.

## API Documentation (coreapi)

The bookstore_api uses coreapi to generate API documentation. To view the API documentation, open the following URL in a web browser:
```
$ http://localhost:8000/api/docs/
```
The API documentation will provide a detailed overview of all of the available endpoints, including the required parameters and response formats.
