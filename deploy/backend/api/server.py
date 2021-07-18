from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import pickle
from predictor import predictor_api

app = Flask(__name__)
CORS(app)
app.register_blueprint(predictor_api, url_prefix='/model')
api = Api(app)

model = None
features = None

def load_model():
    global model, features
    with open('../models/beer_consumption_model.pkl', 'rb') as m:
        model = pickle.load(m)
    with open('../models/beer_consumption_features.pkl', 'rb') as f:
        features = pickle.load(f) 

if __name__ == '__main__':
    load_model() # load the model on flask start
    app.config['model'] = model
    app.config['features'] = features
    app.run(host='0.0.0.0', port=5000)
