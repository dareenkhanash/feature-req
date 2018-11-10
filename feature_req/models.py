from datetime import datetime
from feature_req import db


#Client Model 
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(200))
    feature_requests = db.relationship('Request', backref='client', lazy=True)

    def __repr__(self):
        return f"Client('{self.client_name}')"


#Product Area Model
class ProductArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_area = db.Column(db.String(200))
    feature_requests = db.relationship('Request', backref='product_area', lazy=True)

    def __repr__(self):
        return f"ProductArea('{self.product_area}')" 



#Request Model
class Request(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
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

    def __repr__(self):
        return f"Request('{self.title}'),'{self.client_id}','{self.product_area_id}'"

