# Djnago Basic Setup Project

![PyPI - License](https://img.shields.io/pypi/l/Django?color=success&label=License%20Info)
![GitHub repo size](https://img.shields.io/github/repo-size/tamaraiselvan/Base-django-project-Setup?label=Source%20code%20Size)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#Features)
* [Setup](#setup)

## General info
This Repository have the basic setup of a Django Project. Since setting and configuring a basic setup of a project by using Django is difficult. You can clone this repository for your project and you can use it for your projects.


## Technologies
Project is created with:
* Bootstrap 4
* Python 3.10
* Jazzmin 2.5
* Django 4.0

### Features
1> Authentication, Authorization
2> Overwritten Django admin module
3> Login and Sign up
4> A basic page and basic Navigation system.
5> A good and Mobile friendly User Interface.

## Setup

Follow these steps to make project run locally

1. Clone the repository
   ```sh
   git clone https://github.com/The-Code-of-Duty-Team/Examination-project.git
   ```
2. Create a virtual environment
   ```sh
   python -m venv virtualenviron_name
   ```
3. Activate the environment
   ```sh
   virtualenviron_name\Scripts\activate
   ```
4. Install Requirements from the Requirements.txt file
   ```sh
   pip install -r requirements.txt
   ```
5. Once you installed the requirements migrate the datebase
   ```sh
   python manage.py migrate
   ```
6. Once after migrating, Create a superuser account
   ```sh
   python manage.py createsuperuser
   ```
7. Run the server locally on your system
   ```sh
   python manage.py runserver
   ```
8. Open your browser and type
    ```sh
  http://127.0.0.1:8000/
   ```

## Conclusion
