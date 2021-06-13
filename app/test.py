#training session

from river import compose
from river import preprocessing
from river import linear_model
from river import metrics
from river import tree
from river import neighbors
from river import ensemble
from river import stream
import river
import pandas as pd
import requests
import time

model1 = compose.Pipeline(
    compose.Select('account_type','location','bank','connection_type','broswer','avs', 'gender','entry_type') | river.preprocessing.OneHotEncoder(),
    preprocessing.StandardScaler(),
    ensemble.AdaptiveRandomForestClassifier(
     n_models=4,
     seed=42
    )
)
link = 'http://127.0.0.1:5000/classification/'
li= 'hit400Dataset.csv'
df = pd.read_csv(li)
df = df[28000:]
X= df.drop('label', axis=1)
y = df['label']
for xi, yi in stream.iter_pandas(X, y):
    xi['api_key']  = '404209da0f1b6200a24b19782048fd090b08b3fa4e13a4907778fcbec147672913f133d8d6cb910fa77315c416ccc0a3'
    xi['answer'] = yi
    try:
        resp = requests.get(link, xi)
    except:
        time.sleep(5)
        resp = requests.get(link, xi)

    print(resp.json(),yi)
    time.sleep(5)
