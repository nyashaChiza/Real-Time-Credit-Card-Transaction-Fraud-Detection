
from flask_restful import Api
from flask import Flask, flash, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask import request
from forms import *
from api import *

#-----------------------------------------------------------------------

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = "closed_caskets_as_usual"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/data.db"
db = SQLAlchemy(app)

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
            data = {
            'age': request.args.get('age'),
            'asv': request.args.get('asv'),
            'Amount': request.args.get('Amount'),
            'CardNo': request.args.get('cardNo'),
            'location': request.args.get('location'),
            'card_type': request.args.get('card_type'),
            'bank': request.args.get('bank')
            }
        except:
            return {'class': 'None', 'message':'missing data input, refer to docs'}
        
        security = auth2(request.args.get('api_key'))
        if security['status']:            
            try :
                df = pd.DataFrame(data, index=[0])
                final = pipeline.transform(df)
            except:
                return {'class': 'None', 'message':'invalid data input, refer to docs'}
            try:
                prediction  = model.predict(final)
            except:
                return {'class': 'None', 'message':'model failure, refer to docs'}
            
            if prediction[0]:
                pred = "fraudulent"
            else:
                pred = 'normal'
            save = Data(Client_id=security['id'],age=data['age'], asv = data['asv'], amount=data['Amount'], cardNo=data['CardNo'],   label=prediction[0], location=data['location'], bank=data['bank'], card_type=data['card_type'] )
            db.session.add(save)
            db.session.commit()
            return {'class': pred, 'message': 'classificaton successful'}
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


class classification(Resource):
    '''#1.) authenticate
    #2.) get the data
    #3.) unpack the data
    #4.) call a data cleaning & transformation dunction
    #.5) fit data into a model
    #6.) return prediction or error message
    #.7) save data to database
    '''
    def get(self):
        try:
            data = {
            'age': request.args.get('age'),
            'asv': request.args.get('asv'),
            'Amount': request.args.get('Amount'),
            'CardNo': request.args.get('cardNo'),
            'location': request.args.get('location'),
            'card_type': request.args.get('card_type'),
            'bank': request.args.get('bank')
            }
        except:
            return {'class': 'None', 'message':'missing data input, refer to docs'}
        
        security = auth2(request.args.get('api_key'))
        if security['status']:
            
            try :
                df = pd.DataFrame(data, index=[0])
                final = pipeline.transform(df)
            
            except:
                return {'class': 'None', 'message':'invalid data input, refer to docs'}
            try:
                prediction  = model.predict(final)
            except:
                return {'class': 'None', 'message':'model failure, refer to docs'}
            
            if prediction[0]:
                pred = "fraudulent"
            else:
                pred = 'normal'
            save = Data(Client_id=security['id'],age=data['age'], asv = data['asv'], amount=data['Amount'], cardNo=data['CardNo'],   label=prediction[0], location=data['location'], bank=data['bank'], card_type=data['card_type'] )
            db.session.add(save)
            db.session.commit()
            return {'class': pred, 'message': 'classificaton successful'}
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
    template = 'manage/home.html'
    return render_template(template)

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
            
            session['user'] = 1
            return render_template('manage/home.html', user=authentication[1])
        else:
            alert = "login-failed"
            form = SignIn() 
            return  render_template('account/signin.html', form=form, alert=alert)
    
@app.route("/signout")
def signout():
    #template = 'account/signup.html'
    return index()

@app.route("/transactions")
def transactions():
    data  = load_user_data(session['user'])
    template = 'manage/monitor/transactions.html'
    return render_template(template, data=data)

