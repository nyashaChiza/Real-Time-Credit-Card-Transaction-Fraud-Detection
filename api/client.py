import requests

link = 'http://127.0.0.1:5000/classification/'
link1 = 'http://127.0.0.1:5000/authenticatation/'
link2 = 'http://127.0.0.1:5000/analytics/'

api_key = 'd7311caa7e3c8e6db309d9fe617fff192bddc5bd8877686d2cbdbeaf05d77aa6766d84a2716f8dc3427e91c34a6e24cc'

data = {
    'api_key': api_key,
    'age':760,
    'asv':5925,
    'Amount':18330,
    'cardNo':2578,
    'location':'Harare',
    'card_type':'Credit',
    'bank':'FBC Bank'
}

data2 = {
   'client_id': '1fddd7bd47a7f9efcd15a602bd6462e1',
    'client_token': '9c10eb2b52ffa06a1d3e3369f833f74f'
}


resp = requests.get(link1, data2)
print(resp.json())

