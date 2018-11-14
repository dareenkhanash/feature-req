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


#return feature requests
@app.route('/getData')
def get_features():
    try:
        requests=get_requests()
        if requests:
            request_schema=RequestSchema(many=True)
            output=request_schema.dump(requests).data
            return jsonify({'requests':output})
        else:
            return jsonify({'messeage':'no requests'})
    except Exception as e:
        return jsonify({'error': "Cannot Get Data"})  



# route to add new feature request
@app.route('/request',methods=['GET','POST'])
def add_request():
    try:
        if request.method == 'POST':
            #passes request information from form
            add_feature_request(request.form)
        return render_template('request.html')
    except Exception as e:
        return jsonify({'error': "Cannot Get Data"})


#route to delete request
@app.route('/request/delete/<int:request_id>',methods=['DELETE'])
def delete_request(request_id):
    try:
        if request.method == 'DELETE':
            if request_id:
            delete_feature_request(request_id)
            return jsonify({"message": "Request deleted"})
            else:
                return jsonify({"error": "No Request Id"})
    except Exception as e:
        return jsonify({'error': "Cannot delete request"})

#go to update route
@app.route('/request/<int:request_id>',methods=['GET','POST','PUT'])
def edit_request(request_id):
    try:
        request=db.session.query(Request).filter(Request.id == request_id).all()
        return render_template('edit-request.html',request=request)
    except Exception as e:
        return jsonify({'error': "Cannot go to update route"})


# route to update feature request
@app.route('/request/update',methods=['POST'])
def update_request():
    try:
        if request.method == 'POST':
        #passes request information from form
        update_feature_request(request.form)
        return jsonify({"message": "done"})
    except Exception as e:
        return jsonify({'error': "Cannot update request"})

       

    