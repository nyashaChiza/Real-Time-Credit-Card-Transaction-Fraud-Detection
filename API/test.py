from models import *

def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    return unique_list

def data_stats(user_id):
    data = Data.query.filter_by(Client_id= user_id ).all()
    return len(data)
    
print(data_stats(1))
