from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel


class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)

        # items = []
        # for row in result:
        #     items.append({"name": row[1], "price": row[2]})

        # connection.close()
        # return {"items": items}

        # return {"items": [item.json() for item in ItemModel.query.all()]}
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field is required and must be a float"
    )  # as we didn't defined any other arguments, they will get erased from the pyaload
    parser.add_argument(
        "store_id", type=int, required=True, help="This field is required and must be an integer"
    )  # as we didn't defined any other arguments, they will get erased from the pyaload

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"error": "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):  # is not None
            return {"error": f"An Item with name {name} already exists"}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {"error": "An error ocurred inserting the item"}, 500
        else:
            return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()

        # query = "DELETE FROM items WHERE name = ?"
        # cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()
        return {"message": f"Item {name} deleted"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updatedItem = ItemModel(name, data["price"])
        if item is None:
            # try:
            # updatedItem.insert()
            item = ItemModel(name, **data)
            # except:
            #     return {"error": "An error ocurred inserting the item"}, 500
        else:
            item.price = data["price"]
            # try:
            #     updatedItem.update()
            # except:
            #     return {"error": "An error ocurred updating the item"}, 500
        try:
            item.save_to_db()
        except:
            return {"error": "Error upserting the item"}
        return item.json()