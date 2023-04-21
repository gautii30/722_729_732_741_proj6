from flask import Flask, render_template, request, redirect
import pymongo
from bson.objectid import ObjectId
from datetime import datetime
import requests

app = Flask(__name__)
mydb = pymongo.MongoClient("mongodb://host.docker.internal:27017")
db1=mydb["Ecommerce"]
db=db1["User_database"]

postid=0

@app.route('/shoppingcart')
def shoppingcart():
    print("in here")
    UserId = request.args.get('form')
    print(UserId)
    products=db.find_one({"_id":ObjectId(UserId)})
    p=products["products"]
    listToStr = ' '.join([str(elem) for elem in p])
    print(listToStr)
    return listToStr
    
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)

