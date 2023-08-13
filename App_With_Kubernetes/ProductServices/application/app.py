#product services 
from flask import Flask, request , jsonify
from flask_restful import Resource, Api
app = Flask(__name__)

api = Api(app)

#Resource Store
class Product(Resource):

    def get(self, name):
        return jsonify({'name': name ,
                        'Price':123})
        
    def post(self, name):
        request_param = request.get_json()
        print(request_param)
        # Add product here to REdis db.
        return jsonify(request_param)

#api.add_resource(Item, '/items')
api.add_resource(Product, '/api/product/<string:name>')


if __name__=="__main__":

    app.run(host='0.0.0.0', port=6200)

