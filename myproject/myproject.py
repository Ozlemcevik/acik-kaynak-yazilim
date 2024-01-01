from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd
import requests

app = Flask(__name__)
api = Api(app)



class GetAllWord(Resource):
    def get(self):

        url = 'https://api.datamuse.com/words?ml=duck&sp=b*&max=10'

        resp = requests.get(url)
        data = resp.json()


        return {'data': data}, 200

api.add_resource(GetAllWord, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
    app.run()
