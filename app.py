from flask import Flask, jsonify, request
from flask_restful import Resource, reqparse, Api
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Interpreter

from trainbot import train_bot, predict_intent

app = Flask(__name__)
api = Api(app)

class index(Resource):
    def get(self):
        return "<p> Horoscope bot <p>"


class intent(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        text = json_data['text']
        json= predict_intent(text)
        return json


api.add_resource(index, '/')
api.add_resource(intent, '/intent')
  
if __name__=='__main__':
    train_bot()
    app.run(debug=True)