from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
os.environ['DATABASE_URL'] = <URL>
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
print(os.environ['DATABASE_URL'])
db = SQLAlchemy(app)


from feature_req import routes