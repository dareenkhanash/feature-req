from feature_req import app, db
from flask import request, json, jsonify
from datetime import datetime
from feature_req.models import Request, Client, ProductArea


# add new feature request to database 
def add_feature_request(form):
    title = form['title']
    description = form['description']
    client = form['client']
    priority = int(form['client_priority'])
    target_date = datetime.strptime(form['target_date'], '%Y-%m-%d')
    product_area = form['product_area']
    new_feature_request = Request(
        title=title,
        description=description,
        client_priority=priority,
        target_date=target_date,
        client_id=client,
        product_area_id=product_area
    )
    db.session.query(Request).filter(Request.client_priority >= priority).\
    update({Request.client_priority: Request.client_priority + 1}, synchronize_session=False)
    db.session.add(new_feature_request)
    db.session.commit()
    return     