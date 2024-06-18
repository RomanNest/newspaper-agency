# Newspaper Agency

This application for managing a newspaper agency.

### Check it out

[Newspaper agency project deployed to Render] (https://newspaper-agency-2dec.onrender.com)

###  Features

* Create, update and delete articles, redactors.
* Articles are associated with topics and redactors.
* Searching is able for articles, topics and redactors.
* User must be authentication and authorization.


### Installation
1. Clone this repository.
2. Open the project directory.
3. Create a virtual environment and activate:
 -> virtualenv env
 -> .\env\Scripts\activate
 -> pip3 install -r requirements.txt
4. Set Up Database:
 -> python manage.py makemigrations
 -> python manage.py migrate
5. Start the app:
 -> python manage.py runserver


You can use the following credentials to log into your personal account:
Login: user
Password: test_password
or create a new superuser
 -> python manage.py createsuperuser
