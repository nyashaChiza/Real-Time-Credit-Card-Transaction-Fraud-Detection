from models import *

def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    return unique_list

def grouped_bar_graph_loader(user_id):
    
    cities= []
    fraud_t = []
    clean_t = []
    data = Data.query.filter_by(Client_id= user_id, ).all()
    for x in data:
        cities.append(x.location)
    cities = unique(cities)
    for x in cities:
        clean = Data.query.filter_by(Client_id= user_id, location= x, label=1 ).all()
        fraud = Data.query.filter_by(Client_id= user_id, location= x, label=0 ).all()
        fraud_t.append(len(fraud))
        clean_t.append(len(clean))
    return [cities,fraud_t,clean_t]
    
print(grouped_bar_graph_loader(1))
