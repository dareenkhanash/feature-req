# feature-req



## Description



feature-req is a web application that allowes the user to create &quot;feature requests&quot;.

A &quot;feature request&quot; is a request for a new feature that will be added onto an

existing piece of software.



## Application Overview



Feature Requests:

GET /getData



Add Request:

POST /request/{request form data}



Delete Request:

DELETE /request/delete/:request_id



Edit Request:

GET /request/:request_id



Update Request:

POST /request/update/{request form data}



## Requirements



    • OS: Ubuntu

    • Server Side Scripting: Python 3.6

    • Server Framework: Flask

    • ORM: Sql-Alchemy

    • JavaScript: JQuery and KnockoutJS



## Deployment

The app is running on an AWS EC2 instance.</br>

Ubuntu 18.4 LTS provided by AWS.</br>

PostgresSQL production instance is running on the same machine.</br>



## Installing Dependencies



```sh

install python 

install pip



```

## Setup DataBase





1. Install PostgreSQL:



```sh

sudo apt-get install postgresql postgresql-contrib 

```

2. Access PostgresSQL:



```sh

sudo -iu postgres

```

3. Create Database:



```sh

createdb featurerequest

```

4. Access DataBase:



```sh

psql -d featurerequest

```

5. Create the user and grant access to database:



```sh

CREATE ROLE iws WITH LOGIN PASSWORD <yourpassword>;

GRANT ALL PRIVILEGES ON DATABASE featurerequest TO iws;

ALTER USER iws CREATEDB;

```

## Run locally

  1. Clone or download the repo 



```sh

git clone https://github.com/dareenkhanash/feature-req  



```

  2. create virtual enviroment and install requirements 



```sh

pip install virtualenv

virtualenv feature_request_env

source feature_request_env/bin/activate

pip install -r requirements.txt



```

  3. change the POSTGRES object in config.py to your database information



```sh

POSTGRES = {

    'user': 'iws',

    'pw': <yourpassword>,

    'db': 'featurerequest',

    'host': 'localhost',

    'port': '5432'

}





```



  4. create tables in terminal navigate to the root of feature-req folder and run:



```sh

python create_db.py



```



  5. Run app in terminal navigate to the root of feature-req folder and run:



```sh

python run.py



```

  6. check app on http://localhost:5000 







## Run Test
1. do the same steps for creating database for test call it test_featurerequest
2. change test_config based in your test database config
3. navigate to feature-req folder and run:



```sh

python test_app.py



```









