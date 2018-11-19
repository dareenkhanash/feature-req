from datetime import datetime
from feature_req.app import db


#Client Model 
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(200))
    feature_requests = db.relationship('Request', backref='client', lazy=True)
    def __init__(self, client_name):
        self.client_name = client_name

#Product Area Model
class ProductArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_area_name = db.Column(db.String(200))
    feature_requests = db.relationship('Request', backref='product_area', lazy=True)
    def __init__(self,product_area_name):
        self.product_area_name = product_area_name

#Request Model
#all fields are required except for the description
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    client_id = db.Column(
        db.Integer,
        db.ForeignKey('client.id'),
        nullable=False
    )
    client_priority = db.Column(db.Integer, default=1)
    product_area_id = db.Column(
        db.Integer,
        db.ForeignKey('product_area.id'),
        nullable=False
    )
    target_date = db.Column(db.Date, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, onupdate=datetime.utcnow)
    def __init__(self, title, description, target_date, client_id, client_priority, product_area_id):
        self.title = title
        self.description = description
        self.target_date = target_date
        self.client_id = client_id
        self.client_priority = client_priority
        self.product_area_id = product_area_id
