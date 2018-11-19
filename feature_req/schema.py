from feature_req.models import Request, Client, ProductArea
from flask_marshmallow import Marshmallow


ma = Marshmallow()


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

    def process_client(self, data):
        client = data.get('client_id')
        if client:
            if isinstance(client, dict):
                client_name = client.get('client_name')
            else:
                client_name = client
            client_dict = dict(client_name=client_name)

        else:
            client_dict = {}

        data['client_id'] = client_dict
        product_area = product_area.get('product_area_id')
        if product_area:
            if isinstance(product_area, dict):
                product_area_name = product_area.get('product_area_name')
            else:
                Product_area_name = product_area
            product_area_dict = dict(product_area_name=product_area_name)

        else:
            product_area_dict = {}

        data['product_area_id'] = product_area_dict
        return data




