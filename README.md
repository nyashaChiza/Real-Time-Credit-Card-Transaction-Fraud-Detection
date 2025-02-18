# **Credit Card Fraud Detection using Ensemble Methods in Zimbabwe**  

## **Problem Statement**  
Both the card issuer and the merchant are liable in the event of fraud. However, most fraud detection efforts are focused on the card issuer (banks), leaving merchants with limited tools for protection. Many local SMEs still rely on outdated rule-based techniques to detect fraud.  

Previously, these rule-based techniques were sufficient, but with Zimbabwe’s evolving economy, businesses must constantly rewrite complex rules to avoid misclassification of transactions. While larger organizations can develop in-house fraud detection solutions, SMEs lack the resources, leaving them vulnerable. Consequently, many businesses hesitate to adopt online payment technologies due to fraud risks.  

## **Objective**  
To build a fraud detection classifier that, given a new transaction, can determine whether it is fraudulent with a corresponding confidence score.  

### **Classification Labels:**  
- **"0"** = Transaction is NOT fraudulent  
- **"1"** = Transaction IS fraudulent  

## **Expected Results**  
1) Develop a transaction classification model with at least **80% accuracy**.  
2) Provide a **risk score** for each transaction.  

## **Methodology**  
To achieve optimal performance, the model is trained in conditions similar to production using a **stream-based approach**.  

The system follows the **Kafka pattern**, where the machine learning model continuously learns and predicts from incoming transaction streams. This is achieved using [River-ml](https://riverml.xyz/latest/), an incremental learning Python package, which applies the **Adaptive Random Forest algorithm** to update the model in real time.  

---

## **Installation Instructions**  
Follow these steps to set up and run the Flask API:  

### **1. Set Up a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3. Start the Flask API**  
Navigate to the API folder and run:  
```bash
python app.py
```

### **4. Access the API**  
Open your browser and go to:  
```
http://localhost:5000
```

---

## **API Endpoints**  

### **1. Authentication**  
- Endpoint: `POST /authentication`  
- Description: Generates an API key for authenticated users.  
- Request Example:  
```python
import requests

url = 'http://127.0.0.1:5000/authentication/'
auth = {
    'client_id': '04e7a844acb1606b5d59aeaf0e5a2259',
    'client_token': '7aa241b36cb05cf974ae869ca8698cd7'
}

response = requests.get(url, auth)
print(response.json())
```
- **Response:**  
```json
{
    "api_key": "404209da0f1b6200a24b19782048fdb08b3fa4e13907778fcbec147672913..."
}
```

---

### **2. Transaction Classification**  
- Endpoint: `POST /classification`  
- Description: Accepts transaction details and classifies them as fraudulent or legitimate.  
- Request Example:  
```python
import requests

url = 'http://127.0.0.1:5000/classification/'
data = {
    'api_key': 'your_api_key_here',
    'account_age': 305,
    'avs': 475,
    'amount': 15000,
    'card_number': 8472,
    'location': 'Harare',
    'account_type': 'Credit',
    'bank': 'FBC Bank',
    'connection_type': 'https',
    'cvv': 'n',
    'browser': 'Mozilla/5.0',
    'gender': 'male',
    'entry_type': 'chip',
    'transaction_time': 54,
    'account_balance': 2365,
    'holder_age': 32
}

response = requests.get(url, data)
print(response.json())
```
- **Response:**  
```json
{
    "class": "clean",
    "risk_score": 0.67,
    "message": "classification successful"
}
```

---

### **3. Analytics**  
- Endpoint: `GET /analytics`  
- Description: Provides performance metrics of the fraud detection model.  
- Request Example:  
```python
import requests

url = 'http://127.0.0.1:5000/analytics/'
data = {'api_key': 'your_api_key_here'}

response = requests.get(url, data)
print(response.json())
```
- **Response:**  
```json
{
    "f1_score": 0.87,
    "recall": 0.91,
    "precision": 0.86,
    "accuracy": 0.92,
    "transactions_processed": 10000,
    "normal_transactions": 9500,
    "fraudulent_transactions": 500
}
```

---

### **4. Data Retrieval**  
- Endpoint: `GET /data`  
- Description: Retrieves the client’s transaction data in **Pandas DataFrame** format.  
- Request Example:  
```python
import requests

url = 'http://127.0.0.1:5000/data/'
data = {'api_key': 'your_api_key_here'}

response = requests.get(url, data)
print(response.json())
```

---

## **Conclusion**  
This project provides a **near real-time fraud detection system** that is:  
✅ Scalable with **incremental learning**  
✅ Easy to integrate using **REST APIs**  
✅ Secure with **token-based authentication**  
✅ Accessible to **SMEs and businesses** without expensive in-house solutions  

By implementing this system, **businesses in Zimbabwe** can confidently **adopt digital transactions**, knowing that they have an **intelligent fraud detection system** in place.  

---

### **Contributors**  
- **Nyasha Chizampeni** (Developer)  

For any inquiries, please reach out via email or GitHub.  

