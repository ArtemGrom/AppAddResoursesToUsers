# AppAddResoursesToUsers

We make a clone of the repository to our computer command git clone https://github.com/ArtemGrom/AppAddResoursesToUsers.git or with SSH keys git@github.com:ArtemGrom/AppAddResoursesToUsers.git
Than you can install all dependency from pyproject.toml and start app with command: python manage.py runserver

URL:
 - for registration http://127.0.0.1:8000/add_host/sign_up/
 - for authorization http://127.0.0.1:8000/add_host/login_user/
 - for create host http://127.0.0.1:8000/add_host/create/
 - for update host http://127.0.0.1:8000/add_host/<int:id>/update
 - list of your hosts http://127.0.0.1:8000/add_host/list_host/
