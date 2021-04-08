
from flask_restful import Resource
import numpy as np
import pandas as pd
import joblib
import secrets
import os
import json
from werkzeug.utils import secure_filename
from flask import request
from models import *


#-----------------------------------------------------------------------
model = joblib.load("model/fraud_detection_model.pkl")
pipeline = joblib.load("pipeline/pipeline.pkl")
#-----------------------------------------------------------------------

def auth0(client_id, client_token):
    login_Object =  User.query.filter_by(api_id = client_id, api_token=client_token).first()
    if login_Object == None:
        return {'message': 'invalid client credentials  '}
    else:
        client_Object =  Client.query.filter_by(id = login_Object.id).first()
        if client_Object == None:
            client = Client(id=login_Object.id, api_key = secrets.token_hex(48) )
            db.session.add(client)
            db.session.commit()
            c_Object =  Client.query.filter_by(id = login_Object.id).first()
            return {'api key': c_Object.api_key}
        else:
            c_Object =  Client.query.filter_by(id = login_Object.id).first()
            return {'api key': c_Object.api_key}            
 #-----------------------------------------------------------------------
def auth2(api_key):
    c_Object =  Client.query.filter_by(api_key = api_key).first()
    if c_Object == None:
        return {'status': False, 'id': None}
    else:
        return {'status': True, 'id': c_Object.id }
#-----------------------------------------------------------------------
def auth1( auth_email, auth_pass):
        login_Object =  User.query.filter_by(email = auth_email, password=auth_pass).first()
        if login_Object  == None:
                form = SignIn() 
                return [False, None] 
        else:   
                return [True, login_Object] 
#-----------------------------------------------------------------------
def load_user_data(user_id):
    data =  Data.query.filter_by(Client_id= user_id).all()
    return data
#-----------------------------------------------------------------------
            

