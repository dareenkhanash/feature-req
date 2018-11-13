from feature_req.models import Request, Client, ProductArea
from flask_marshmallow import Marshmallow
from feature_req import app


ma = Marshmallow(app)


class ClientSchema(ma.ModelSchema):
    class Meta:
        model=Client
        fields = ('id', 'client_name')


class ProductAreaSchema(ma.ModelSchema):
    class Meta:
        model=ProductArea    


class RequestSchema(ma.ModelSchema):

    class Meta:
        model=Request
        fields = ('id', 'title', 'client_name','product_area_name','description','client_priority','target_date')
    client = ma.Nested(ClientSchema)
    product_area = ma.Nested(ProductAreaSchema)


