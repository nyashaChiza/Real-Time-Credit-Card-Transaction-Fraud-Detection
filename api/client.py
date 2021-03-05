import requests

link = 'http://127.0.0.1:5000/classification/'
link2 = 'http://127.0.0.1:5000/authenticatation/'
link3 = 'http://127.0.0.1:5000/analytics/'

api_key = '7662c2e8cd4543ffaf920c5889c0e0c26aac16b971cdce96bd8a79889d21c96cf5c978e215ec5557028f2b562ddcd755'

data = {
    'api_key': api_key,
    'age':16,
    'cv_data':1,
    'asv':1245,
    'cvv':567,
    'Amount':1330,
    'cardNo':424,
    'location':'Marondera',
    'card_type':'Credit',
    'bank':'FBC Bank'
}

data2 = {
   'client_id': '6480d7790a0751d57225573faa3b5121',
    'client_token': 'ff49ee3824cdc7c2ae1940229bbd0d9d'
 

}

auth = {
    'api_key': api_key
}
resp = requests.get(link, data)
print(resp.json())

