from feature_req.app import db
from feature_req.models import Request, Client, ProductArea

from feature_req.app import create_app

app = create_app()
app.app_context().push()
with app.app_context():
    db.create_all(None)

    pa=ProductArea(product_area_name='Policies')
    db.session.add(pa)
    db.session.commit()
    pa=ProductArea(product_area_name='Billings')
    db.session.add(pa)
    db.session.commit()
    pa=ProductArea(product_area_name='Claims')
    db.session.add(pa)
    db.session.commit()
    pa=ProductArea(product_area_name='Reports')
    db.session.add(pa)
    db.session.commit()

    client=Client(client_name='Client A')
    db.session.add(client)
    db.session.commit()
    client=Client(client_name='Client B')
    db.session.add(client)
    db.session.commit()
    client=Client(client_name='Client C')
    db.session.add(client)
    db.session.commit() 