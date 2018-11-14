from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  "postgres://kkfyldiafopfgc:fec67dbae9bcfe5d68ed60f4389959c09e64c3b9ebfece493f512caa60340b9c@ec2-54-204-10-231.compute-1.amazonaws.com:5432/dfvsp60t634an1"
db = SQLAlchemy(app)


from feature_req import routes