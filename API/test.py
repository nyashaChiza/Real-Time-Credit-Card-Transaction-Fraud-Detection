from river import compose
from river import linear_model
from river import preprocessing
import dill
import requests

model = compose.Pipeline(
    preprocessing.StandardScaler(),
    linear_model.LinearRegression()
)
with open('model.pkl', 'wb') as file:
    dill.dump(model, file)