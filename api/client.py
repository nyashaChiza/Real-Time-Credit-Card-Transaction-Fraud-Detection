import requests

link = 'http://127.0.0.1:5000/classification/'
link1 = 'http://127.0.0.1:5000/authenticatation/'
link2 = 'http://127.0.0.1:5000/analytics/'

api_key = 'd7311caa7e3c8e6db309d9fe617fff192bddc5bd8877686d2cbdbeaf05d77aa6766d84a2716f8dc3427e91c34a6e24cc'
w_api_key = 'd7311caga7e3c8e6db309d9fe617fff192bddc5bd8877686d2cbdbeaf05d77aa6766d84a2716f8dc3427e91c34a6e24cc'

data1 = {
    'api_key':api_key,
    'account_age':1305,
    'avs':8475,
    'amount':1000,
    'card_number':1272,
    'location':'Kadoma',
    'account_type':'Credit',
    'bank':'Standard Bank',
    'connection_type':'http',
    'cvv':'y',
    'broswer':'Mozilla/5.0 ',
    'gender':'female',
    'entry_type':'chip',
    'transaction_time':64,
    'account_balance':674,
    'holder_age':28
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
auth = {
   'client_id': '1fddd7bd47a7f9efcd15a602bd6462e1',
    'client_token': '9c10eb2b52ffa06a1d3e3369f833f74f'
}

#obtaining API KEY
#resp = requests.get(link1, auth)
#print(resp.json())

#testing classification with wrong key
#resp = requests.get(link, data3)
#print(resp.json())

#classifying transaction 1
#resp = requests.get(link, data1)
#print(resp.json())

#classifying transaction 2
resp = requests.get(link, data2)
print(resp.json())
