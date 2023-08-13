# application/frontend/api/UserClient.py
from flask import Flask, request , jsonify
from flask_restful import Resource, Api
import os
import requests
app = Flask(__name__)

api = Api(app)

#ip
PRODUCT_URL = os.environ.get('PRODUCT_URL')
USER_URL = os.environ.get('USER_URL')
ORDER_URL = os.environ.get('ORDER_URL')

print("PRODUCT address :" , PRODUCT_URL )
print("USER address :" , USER_URL )
print("ORDER address :" , ORDER_URL )


class UserClient:
    @staticmethod
    def get_user(name):

        #url = 'http://cuser-service_5001:5001/api/user/{0}'.format(name) URL of User service.
        #url = 'http://localhost:6300/api/user/{0}'.format(name)
        url = "".join([USER_URL, '/api/user/{0}'.format(name)])
        print ("********************************************")
        print(url)
        response = requests.request(method="GET", url=url)
        user = response.json()
        return user


class OrderClient:
    @staticmethod
    def get_order(id):
        #url = "http://localhost:6100/api/order/{0}".format(id) #URL to order service.
        url = "".join([ORDER_URL, '/api/order/{0}'.format(id)])
        print ("********************************************")
        print(url)
    
        response = requests.request(method="GET", url=url)
        products = response.json()
        return products


class ProductClient:
    @staticmethod
    def get_product(name):
        #url = "http://localhost::6200/api/product/{0}".format(name) # URL of product service.
        url = "".join([PRODUCT_URL, '/api/product/{0}'.format(name)])
        print ("********************************************")
        print(url)

        response = requests.request(method="GET", url=url)
        products = response.json()
        return products


#Resource Store
class FrontendUser(Resource):

    def get(self, name):
        print("*****Going to call backend: userService")
        return  UserClient.get_user(name)
        
  

class FrontendProduct(Resource):
    
    def get(self, name):
        print("*****Going to call backend: ProductService")
        return  ProductClient.get_product(name)
    
class FrontendOrder(Resource):

    def get(self, id):
        print("*****Going to call backend: OrderService")
        return OrderClient.get_order(id)
        
        




#api.add_resource(Item, '/items')
api.add_resource(FrontendUser, '/api/frontend/user/<string:name>')
api.add_resource(FrontendProduct, '/api/frontend/product/<string:name>')
api.add_resource(FrontendOrder, '/api/frontend/order/<string:id>')



if __name__=="__main__":

    app.run(host='0.0.0.0', port=6000)
