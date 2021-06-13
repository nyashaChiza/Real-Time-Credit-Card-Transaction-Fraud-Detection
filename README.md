Detecting Credit Card Fraud using ensemble methods in near real-time

# Credit Card Fraud Detection using ensemble methods in Zimbabwe


# The Problem:

Both the card issuer and the merchant are liable in the event of fraud, most of the fraud detection efforts are being directed towards the card issuer (the Bank) and merchants are left with no real tools to protect themselves.  Most local SME’s still use rule-based techniques to detect fraud. This solution was relevant back then when Zimbabwe had a stable economy, now these complex rules have to be constantly be rewritten at every turn to avoid incorrect classification of transactions. Bigger organisations can afford develop in house solutions that are not available to the public leaving SME’s exposed to attackers. As a result of this most businesses in Zimbabwe hesitate in the adoption of technology in their business processes because of fear of the risks associated with transacting online. 



# THE OBJECTIVE: 

To build a fraud detection classifier that, given a new transaction, can tell us if it is fraudulent or not with a correspondent confidence level. # Which are our classes? : 

1) “0” label = transaction is NOT fraudulent
2) “1” label (transaction IS fraudulent)

# EXPECTED RESULTS:

1)	To develop a transaction classification model with at least a 80% accuracy rate
2) To provide a risk score for each transaction


# METHODOLOGY:
In order to get the best performance the model has to be trained in conditions similiar to the production environment,
so the system will follow the kaffa pattern where the machine learning model learns and predicts from a stream of inputs.
The data will be handles as a stream using the [River-ml](https://riverml.xyz/latest/) incremental learning python package and will make use of the adaptive random forest algorithm to incrementally learn from a data. 

# Instalation:
1) Create a virtual enviroment wit virtualenv evn
2) pip install -r requirements.txt
3.) navigation to the API folder and run "py app.py"
4.) go to "localhost:5000" on your browser

# Use:
The system is based on a REST API with the following endpoints
	1.) "localhost:5000/authentication"
	2.) "localhost:5000/classification"
	3.) "localhost:5000/analytics"
	4.) "localhost:5000/data"
All these endpoints can be accessed using a get request, and they all require the API key to authenticate calls except for the authentication endpoint

# Authentication
The system makes use of a token based authentication mechanism. When a user create an account and login, they are assigned a client id and token in the web application.
They use these credentials to obtain the API KEY. Below is an example of the script

		''' 
		import requests
		link = 'http://127.0.0.1:5000/authenticatation/'
		auth = {
   			'client_id': '04e7a844acb1606b5d59aeaf0e5a2259',
    			'client_token': '7aa241b36cb05cf974ae869ca8698cd7'
			}
		resp = requests.get(link, auth)
		print(resp.json())

		'''
The sample script above with print out the API key

# Classification
This endpoint consumes transaction details, classifies the transaction and returns a classification report as shown in the script below

		''' 
		import requests
		link = 'http://127.0.0.1:5000/classification/'
		data = {
    			'api_key': 404209da0f1b6200a24b19782048fdb08b3fa4e13907778fcbec147672913gut3d8d6cb910fa77315c416ccc0a3,
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

		resp = requests.get(link, data)
		print(resp.json())

		'''
the expected response:
			{'class': ‘clean’, risk score:0.67 'message': 'classification successful'}


	
#Analytics
This endpoint requires the API key for authentication as shown by the script below,

		''' 
		import requests
		link = 'http://127.0.0.1:5000/analytics/'
		data = {
    			'api_key':404209da0f1b6200a24b19782048fdb08b3fa4e13907778fcbec147672913gut3d8d6cb910fa77315c416ccc0a3,
			}

		resp = requests.get(link, data)
		print(resp.json())

		'''
the expected response:
			{
		‘f1_score’: 0.87,
		‘recall’: 0.91,
		‘precision’: 0.86,
		‘accuracy’: 0.92,
		‘transactions processed’: 10000,
		‘Normal transactions’: 9500,
‘		Fraudulent transactions’: 500,
}

#Data
This endpoint requires the API key for authentication and it returns the clients data in a pandas dataFrame format as shown by the script below,
		''' 
		import requests
		link = 'http://127.0.0.1:5000/data/'
		data = {
    			'api_key':404209da0f1b6200a24b19782048fdb08b3fa4e13907778fcbec147672913gut3d8d6cb910fa77315c416ccc0a3,
			}

		resp = requests.get(link, data)
		print(resp.json())

		'''
