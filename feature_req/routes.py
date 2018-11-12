from flask import render_template,request,jsonify
from feature_req import app, db
from datetime import datetime
from feature_req.models import Request, Client, ProductArea
from feature_req.utils import add_feature_request
from feature_req.schema import RequestSchema

#render main page
@app.route('/')
def features():
    return render_template('feature-requests.html')


#retuens feature requests
@app.route('/getData')
def get_features():
    requests=Request.query.all()
    request_schema=RequestSchema(many=True)
    output=request_schema.dump(requests).data
    return jsonify({'requests':output})

# route to add new feature request
@app.route('/request',methods=['GET','POST'])
def add_request():
    if request.method == 'POST':
       #passes request information from form
       add_feature_request(request.form)
    return render_template('request.html')


@app.route('/request/<request_id>',methods=['GET','POST'])
def edit_request(request_id=None):
    return render_template('request.html',request_id=request_id)