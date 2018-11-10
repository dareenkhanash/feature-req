from flask import render_template
from feature_req import app, db
from datetime import datetime
from feature_req.models import Request, Client, ProductArea

@app.route('/')
def features():
    return render_template('feature-requests.html')

@app.route('/request',methods=['GET','POST'])
def add_request():
    new_request  = Request(
                title='title',
                description='description',
                client_priority=1,
                target_date=datetime.utcnow(),
                client_id=1,
                product_area_id=1
            )
    db.session.add(new_request)
    db.session.commit()
    return render_template('request.html')
@app.route('/request/<request_id>',methods=['GET','POST'])
def edit_request(request_id=None):
    return render_template('request.html',request_id=request_id)