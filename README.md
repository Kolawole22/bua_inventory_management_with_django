# Asset Inventory Management App
This Django application is designed to manage and track assets within an organization. It provides functionalities to add, view, edit, and delete inventory items. Additionally, the app offers features for user authentication, email notifications, and data export as CSV.

Make sure you have python and mysql installed

open mysql workbench and create a database with a name of your choice

  
Clone this repository or download the project files.  
You can clone this project by running git clone   
Navigate to the project directory in your terminal.

Create a .env file in the project root directory and add environment variables for database credentials.  

Here's an example .env file:  
DATABASE_NAME=your_database_name  
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password

## Libraries
The following libraries are used in this project:

asgiref==3.7.2  
bleach==6.1.0  
Django==4.2.7  
django-cors-headers==4.3.1  
django-db-logger==0.1.13  
django-filter==23.4  
djangorestframework==3.14.0  
drf_api_logger_with_user==1.2.5  
Markdown==3.5.1  
mysqlclient==2.2.4  
PyJWT==2.8.0  
python-dotenv==1.0.1  
pytz==2023.3.post1  
rest-framework-simplejwt==0.0.2  
six==1.16.0  
sqlparse==0.4.4  
tzdata==2023.3  
webencodings==0.5.1

To install it, First create a virtual environment and activate it.    
To create the virtual environment, open the terminal and navigate to the root of the project if not on it already    
type "python -m venv env" and press enter    
To activate the virtual environment run ".\env\Scripts\activate"  
Then run "pip install requirements.txt" to install the libraries

  
To run your database migrations  
on the terminal run  
python manage.py makemigrations
python manage.py migrate

  
Then create a superuser account by running  
"python manage.py createsuperuser"  
The superuser account is the administrator account with the highest privilege

  
Then start the server by running  
"python manage.py runserver"




