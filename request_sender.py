    # -*- coding: utf-8 -*-
    #код для того чтобы посылать запросы
import json
from flask import jsonify, Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True

f = open('smartphones.json')
data = json.load(f)
@app.route('/smartphones', methods = ['GET'])
def getSmarpthones():
    price = request.args['price']
    list = []
    for i in data:
        for j in i:
            if int(j["price"]) == int(price):
                list.append(j)
    return (jsonify(list))
app.run(debug=True, port=5000)
