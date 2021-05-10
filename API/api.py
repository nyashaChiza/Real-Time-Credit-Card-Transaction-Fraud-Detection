
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
model = joblib.load("model/fraud_detection_classifier.pkl")

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
def bar_graph_loader(user_id):
    fraud = Data.query.filter_by(Client_id= user_id, label=0).all()
    clean = Data.query.filter_by(Client_id= user_id, label=1).all()
    return [len(fraud), len(clean)]
#-----------------------------------------------------------------------
def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    return unique_list
#-----------------------------------------------------------------------
def grouped_bar_graph_loader(user_id):
    
    cities= []
    fraud_t = []
    clean_t = []
    data = Data.query.filter_by(Client_id= user_id, ).all()
    for x in data:
        cities.append(x.location)
    cities = unique(cities)
    for x in cities:
        clean = Data.query.filter_by(Client_id= user_id, location= x, label=0 ).all()
        fraud = Data.query.filter_by(Client_id= user_id, location= x, label=1 ).all()
        fraud_t.append(len(fraud))
        clean_t.append(len(clean))
    return [cities, fraud_t, clean_t]
#-----------------------------------------------------------------------
def data_stats(user_id):
    data = Data.query.filter_by(Client_id= user_id ).all()
    return len(data)
#-----------------------------------------------------------------------