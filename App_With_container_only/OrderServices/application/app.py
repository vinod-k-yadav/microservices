#product services 
from flask import Flask, request , jsonify
from flask_restful import Resource, Api
import requests
app = Flask(__name__)

api = Api(app)

#Resource Store
class Order(Resource):

    def get(self, id):
        return jsonify({'order_id': id ,
                        'details':{"Item Name": "T-Shirt",
                                    "Price": 12345.56}
                                    
                                }
                        )
        
    def post(self, name):
        request_param = request.get_json()
        print(request_param)
        return jsonify(request_param)

class OrderCheckout(Resource):
    def post(self):
        response = requests.get(url='http://cuser-service_5001:5001/api/user/vinod1' )
        if response.status_code == 401:
            return False
        user = response.json()
        return user

#api.add_resource(Item, '/items')
api.add_resource(Order, '/api/order/<string:id>')
api.add_resource(OrderCheckout, '/api/order/checkout')


if __name__=="__main__":

    app.run(host='0.0.0.0', port=5005)

