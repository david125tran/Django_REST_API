# Django_REST_API  
A REST api built with Django using their broilerplate that has Create, Read, and Delete functionality.  
Docs: https://www.django-rest-framework.org/
  
# Terminall installations:
pip install django  
pip install djangorestframework  
  
# Django broilerplate installation:  
Most of this code was built starting from the Django broiler plate.  
To install the broilerplate, type in the terminal:  
django-admin startproject myproject  

# To run the project:
cd myproject  
python manage.py runserver  
<img src="https://github.com/david125tran/Django_REST_API/blob/main/images/terminal.png" width="70%">

# Create / Post:
https://127.0.0.1:8000/add  
Go to the add page to add an entry to the database:  
<img src="https://github.com/david125tran/Django_REST_API/blob/main/images/add.png" width="70%">  
  
Example of JSON format for entry:  
<img src="https://github.com/david125tran/Django_REST_API/blob/main/images/add_example1.png" width="70%">  

Syntax:  
{  
"name":"Joe"  
}  
  
Click "post"  
  
The entry was added:  
<img src="https://github.com/david125tran/Django_REST_API/blob/main/images/add_example2.png" width="70%">

# Read / Get:  
https://127.0.0.1:8000  
<img src="https://github.com/david125tran/Django_REST_API/blob/main/images/get.png" width="70%">

# Delete  
https://127.0.0.1:8000  
Click the delete button:  
<img src="https://github.com/david125tran/Django_REST_API/blob/main/images/delete1.png" width="70%">  
  
This button will delete all of the entries from the database:  
<img src="https://github.com/david125tran/Django_REST_API/blob/main/images/delete2.png" width="70%">
