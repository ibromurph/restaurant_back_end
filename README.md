# Restaurant web application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ibromurph/restaurant_back_end
$ cd restaurant_back_end
```

Create a virtual environment to install dependencies in and activate it:


```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
or you can check this documentations
https://docs.python.org/3/library/venv.html
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd backend
Paste Media File folder in root directory (i.e) where you will find manage.py 
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
create folder named as static in root director of project
(env)$ python manage.py collectstatic
(env)$ python manage.py createsuperuser 
(env)$ python manage.py runserver
```
```sh

And navigate to `http://127.0.0.1:8000/admin/`.

Existing user details
Login Details 
username=ibromurph
password=root

Heroku admin login detail
username=ibromurph
password=dave123
 
Credit: Ibrahim Murphy, Mohammed Charles Murphy (brother; offering support and QA), template design from colorlib.com
