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
