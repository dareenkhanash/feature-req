from flask import render_template,request,jsonify
from feature_req import app, db
from datetime import datetime
from feature_req.models import Request, Client, ProductArea
from feature_req.utils import add_feature_request,delete_feature_request,update_feature_request,get_requests
from feature_req.schema import RequestSchema

#render main page
@app.route('/')
def features():
    return render_template('feature-requests.html')


#retuens feature requests
@app.route('/getData')
def get_features():
    requests=get_requests()
    if requests:
       request_schema=RequestSchema(many=True)
       output=request_schema.dump(requests).data
       return jsonify({'requests':output})
    else:
       return jsonify({'messeage':'no requests'})



# route to add new feature request
@app.route('/request',methods=['GET','POST'])
def add_request():
    if request.method == 'POST':
       #passes request information from form
       add_feature_request(request.form)
    return render_template('request.html')


@app.route('/request/delete/<int:request_id>',methods=['DELETE'])
def delete_request(request_id):
    print("jhhhhh")
    if request.method == 'DELETE':
        if request_id:
           delete_feature_request(request_id)
           return jsonify({"message": "deleted."})
        else:
            return jsonify({"message": "no requestId."})
    return jsonify({"message": "no requestId."})


@app.route('/request/<int:request_id>',methods=['GET','POST','PUT'])
def edit_request(request_id):
    request=db.session.query(Request).filter(Request.id == request_id).all()
    return render_template('edit-request.html',request=request)


# route to add new feature request
@app.route('/request/update',methods=['DELETE','POST'])
def update_request():
    if request.method == 'POST':
       #passes request information from form
       update_feature_request(request.form)
    return jsonify({"message": "done"})
    