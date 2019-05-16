# Django App

### Pre request:-
    installed python and pip3
    installed pip3 OR  run to install pip3            : sudo apt-get install python3-pip
    installed virtulaenv OR run to install virtualenv : sudo pip3 install virtualenv
### NEXT:
	download this repo and go to root directory
	run into ur project root directory to create virtual environment: virtualenv venv
	run to install virtual environment activate: source venv/bin/activate
### NEXT:
	run to install package dependency: pip install -r requirements.txt
### NEXT:-
    python manage.py runserver

### steps to integrate mysqlclient with django (special case)

	Step: 1. sudo apt-get install python3-dev
	Step: 2. sudo apt-get install libmysqlclient-dev
	Step: 3. pip install mysqlclient -after tow above installation we able to install mysqlclient
	Step: 4. Create database by which name you are using in project
	Step: 5. run python manage.py migrate 