@app.route("/analysis")
def analysis():
    j = '''{"Month":{"0":"1949-01","1":"1949-02","2":"1949-03","3":"1949-04","4":"1949-05","5":"1949-06","6":"1949-07","7":"1949-08","8":"1949-09","9":"1949-10","10":"1949-11","11":"1949-12","12":"1950-01","13":"1950-02","14":"1950-03","15":"1950-04","16":"1950-05","17":"1950-06","18":"1950-07","19":"1950-08","20":"1950-09","21":"1950-10","22":"1950-11","23":"1950-12","24":"1951-01","25":"1951-02","26":"1951-03","27":"1951-04","28":"1951-05","29":"1951-06","30":"1951-07","31":"1951-08","32":"1951-09","33":"1951-10","34":"1951-11","35":"1951-12","36":"1952-01","37":"1952-02","38":"1952-03","39":"1952-04","40":"1952-05","41":"1952-06","42":"1952-07","43":"1952-08","44":"1952-09","45":"1952-10","46":"1952-11","47":"1952-12","48":"1953-01","49":"1953-02","50":"1953-03","51":"1953-04","52":"1953-05","53":"1953-06","54":"1953-07","55":"1953-08","56":"1953-09","57":"1953-10","58":"1953-11","59":"1953-12","60":"1954-01","61":"1954-02","62":"1954-03","63":"1954-04","64":"1954-05","65":"1954-06","66":"1954-07","67":"1954-08","68":"1954-09","69":"1954-10","70":"1954-11","71":"1954-12","72":"1955-01","73":"1955-02","74":"1955-03","75":"1955-04","76":"1955-05","77":"1955-06","78":"1955-07","79":"1955-08","80":"1955-09","81":"1955-10","82":"1955-11","83":"1955-12","84":"1956-01","85":"1956-02","86":"1956-03","87":"1956-04","88":"1956-05","89":"1956-06","90":"1956-07","91":"1956-08","92":"1956-09","93":"1956-10","94":"1956-11","95":"1956-12","96":"1957-01","97":"1957-02","98":"1957-03","99":"1957-04","100":"1957-05","101":"1957-06","102":"1957-07","103":"1957-08","104":"1957-09","105":"1957-10","106":"1957-11","107":"1957-12","108":"1958-01","109":"1958-02","110":"1958-03","111":"1958-04","112":"1958-05","113":"1958-06","114":"1958-07","115":"1958-08","116":"1958-09","117":"1958-10","118":"1958-11","119":"1958-12","120":"1959-01","121":"1959-02","122":"1959-03","123":"1959-04","124":"1959-05","125":"1959-06","126":"1959-07","127":"1959-08","128":"1959-09","129":"1959-10","130":"1959-11","131":"1959-12","132":"1960-01","133":"1960-02","134":"1960-03","135":"1960-04","136":"1960-05","137":"1960-06","138":"1960-07","139":"1960-08","140":"1960-09","141":"1960-10","142":"1960-11","143":"1960-12"},"#Passengers":{"0":112,"1":118,"2":132,"3":129,"4":121,"5":135,"6":148,"7":148,"8":136,"9":119,"10":104,"11":118,"12":115,"13":126,"14":141,"15":135,"16":125,"17":149,"18":170,"19":170,"20":158,"21":133,"22":114,"23":140,"24":145,"25":150,"26":178,"27":163,"28":172,"29":178,"30":199,"31":199,"32":184,"33":162,"34":146,"35":166,"36":171,"37":180,"38":193,"39":181,"40":183,"41":218,"42":230,"43":242,"44":209,"45":191,"46":172,"47":194,"48":196,"49":196,"50":236,"51":235,"52":229,"53":243,"54":264,"55":272,"56":237,"57":211,"58":180,"59":201,"60":204,"61":188,"62":235,"63":227,"64":234,"65":264,"66":302,"67":293,"68":259,"69":229,"70":203,"71":229,"72":242,"73":233,"74":267,"75":269,"76":270,"77":315,"78":364,"79":347,"80":312,"81":274,"82":237,"83":278,"84":284,"85":277,"86":317,"87":313,"88":318,"89":374,"90":413,"91":405,"92":355,"93":306,"94":271,"95":306,"96":315,"97":301,"98":356,"99":348,"100":355,"101":422,"102":465,"103":467,"104":404,"105":347,"106":305,"107":336,"108":340,"109":318,"110":362,"111":348,"112":363,"113":435,"114":491,"115":505,"116":404,"117":359,"118":310,"119":337,"120":360,"121":342,"122":406,"123":396,"124":420,"125":472,"126":548,"127":559,"128":463,"129":407,"130":362,"131":405,"132":417,"133":391,"134":419,"135":461,"136":472,"137":535,"138":622,"139":606,"140":508,"141":461,"142":390,"143":432},"forecast":{"0":328.4562121125,"1":329.5093575474,"2":319.6742927877,"3":316.3808034335,"4":309.9364494471,"5":305.6898260955,"6":300.6505412937,"7":296.4535901474,"8":292.1704094466,"9":288.2951494982,"10":284.5341822336,"11":281.0317790465,"12":277.6904022118,"13":274.5475549087,"14":271.5667621469,"15":268.7534246808,"16":266.0905303506,"17":263.5742587792,"18":261.1941966216,"19":258.9442690715,"20":256.8166410446,"21":254.8050638697,"22":252.9029862677,"23":251.1045703963,"24":249.4040987194,"25":247.7962747991,"26":246.27602993,"27":244.8386052368,"28":243.4794823925,"29":242.1943995732,"30":240.9793213716,"31":239.830435398,"32":238.7441351763,"33":237.7170116749,"34":236.7458410267,"35":235.8275752875,"36":234.9593323836,"37":234.1383873362,"38":233.3621635591,"39":232.6282248553,"40":231.9342677246,"41":231.2781141594,"42":230.6577047951,"43":230.0710924547,"44":229.5164360324,"45":228.9919947184,"46":228.4961225337,"47":228.0272631648,"48":227.5839450787,"49":227.1647769049,"50":226.7684430683,"51":226.39369966,"52":226.0393705337,"53":225.7043436142,"54":225.3875674066,"55":225.088047697,"56":224.8048444314,"57":224.5370687655,"58":224.2838802755,"59":224.0444843195,"60":223.8181295444,"61":223.6041055272,"62":223.4017405453,"63":223.2103994686,"64":223.029481766,"65":222.8584196203,"66":222.6966761466,"67":222.5437437068,"68":222.3991423167,"69":222.2624181394,"70":222.1331420608,"71":222.0109083432,"72":221.8953333513,"73":221.7860543487,"74":221.682728359,"75":221.5850310899,"76":221.4926559147,"77":221.4053129103,"78":221.3227279476,"79":221.2446418304,"80":221.1708094826,"81":221.1009991785,"82":221.0349918158,"83":220.972580228,"84":220.9135685339,"85":220.857771523,"86":220.8050140744,"87":220.7551306068,"88":220.7079645591,"89":220.6633678987,"90":220.6212006575,"91":220.581330492,"92":220.543632268,"93":220.5079876684,"94":220.4742848212,"95":220.4424179487,"96":220.4122870355,"97":220.3837975147,"98":220.3568599708,"99":220.3313898593,"100":220.3073072413,"101":220.2845365325,"102":220.2630062663,"103":220.2426488691,"104":220.2234004485,"105":220.2052005925,"106":220.1879921802,"107":220.1717212023,"108":220.1563365919,"109":220.1417900636,"110":220.1280359627,"111":220.1150311214,"112":220.1027347235,"113":220.0911081762,"114":220.0801149894,"115":220.0697206603,"116":220.0598925661,"117":220.0505998608,"118":220.041813379,"119":220.033505544,"120":220.0256502812,"121":220.0182229368,"122":220.0112001996,"123":220.0045600285,"124":219.9982815831,"125":219.9923451583,"126":219.9867321224,"127":219.9814248586,"128":219.97640671,"129":219.9716619268,"130":219.9671756173,"131":219.9629337012,"132":219.958922865,"133":219.9551305206,"134":219.9515447654,"135":219.9481543456,"136":219.9449486201,"137":219.9419175277,"138":219.9390515551,"139":219.9363417074,"140":219.9337794796,"141":219.9313568301,"142":219.9290661553,"143":219.9269002659}}'''
    data = json.loads(j)
    data = list(data['forecast'].values())
    template = 'manage/forecast/analytics.html'
    return render_template(template, data=data[4:15])

if __name__ == '__main__':
    app.run(debug=True)