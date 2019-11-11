from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse, Api
from flask_cors import CORS
import json
from datetime import datetime

class ScoreHandler(Resource):
    def post(self):
        print('POST REQUEST RECIEVED')
        data = request.json['data']
        print(data)
        file_name = request.remote_addr.replace('.','_') + '_' + datetime.now().strftime("%y%m%d_%H%M%S")
        print(file_name)
        with open('./'+file_name+'.json', 'a+') as f:
            json.dump(data, f)
        return 'ok'

    def get(self):
        print("GET REQ NOT EXPECTED")
        return "GET REQ NOT EXPECTED"
def main():
    app = Flask(__name__)
    CORS(app, support_credentials=True, resources={r"*": {"origins": "*"}})
    api = Api(app)
    api.add_resource(ScoreHandler, '/submit_scores')
    app.debug = True
    app.run(debug=app, host='x.x.x.x', port=2020, use_reloader=False)

if __name__ == "__main__":
    main()
