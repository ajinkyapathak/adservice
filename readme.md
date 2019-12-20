Language = python 3.6
Django = 3.0
Database = sqlite3
API tool - Postman

- How to run project
* Virtual env setup
    1. create a virtualenv for python3.6
    2. source to that virtualenv
    3. run pip install -r requirements.txt
    
* Basic Setup
# make sure in parent adservice directory then apply following commands
    1. export DJANGO_SETTINGS_MODULE=adservice.db.settings.base; export PYTHONPATH=$PWD;
    2. python adservice/manage.py migrate ad_management
    3. python adservice/scripts/category_population.py
    4. python adservice/scripts/users_population.py
    
* Run the application
# make sure in parent adservice directory then apply following commands
    1. export DJANGO_SETTINGS_MODULE=adservice.db.settings.base; export PYTHONPATH=$PWD;
    2. python adservice/conf/service_app.py

- Download Postman
https://www.getpostman.com/downloads/

- Import collection using following url
(make sure application is running in background before hitting API through postman)
https://www.getpostman.com/collections/17146431b04440865ca4

