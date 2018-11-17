import os, sys
import unittest
import tempfile
import feature_req
from flask import json,jsonify
from datetime import datetime
from feature_req.app import create_app
from feature_req.models import Request, Client, ProductArea
from feature_req.models import db


class FeatureRequestTestCase(unittest.TestCase):
#test app
    def setUp(self):
        self.app = create_app('test_config')
        self.app_client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = Client(client_name='Client A')
        self.productarea = ProductArea(product_area_name='Policies')
        self.request = Request(
            title='Title Test',
            description='Description',
            target_date=datetime.strptime('2018-11-13', '%Y-%m-%d'),
            client_priority=1,
            product_area_id=1,
            client_id=1
        )
        
        db.create_all()
        db.session.add(self.client)
        db.session.add(self.productarea)
        db.session.add(self.request)
        self.request = db.session.query(Request).first()

    def tearDown(self):
        db.session.close()
        db.drop_all()
        self.app_context.pop()

#test routes
    #test root status code
    def test_root_Route(self):
        resp = self.app_client.get('/')
        self.assertEqual(200, resp.status_code)
    #test getdData route status code 
    def test_getData_Route(self):
        resp = self.app_client.get('/getData')
        self.assertEqual(200, resp.status_code)
   
   

if __name__ == '__main__':
    unittest.main()