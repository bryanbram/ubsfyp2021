first time running django:
- run cd \ubsfyp2021\djreact\src
- run pip install -r requirements.txt, (for mysqlclient, windows users may fail to install,  can jus pip install the wheel i uploaded in \ubsfyp2021\djreact\src)
- create a 'fyp' table in local mysql database, change the database settings in the \djreact\src\djreact\settings.py if needed
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver