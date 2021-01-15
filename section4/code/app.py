from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = "enrique"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []


class ItemList(Resource):
    def get(self):
        return items


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field is required and must be a float"
    )  # as we didn't defined any other arguments, they will get erased from the pyaload

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda item: item["name"] == name, items), None)
        result = item if item else {"error": f"Item with name {name} not founded"}
        return result, 200 if item else 404

    def post(self, name):
        if next(filter(lambda item: item["name"] == name, items), None):  # is not None
            return {"error": f"An Item with name {name} already exists"}, 400

        # data = request.get_json()  # force=True (doesn't check for Header type)
        data = Item.parser.parse_args()

        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda item: item["name"] != name, items))
        return {"message": f"Item {name} deleted"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda item: item["name"] == name, items), None)
        if item is None:
            item = {"name": name, "price": data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item


api.add_resource(Item, "/item/<string:name>")  # http://localhost:5000/item/chair
api.add_resource(ItemList, "/items")  # http://localhost:5000/items
app.run(port=5000, debug=True)
