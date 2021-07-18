from flask_restful import Resource
from flask import request, jsonify, Blueprint, current_app, jsonify
import pandas as pd

predictor_api = Blueprint('predictor_api', __name__)

class Predictor(Resource):

    def predict(self, model, features, payload):
        data = pd.json_normalize(payload).fillna(0)[features]
        prediction = model.predict(data)
        predicted_consumption = {
            'prediction': list(prediction)
        }
        return jsonify(predicted_consumption), 200

model_predictor = Predictor()

@predictor_api.route("/predict", methods=['POST'], )
def predict():
    payload = request.get_json(force=True)
    model = current_app.config['model']
    features = current_app.config['features']
    return model_predictor.predict(model, features, payload)