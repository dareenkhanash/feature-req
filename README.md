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
The app is running on an AWS EC2 instance. 
Ubuntu 18.4 LTS provided by AWS.
PostgresSQL production instance is running on the same machine.

## Installing Dependencies

```sh
install python 
install pip

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
  3. Navigate to feature-req folder and add .env file with this variable

```sh
export DATABASE_URL="sqlite:///featurerequests.db"

```

  4. create database in terminal run:

```sh
python create_db.py

```

  5. Run app in terminal navigate to the root of feature-req folder and run:

```sh
python run.py

```
  6. check app on http://localhost:5000 



## Run Test

navigate to feature-req folder 

```sh
python test_app.py

```




