from flask import Flask, request , jsonify
from flask_restful import Resource, Api
import redis
import os
REDIS_URL = os.environ.get("REDIS_URL")
print("REDIS url:",  REDIS_URL)
r = redis.Redis.from_url(url=REDIS_URL)

app = Flask(__name__)

api = Api(app)
ITEMS= []
#Resource Store
class User(Resource):

    def get(self, name):
        rst = r.get(name)
        return jsonify({'name': name , "result" : str(rst)})
        
    def post(self, name):
        
        r.set(  name , "added" )
        request_param = request.get_json()
        print(request_param)
        # Add user to data base
        return jsonify(request_param)

#api.add_resource(Item, '/items')
api.add_resource(User, '/api/user/<string:name>')

"""

# GET : get all store
@app.route('/store', methods= ['GET'])
def get_stores():
    

@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    return f"get_store {name}"

@app.route('/store', methods=['POST'])
def create_store():
    request_param = request.get_json()
    print(request_param)
    return jsonify(request_param)
    

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    return f"create_item_in_store {name}"

@app.route('/store/<string:name>/item', methods=['GET'])
def get_items(name):
    return "get_items"


"""
if __name__=="__main__":

    app.run(host='0.0.0.0', port=6300)

