# feature-req

## Description

feature-req is a web application that allowes the user to create &quot;feature requests&quot;.
A &quot;feature request&quot; is a request for a new feature that will be added onto an
existing piece of software.

## Table of Contents
* [Requirements](#Requirements)
* [Installation](#Installation)
* [Usage](#Usage)


## Requirements

    • OS: Ubuntu
    • Server Side Scripting: Python 3.6+
    • Server Framework: Flask
    • ORM: Sql-Alchemy
    • JavaScript: JQuery and KnockoutJS

### Installing Dependencies

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
  3. create database 

```sh
python create_db.py

```

  4. Run app 

```sh
python run.py

```
  5. check app on http://localhost:5000 



