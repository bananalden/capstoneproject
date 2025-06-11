# Capstone Project: Online Student Records and Document Request System for Vision Academy

This was the capstone project me and Mark Joseph developed in order to fulfill the requirements for our Graduation. The system utilizes the Django framework for the backend, and many python libraries such as pandas, and weasyprint. The system was developed with the purpose to provide an online platform 
for students to make document requests. The system was able to generate pre-rendered document templates with names of students being automatically filled out based on whether the student has requested for them.

## Setting up for development
1. After downloading the project open a pipenvironment in order to run the installed packages
```
pipenv shell
pipenv install
```
2. Once the packages have been installed, create a **.env** file with the required variables that can be found within the **studentportal** folder and in the **settings.py** file.
3. Before starting the project, make sure you have a PostgreSQL database connected to it,
4. Make sure to run the following command in order to create the necessary tables:
```
python manage.py migrate
```
5. Run the following command to create a superuser/admin account to access the system:
```
python manage.py createsuperuser
```
6. After creating the superuser you may now run the system in your machine with the following command:
```
python manage.py runserver
```
