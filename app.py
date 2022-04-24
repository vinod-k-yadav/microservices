# application/frontend/api/UserClient.py
from flask import Flask, request , jsonify
from flask_restful import Resource, Api
import requests
app = Flask(__name__)

api = Api(app)

class UserClient:
    @staticmethod
    def get_user(name):

        url = 'http://cuser-service_5001:5001/api/user/{0}'.format(name)
        response = requests.request(method="GET", url=url)
        user = response.json()
        return user


class OrderClient:
    @staticmethod
    def get_order(id):
        url = "http://corder-service_5005:5005/api/order/{0}".format(id)
        response = requests.request(method="GET", url=url)
        products = response.json()
        return products


class ProductClient:
    @staticmethod
    def get_product(name):
        url = "http://cproduct-service_5003:5003/api/product/{0}".format(name)

        response = requests.request(method="GET", url=url)
        products = response.json()
        return products


#Resource Store
class FrontendUser(Resource):

    def get(self, name):
        return  UserClient.get_user(name)
        
  

class FrontendProduct(Resource):
    
    def get(self, name):
        return ProductClient.get_product(name)

class FrontendOrder(Resource):

    def get(self, id):
        return  OrderClient.get_order(id)
        




#api.add_resource(Item, '/items')
api.add_resource(FrontendUser, '/api/frontend/user/<string:name>')
api.add_resource(FrontendProduct, '/api/frontend/product/<string:name>')
api.add_resource(FrontendOrder, '/api/frontend/order/<string:id>')



if __name__=="__main__":

    app.run(host='0.0.0.0', port=6000)
