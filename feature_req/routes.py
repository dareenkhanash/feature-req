from flask import render_template
from feature_req import app
from feature_req.models import Request, Client, ProductArea

@app.route('/')
def features():
    return render_template('feature-requests.html')


@app.route('/request',methods=['GET','POST'])
@app.route('/request/<request_id>',methods=['GET','POST'])
def editrRequest(request_id=None):
    return render_template('request.html',request_id=request_id)