from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from feature_req.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config) 
    db.init_app(app)
    
    from .routes import feature_req
    app.register_blueprint(feature_req)

    return app
   






####
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#import os


#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)


#from feature_req import routes

#app.register_blueprint(routes)

#import os

#if __name__ == '__main__':
   # port = int(os.environ.get('PORT', 5000))
  #  app.run(host= '0.0.0.0',port=port)
