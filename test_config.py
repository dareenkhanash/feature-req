import os

POSTGRES = {
    'user': 'iws',
    'pw': '123456',
    'db': 'test_featurerequests',
    'host': 'localhost',
    'port': '5432'
}


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES                  
    
