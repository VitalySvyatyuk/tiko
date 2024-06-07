# Events API

### Installation
Create virtual environment and install packages:

`pip install -r requirements.txt`

Apply migrations:

`python manage.py migrate`

Create superuser:

`python manage.py createsuperuser`

(optional) Login to admin and create users/events:

`http://127.0.0.1:8000/admin`

API Docs available on:

`http://127.0.0.1:8000/api/swagger`

### Authorization
To register new user you can send POST-request to:

`http://127.0.0.1:8000/api/register/`

To receive new token send POST-request to:

`http://127.0.0.1:8000/api/token/`

To refresh access token from refresh token send POST-request to:

`http://127.0.0.1:8000/api/token/refresh`

Use this token in `Authorization` header of each request.

### Information
Authorized users can do requests to `/events/` to create/edit/delete/list events or register/unregister to/from events.




