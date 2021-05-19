
from flask_restful import Api
from flask import Flask, flash, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask import request
from river import metrics
from forms import *
from api import *
import  random 
#-----------------------------------------------------------------------

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = "the_real_is_back_the_ville_is_back"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/data.db"
db = SQLAlchemy(app)
metric = metrics.ROCAUC()

#-----------------------------------------------------------------------
 #-----------------------------------------------------------------------
    
class authenticatation(Resource):
    '''
    # 1.) get the client id and client token
    # .2) parse the information to the auth0 function
    # 3.) return client api key 
'''
    def get(self):
        client_id = request.args.get('client_id')
        client_token = request.args.get('client_token')
        return auth0(client_id, client_token)


class classification(Resource):
    '''
    #1.) authenticate
    #2.) get the data
    #3.) unpack the data
    #4.) call a data cleaning & transformation dunction
    #.5) fit data into a model
    #6.) return prediction or error message
    #.7) save data to database
    '''
    def get(self):
        try:
            seed1 = random.choice(['male', 'female'])
            data = {
            'account_age': request.args.get('account_age'),
            'avs': request.args.get('avs'),
            'amount': request.args.get('amount'),
            'card_number': request.args.get('card_number'),
            'location': request.args.get('location'),
            'account_type': request.args.get('account_type'),
            'bank': request.args.get('bank'),
            'transaction_time': request.args.get('transaction_time'),
            'connection_type': request.args.get('connection_type'),
            'cvv': request.args.get('cvv'),
            'browser': request.args.get('broswer'),
            'gender': request.args.get('gender'),
            'entry_type': request.args.get('entry_type'),
            'account_balance': request.args.get('account_balance'),
            'holder_age': request.args.get('holder_age')
            }
            
        except:
            return {'class': 'None', 'message':'missing data input, refer to docs'}
        
        security = auth2(request.args.get('api_key'))
        if security['status']:            
            #try :
             #   df = pd.DataFrame(data, index=[0])
             #   final = pipeline.transform(df)
            #except:
             #   return {'class': 'None', 'message':'invalid data input, refer to docs'}
            try:
                label = random.choice([0,1])
                prediction = model.predict_proba_one(data)
                model.learn_one(data, label)
                met = metric.update(prediction, label)
            except:
                seed = random.choice(['clean', 'fraudulent'])
                
                if seed == 'clean':
                    pred = False
                else:
                    pred = True
                save = Data(Client_id=security['id'], account_age=data['account_age'], avs = data['avs'], amount=data['amount'],
                    card_number=data['card_number'],   label=pred, location=data['location'], bank=data['bank'], account_type=data['account_type'],
                    transaction_time=data['transaction_time'],   connection_type=data['connection_type'], cvv=data['cvv'], broswer=data['browser'], gender=data['gender'],
                    entry_type=data['entry_type'],   account_balance=data['account_balance'], holder_age=data['holder_age'])            
                print('save')
                
                db.session.add(save)
                db.session.commit()
                return {'class': seed, 'message': 'classificaton successful'}
                #return {'class': 'None', 'message':'invalid input, refer to docs'}
            
        else:
            return {'class': 'None', 'message':'invalid API key'}

class analytics(Resource):
    '''
#1.) call authentication function
#2.) collect model infomation
#3.) package info and return data or erroe message 
'''
    def get(self):
        print('testing')
        security = auth2(request.args.get('api_key'))
        return security
        
#class data(Resource):
    '''
    #2.) query data from database
    #3.) package data into a csv file
    #4.) return file
    '''
class authenticatation(Resource):
    '''
    # 1.) get the client id and client token
    # .2) parse the information to the auth0 function
    # 3.) return client api key 
    '''

    def get(self):
        client_id = request.args.get('client_id')
        client_token = request.args.get('client_token')
        return auth0(client_id, client_token)


class analytics(Resource):
    '''
#1.) call authentication function
#2.) collect model infomation
#3.) package info and return data or erroe message 
'''
    def get(self):
        print('testing')
        security = auth2(request.args.get('api_key'))
        return security
        
#class data(Resource):
    
    #2.) query data from database
    #3.) package data into a csv file
    #4.) return file

#-----------------------------------------------------------------------

api.add_resource(classification, '/classification/')
api.add_resource(analytics, '/analytics/')
api.add_resource(authenticatation, '/authenticatation/')
#-----------------------------------------------------------------------

@app.route("/")
def index():
    template = 'home/index.html'
    return render_template(template)

@app.route("/signin")
def signin():
    form = SignIn()
    template = 'account/signin.html'
    alert = None
    return render_template(template, form=form, alert=alert)

@app.route("/about")
def about():
    template = 'info/about.html'
    return render_template(template)

@app.route("/contact")
def contact():
    template = 'info/contact.html'
    return render_template(template)

@app.route("/contact_process")
def contact_process():
    #template = 'info/contact.html'
    return index()

@app.route("/signup")
def signup():
    form = RegisterForm()
    template = 'account/signup.html'
    return render_template(template, form=form)

@app.route("/manage")
def manage():
    user = session['user_data']
    template = 'manage/home.html'
    return render_template(template, user=user)

@app.route("/signup_process", methods=['POST'])
def signup_process():
    if request.method == 'POST':
        user = User(name=request.form['name'], surname=request.form['surname'], address=request.form['address'], email=request.form['email'], password=request.form['password'])
        db.session.add(user)
        db.session.commit()
    return signin()

@app.route("/signin_process", methods=['POST'])
def signin_process():
     if request.method == 'POST':
        authentication = auth1(request.form['email'], request.form['password'])
        if  authentication[0]:
            session['user_data'] = [authentication[1].name, authentication[1].api_id, authentication[1].api_token, authentication[1].id ]
            #print(session['user'].name)
            return manage()
        else:
            alert = "login-failed"
            form = SignIn() 
            return  render_template('account/signin.html', form=form, alert=alert)
    
@app.route("/signout")
def signout():
    #template = 'account/signup.html'
    return index()

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404

@app.route("/transactions")
def transactions():
    data  = load_user_data(session['user_data'][3])
    template = 'manage/transactions.html'
    return render_template(template, data=data)

@app.route("/analysis")
def analysis():
    bar_data = bar_graph_loader(session['user_data'][3])
    grouped_data = grouped_bar_graph_loader(session['user_data'][3])
    stats = data_stats(session['user_data'][3])
    template = 'manage/analytics.html'
    return render_template(template, bar_data=bar_data, grouped_data = grouped_data, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)