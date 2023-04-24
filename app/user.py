from flask import Flask, render_template, request, redirect
import pymongo
from bson.objectid import ObjectId
from datetime import datetime
import requests

mydb = pymongo.MongoClient("mongodb://localhost:27017/")
db1=mydb["Ecommerce"]
db=db1["User_database"]

db.insert_one({"name":"rhea" ,"password":"sudheer"})
# app = Flask(__name__)

# @app.route('/')
# def authenticate():
#     return render_template('create-post.html')

# @app.route('/create-post', methods=["GET", "POST"])
# def createPost():
#     if(request.method=="GET"):
#         return render_template("create-post.html", homeIsActive=False, createPostIsActive=True)

#     elif(request.method == "POST"):
#         title = request.form['username']
#         author = request.form['password']
#         createdAt = datetime.now()

#         # save the record to the database
#         db.posts.insert_one({"title": title, "author": author, "createdAt": createdAt})

#         # redirect to home page
#         return redirect("/")

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="4000", debug=True)