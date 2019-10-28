```py
from flask import Flask
from flask_restful import Resource, reqparse, Api
import json, csv

class AI_Server(Resource):

    def post(self):
        parser                                      = reqparse.RequestParser()
        parser.add_argument("data", type=str)
        args                                        = parser.parse_args()
        data                                        = json.loads(args["data"])
        print(data)

        with open('subjective_eval_results.csv', 'ab') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writerow(data)
        return '...saved...'

if __name__ == "__main__":
    fields = [str(x) for x in range(1, 65)]
    with open('subjective_eval_results.csv', 'wb') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(AI_Server, '/submit')
    app.debug = True
    app.run(debug=app, host='xx.xxx.xxx.xx', port=2020, use_reloader=False)
```
