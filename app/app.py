from flask import Flask, render_template, request, redirect
import pymongo
from bson.objectid import ObjectId
from datetime import datetime
import requests

app = Flask(__name__)

user = ''           # username as set for the mongodb admin server (the username used in secret.yaml - before base64 conversion)
password = ''       # password as set for the mongodb admin server (the password used in secret.yaml - before base64 conversion)
host = ''    # service name of the mongodb admin server as set in the service for mongodb server
port = ''              # port number of the mongodb admin server as set in the service for mongodb server


mydb = pymongo.MongoClient("mongodb://host.docker.internal:27017")
db1=mydb["Ecommerce"]
db=db1["Product_database"]
# db_user=db1['users']




@app.route('/products')
def home():
    products = list(db.find({}))
    

    listToStr = ' '.join([str(elem["_id"]) for elem in products])
    return listToStr
   




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)
