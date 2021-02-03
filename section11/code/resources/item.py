from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_claims, get_jwt_identity, fresh_jwt_required

from models.item import ItemModel


class ItemList(Resource):
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        items = [x.json() for x in ItemModel.find_all()]
        if user_id:
            return {"items": items}, 200

        return {"message": "More data available if you log in", "items": [item["name"] for item in items]}, 200


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True, help="This field is required and must be a float")
    parser.add_argument("store_id", type=int, required=True, help="This field is required and must be an integer")

    @jwt_required
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"error": "Item not found"}, 404

    @fresh_jwt_required
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"error": f"An Item with name {name} already exists"}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {"error": "An error ocurred inserting the item"}, 500
        else:
            return item.json(), 201

    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims["is_admin"]:
            return {"error": "Admin privilege required"}
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": f"Item {name} deleted"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data["price"]
        try:
            item.save_to_db()
        except:
            return {"error": "Error upserting the item"}
        return item.json()