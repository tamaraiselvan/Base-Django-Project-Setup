# Django Basic Setup Project

![GitHub repo size](https://img.shields.io/github/license/tamaraiselvan/Base-django-project-Setup)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)
* [License](#license)

## General info
This Repository has the basic setup of a Django Project. Since setting and configuring a basic setup of a project by using Django is difficult. You can clone this repository for your project, and you can use it for your projects. This Repository is developed with a simplified coding style and file structure.


## Technologies
Project is created with:
* Bootstrap 5.3
* Python 3.10
* Django 4.0.4

## Features
1. Authentication, Authorization. <br>
2. Overwritten Django admin module. <br>
3. Login and Sign up and Logout.<br>
4. A Dashboard and Advanced Navigation system.<br>
5. A good and Mobile friendly User Interface.<br>
6. Advanced UI and UX.<br>
7. Theme Customizer.<br>

## Setup

Follow these steps to make the project run locally:

1. Clone the repository.
   ```sh
   git clone https://github.com/tamaraiselvan/Base-django-project-Setup.git
   ```
2. Create a virtual environment.
   ```sh
   python -m venv virtualenviron_name
   ```
3. Activate the environment.
   ```sh
   virtualenviron_name\Scripts\activate
   ```
4. Install Requirements from the Requirements.txt file.
   ```sh
   pip install -r requirements.txt
   ```
5. Once you installed the requirements, migrate the database.
   ```sh
   python manage.py migrate
   ```
6. Once after migrating, create a superuser account.
   ```sh
   python manage.py createsuperuser
   ```
7. Run the server locally on your system.
   ```sh
   python manage.py runserver
   ```
8. Open your browser and type.
   ```sh
   http://127.0.0.1:8000/
   ```
   
## License
Licensed under the MIT License.
Copyright © 2022 TS Tamarai Selvan [Copy of the license](LICENSE).
