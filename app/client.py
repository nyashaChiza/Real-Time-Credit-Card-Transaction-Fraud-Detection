import requests
import random

link = 'http://127.0.0.1:5000/classification/'
link1 = 'http://127.0.0.1:5000/authenticatation/'
link2 = 'http://127.0.0.1:5000/analytics/'
link3 = 'http://127.0.0.1:5000/data/'

api_key = '404209da0f1b6200a24b19782048fd090b08b3fa4e13a4907778fcbec147672913f133d8d6cb910fa77315c416ccc0a3'
w_api_key = 'd7311caga7e3c8e6db309d9fe617fff192bddc5bd8877686d2cbdbeaf05d77aa6766d84a2716f8dc3427e91c34a6e24cc'
seed1 = random.choice(['male', 'female'])
data1 = {
    'api_key':api_key,
    'account_age':95,
    'avs':1555,
    'amount':100,
    'card_number':8221,
    'location':'Kwekwe',
    'answer': 1,
    'account_type':'Credit',
    'bank':'Steward bank',
    'connection_type':'https',
    'cvv':'y',
    'broswer':'Mozilla/5.0',
    'gender':'male',
    'entry_type':'chip',
    'transaction_time':294,
    'account_balance':47,
    'holder_age':46
}
data4 = {
    'api_key':api_key,
}

data3 = {
    'api_key': w_api_key,
    'account_age':305,
    'avs':475,
    'amount':15000,
    'card_number':8472,
    'location':'Harare',
    'account_type':'Credit',
    'bank':'FBC Bank',
    'connection_type':'https',
    'cvv':'n',
    'broswer':'Mozilla/5.0 ',
    'gender':'male',
    'entry_type':'chip',
    'transaction_time':54,
    'account_balance':2365,
    'holder_age':32
}
data2 = {
    'api_key': api_key,
    'account_age':79,
    'avs':467,
    'amount':6700,
    'card_number':3474,
    'location':'Kadoma',
    'account_type':'Deedit',
    'bank':'Banc ABC',
    'connection_type':'https',
    'cvv':'n',
    'broswer':'Mozilla/5.0 ',
    'gender':'male',
    'entry_type':'magnetic strip',
    'transaction_time':304,
    'account_balance':4640,
    'holder_age':21
}
auth = {
   'client_id': '04e7a844acb1606b5d59aeaf0e5a2259',
    'client_token': '7aa241b36cb05cf974ae869ca8698cd7'
}

#obtaining API KEY
#resp = requests.get(link1, auth)
#print(resp.json())

#testing classification with wrong key
#resp = requests.get(link, data3)
#print(resp.json())

#classifying transaction 1
#resp = requests.get(link, data2)
#print(resp.json())

#classifying transaction 2
#resp = requests.get(link, data2)
#print(resp.json())

#obtaining analytics 
resp = requests.get(link2, data4)
print(resp.json())

#obtaining transaction data 
#resp = requests.get(link3, data4)
#print(resp.json())