from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

@app.get("/about")
def about():
    me = {"name":"Nicholas Johnson"}
    return json.dumps(me)

#please create an API to footer that contains the name of the page
@app.get("/footer")#I know that this is a section not a page
def footer():
    pageName = {"pageName": "Organika"}
    return json.dumps(pageName)

products = []
@app.get("/api/products")
def read_products():
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    products.append(item)
    print(item)
    return json.dumps(item)

@app.put("/api/products/<int:index>")
def update_products(index):
    update_item = request.get_json()
    if 0<= index < len(products):
        products[index]=update_item
        return json.dumps(update_item)
    else:
        return "That index does not exist"
app.run(debug=True)

