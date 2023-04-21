from flask import Flask, render_template, request, redirect
import pymongo
from bson import ObjectId
from datetime import datetime
import requests

app = Flask(__name__)



mydb = pymongo.MongoClient("mongodb://host.docker.internal:27017")
db1=mydb["Ecommerce"]
db=db1["Product_database"]
print("connection Successfull")
db2=db1["User_database"]
print("connection Successfull")



@app.route('/')
def authenticate():
    return render_template('create-post.html')

@app.route('/create-post', methods=["GET", "POST"])
def createPost():
    if(request.method=="GET"):
        return render_template("create-post.html", homeIsActive=False, createPostIsActive=True)

    elif(request.method == "POST"):
        print("in posttt")
        password = request.form['password']
        user = request.form['username']
        
        

        # save the record to the database
        x=db2.find_one({"name": user, "password": password})
        print(x["name"])
        return redirect("/products?form="+str(x["_id"]))
        


@app.route('/products')
def products():
    userId = request.args.get('form')
    print(userId)
    res= requests.get("http://products:5001/products")
    product_id=res.text.split(" ")
    print("back from 5001")
    print(product_id)
    products=[]
    print(product_id)
    for i in product_id:
         products.append(db.find_one({"_id":ObjectId(i)}))
    
    print(products)
    

    # products = list(db.find({}))
    return render_template("home.html", homeIsActive=True, createPostIsActive=False, posts=products,user=userId)


@app.route("/shopping_cart")
def addtocard():
    postId = request.args.get('form')
    print(postId)
    res=requests.get("http://shopping_cart:8000/shoppingcart?form="+str(postId))
    res=res.text.split(" ")
    products=[]
    print(res)
    for i in res:
         products.append(db.find_one({"_id":ObjectId(i)}))
    return render_template("edit-post.html", homeIsActive=True, createPostIsActive=False,posts=products)




@app.route('/addtocart')
def Shopping():
    postId = request.args.get('form')
    postId=postId.split(" ")

    products=db2.find_one_and_update({"_id":ObjectId(postId[1])},{'$push':{'products': postId[0]}})
    return redirect("/products?form="+str(postId[1]))





if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
