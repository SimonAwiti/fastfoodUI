from flask import Flask, request
from flask import jsonify
import json
import requests
import ast


app = Flask(__name__)



orders = {}

@app.route('/api/v1/orders')
def get_all_orders():
    return jsonify({'orders':orders})

@app.route('/api/v1/orders', methods=['POST'])
def post_order():
   
   data = request.data
   data=data.decode("utf-8")
   data=ast.literal_eval(data)
   new_index = len(orders) 
   orders[str(new_index)] = [data['date'], data['description'], data['price'], data['status'], data['address'], data['deliveryTime']]
   return jsonify({'data': data}), 201

@app.route('/api/v1/orders/<string:id>')
def get_one_order(id):
    return jsonify({'order':orders[id]}) 
       
@app.route('/api/v1/orders/<string:id>', methods=['PUT'])
def  update_orders(id):
    import pdb;pdb.set_trace()
    data = request.data
    data=data.decode("utf-8")
    data=ast.literal_eval(data)
    orders[id] = [data['date'], data['description'], data['price'], data['status'], data['address'], data['deliveryTime']]
    return jsonify({'data': data}), 202


if __name__ == '__main__':
    app.run()
