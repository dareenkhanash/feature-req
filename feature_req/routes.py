from flask import Blueprint, render_template,request,jsonify
from feature_req.app import db
from datetime import datetime
from feature_req.models import Request, Client, ProductArea
from feature_req.utils import add_feature_request,delete_feature_request,update_feature_request,get_requests
from feature_req.schema import RequestSchema


feature_req=Blueprint('feature_req',__name__)   


#render main page
@feature_req.route('/')
def features():
    return render_template('feature-requests.html')



#return feature requests
@feature_req.route('/getData')
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
        return jsonify("error: {0}".format(e))  



# route to add new feature request
@feature_req.route('/request',methods=['GET','POST'])
def add_request():
    try:
        if request.method == 'POST':
            #passes request information from form
            add_feature_request(request.form)
        return render_template('request.html')
    except Exception as e:
        return jsonify("error: {0}".format(e))


#route to delete request
@feature_req.route('/request/delete/<int:request_id>',methods=['DELETE'])
def delete_request(request_id):
    try:
        if request.method == 'DELETE':
            if request_id:
               delete_feature_request(request_id)
               return jsonify({"message": "Request deleted"})
            else:
               return jsonify({"error": "No Request Id"})
    except Exception as e:
        return jsonify("error: {0}".format(e))

#go to update route
@feature_req.route('/request/<int:request_id>')
def edit_request(request_id):
    try:
        request=db.session.query(Request).filter(Request.id == request_id).all()
        return render_template('edit-request.html',request=request)
    except Exception as e:
        return jsonify("error: {0}".format(e))


# route to update feature request
@feature_req.route('/request/update',methods=['POST'])
def update_request():
    try:
        if request.method == 'POST':
        #passes request information from form
           update_feature_request(request.form)
           return jsonify({"message": "done"})
    except Exception as e:
        return jsonify("error: {0}".format(e))

       

    