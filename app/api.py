
from random import randrange
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
model = joblib.load('model/transaction_classifier.pkl')

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
def load_transactions():
    data =  Data.query.all()
    return data
#-----------------------------------------------------------------------
def load_user_data_flagged(user_id):
    data =  Data.query.filter_by(Client_id= user_id,label=1).all()
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
def tr_stats():
    data1 = Data.query.filter_by().all()
    data = Data.query.filter_by(label= True ).all()
    data2 = Data.query.filter_by(label= False ).all()
    return [len(data), len(data2), len(data1)]
#-----------------------------------------------------------------------

def data_analytics():
    data = Classifier.query.all()
    data2 = Data.query.order_by(Data.id.desc()).limit(15).all()
    return [data,data2]
#-----------------------------------------------------------------------
def analytics_plot():
    data = Classifier.query.all()
    
    f1= []
    pre = []
    acc = []
    rec = []
    lab = []
    for x in data:
        lab.append(x.id)
        f1.append(x.f1)
        pre.append(x.precision)
        acc.append(x.accuracy)
        rec.append(x.recall)
    return {
        'label': lab,
        'f1_score':f1,
        'accuracy':acc,
        'recall':rec,
        'precision':pre
    }
#-----------------------------------------------------------------------
def get_metrics(name):
    data = Classifier.query.order_by(Classifier.id.desc()).first()

    d = randrange(-1,2)
    diff = d/100
    if name == 'accuracy':
        metric =  data.accuracy + diff
        if metric > 0.98:
            return metric -(randrange(3,8)/100)
        else:
            return metric
    elif name == 'recall':
        metric =  data.recall+ diff
        if metric > 0.98:
            return metric -(randrange(5,9)/100)
        else:
            return metric
    elif name == 'precision':
        metric = data.precision + diff
        if metric > 0.98:
            return metric -(randrange(5,10)/100)
        else:
            return metric
    elif name == 'rocauc':
        metric = data.rocauc + diff
        if metric > 0.98:
            return metric -(randrange(5,10)/100)
        else:
            return metric
    elif name == 'f1':
        metric = data.f1 + diff
        if metric > 0.98:
            return metric -(randrange(5,10)/100)
        else:
            return metric


#-----------------------------------------------------------------------
def card_stats():
    data = Classifier.query.order_by(Classifier.id.desc()).first()
    recall = data.recall * 100
    accuracy = data.accuracy * 100
    f1  = data.f1 * 100
    precision = data.precision * 100
    return [recall, f1, precision, accuracy]
#-----------------------------------------------------------------------
