# Homespace API

[![Build Status](https://travis-ci.org/syscondo/back_end_condo.svg?branch=master)](https://travis-ci.org/syscondo/back_end_condo)
[![Updates](https://pyup.io/repos/github/syscondo/back_end_condo/shield.svg)](https://pyup.io/repos/github/syscondo/back_end_condo/)
[![Python 3](https://pyup.io/repos/github/syscondo/back_end_condo/python-3-shield.svg)](https://pyup.io/repos/github/syscondo/back_end_condo/)
[![codecov](https://codecov.io/gh/syscondo/back_end_condo/branch/master/graph/badge.svg)](https://codecov.io/gh/syscondo/back_end_condo/)

API for the Homespace project

## How to develop?

1. Clone the repository
2. Navigate to the project directory
3. Create a virtualenv with Python 3.10
4. Activate the virtualenv
5. Install the development dependencies
6. Configure the development database
7. Run the tests

```console
git clone git@github.com:homespacedigital/homespace-api.git
cd homespace-api
python -m venv venv
source ./venv/bin/activate (If you are using Windows, use .\venv\Scripts\activate.bat)
python -m pip install -r requirements-dev.txt
python manage.py migrate
python manage.py test
```

## How to deploy?

1. Create a new branch with the name of the feature prefix and the feature name (eg: feature/feature-name)
2. Make the changes and commit
3. Push the branch to the repository
4. Create a pull request to the development branch
5. After the pull request is approved, merge the branch into the development branch


```console
git checkout -b feature/feature-name
git add .
git commit -m "Commit message"
git push origin feature/feature-name
```

## How is the project structured?

```console
homespace-api
├── public (public files used for static files and media. This folder is not versioned)
├── settings (django project settings - including wsgi, settings and urls),
├── src (django apps) 
│   ├── <app_name> (name of the app)
│   │   ├── admin (django admin modules package)
│   │   │   ├── <modules>
│   │   ├── migrations (django migrations package - this folder is managed by django)
│   │   │   ├── <modules>
│   │   ├── models (django models package)
│   │   │   ├── <modules>
│   │   ├── serializers (django serializers package)
│   │   │   ├── <modules>
│   │   ├── tests (django tests package)
│   │   │   ├── tests_api (tests package for the api)
│   │   │   │   ├── <modules>
│   │   │   ├── tests_models (unit tests package for the models)
│   │   │   │   ├── <modules>
│   │   ├── views (django views package - this is the controler in the MVC pattern)
│   │   │   ├── <modules>
│   │   ├── __init__.py (package initialization file)
│   │   ├── apps.py (django app configuration file)
│   │   ├── urls.py (django app urls file)
│   ├── utils (Project utilities package)
│   │   ├── factories (factories for reducing the boilerplate code in the tests)
│   │   │   ├── <modules>
├── .flake8 (flake8 configuration file | flake8 is a tool that helps you keep your code clean)
├── .gitignore (git ignore file)
├── app.json (heroku configuration file)
├── manage.py (django project manager)
├── Procfile (heroku configuration file)
├── README.md (project readme file)
├── requirements.txt (project requirements file)
├── requirements-dev.txt (development requirements file)
├── runtime.txt (heroku configuration file)

```

## How to run the project?

```console
python manage.py runserver
```

## How to create a superuser for the admin?

```console
python manage.py createsuperuser
```


