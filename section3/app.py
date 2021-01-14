from flask import Flask, jsonify, request, render_template

# create flask application
app = Flask(__name__)


# Create mock data
stores = [{"name": "My Wonderful Store", "items": [{"name": "My Item", "price": 15.99}]}]

# Hellow world using Flask
# @app.route("/")  # Home page
# def home():
#     return "Hello world!"


# HOME
@app.route("/")  # Home page
def home():
    return render_template("index.html")


# Create endpoints
# POST /store data:{name}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name: str):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"error": f"No store found with name {name}"})


# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})


# POST /store/<string:name>/item {name:,price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            request_data = request.get_json()
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"error": f"No store found with name {name}"})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name: str):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"error": f"No store found with name {name}"})


app.run(port=5000)