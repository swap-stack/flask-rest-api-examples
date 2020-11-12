from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(posted_data, function_name):
    if (function_name == "add"):
        if "x"not in posted_data or "y" not in posted_data:
            return 301
        else:
            return 200


class Add(Resource):
    def post(self):
        #resource add was requested by POST

        posted_data = request.get_json()
        
        status_code = checkPostedData(posted_data, "add")

        if status_code != 200:
            retJson = {
                "Message": "An error occured",
                "Status Code": status_code
            }
            return jsonify(retJson)
                    
        x = posted_data['x']
        y = posted_data['y']
        x, y = int(x), int(y)
        ret = x + y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

    def get(self):
        #resource add was requested by GET
        pass


api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return "Hello World"

if __name__=="__main__":
    app.run(debug=True)
