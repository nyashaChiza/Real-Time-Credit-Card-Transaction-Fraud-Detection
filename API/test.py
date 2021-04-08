from models import *

def load_user_data(user_id):
    return Data.query.filter_by(Client_id = user_id ).all()

data = load_user_data(1) 
#for x in data:
print(len(data))