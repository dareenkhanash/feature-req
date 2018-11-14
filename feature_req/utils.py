from feature_req import app, db
from flask import request, json, jsonify
from datetime import datetime
from feature_req.models import Request, Client, ProductArea
from sqlalchemy.orm import validates



def change_priority(priority,clientid,id=0):
    old_priority=priority
    request_id=id
    while old_priority > 0:
        equeal=db.session.query(Request).filter(Request.client_priority == old_priority).\
        filter(Request.client_id == clientid).filter(Request.id != request_id).all()
        if equeal:
           db.session.query(Request).filter(Request.client_priority == old_priority).\
           filter(Request.client_id == clientid).\
           filter(Request.id != request_id).\
           update({Request.client_priority: Request.client_priority + 1}, synchronize_session=False)
           old_priority=equeal[0].client_priority+1
           request_id=equeal[0].id
        else:
           old_priority=0
    return

# add new feature request to database 
def add_feature_request(form):
    title = form['title']
    description = form['description']
    client = form['client']
    priority = int(form['client_priority'])
    target_date = datetime.strptime(form['target_date'], '%Y-%m-%d')
    product_area= form['product_area']
    new_feature_request = Request(
        title=title,
        description=description,
        client_priority=priority,
        target_date=target_date,
        client_id=client,
        product_area_id=product_area
    )
    #update priorities for old request features if they are less than the new one
    change_priority(priority,client)

    #add new request
    db.session.add(new_feature_request)
    db.session.commit()
    return    


# deletes request
def delete_feature_request(id):
    db.session.query(Request).filter(Request.id == id).\
    delete(synchronize_session=False)
    db.session.commit()
    return


#update request
def update_feature_request(form):
    #get all data from form
    try:
        id = form['id']
        title = form['title']
        description = form['description']
        client = form['client']
        priority = int(form['client_priority'])
        target_date = datetime.strptime(form['target_date'], '%Y-%m-%d')
        product_area= form['product_area']

    
        #update priorities for old request features if they are less than the updated one
        change_priority(priority,client,id)
        #update request
        db.session.query(Request).filter(Request.id == id).\
        update({Request.title:title,
        Request.description:description,
        Request.title:title,
        Request.client_priority:priority,
        Request.client_id:client,
        Request.product_area_id:product_area
        }, synchronize_session=False)

        db.session.commit()
    except Exception as e:
        return jsonify({"error" : "Cannot update request"})  


#get all requests
def get_requests():
    try:
        requests=db.session.query(Request).join(Client, Request.client_id==Client.id).\
        join(ProductArea, Request.product_area_id==ProductArea.id).\
        add_columns(Request.id,Request.title,Request.description,Client.client_name,Request.\
        target_date,Request.client_priority,ProductArea.product_area_name).\
        order_by('Request.client_priority').all()
        return requests
    except Exception as e:
        return jsonify({"error" : "Cannot retreive data from database"})  
