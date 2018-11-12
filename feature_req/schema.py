from feature_req.models import Request, Client, ProductArea
from flask_marshmallow import Marshmallow
from feature_req import app


ma = Marshmallow(app)


class RequestSchema(ma.ModelSchema):
    class Meta:
        model=Request


class ClientSchema(ma.ModelSchema):
    class Meta:
        model=Client


class ProductAreaSchema(ma.ModelSchema):
    class Meta:
        model=ProductArea       
