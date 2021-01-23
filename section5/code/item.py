from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)

        items = []
        for row in result:
            items.append({"name": row[0], "price": row[1]})

        connection.close()
        return {"items": items}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field is required and must be a float"
    )  # as we didn't defined any other arguments, they will get erased from the pyaload

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {"item": {"name": row[0], "price": row[1]}}

    @jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)
        if item:
            return item
        return {"error": "Item not found"}, 404

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (item["name"], item["price"]))

        connection.commit()
        connection.close()

    def post(self, name):
        if Item.find_by_name(name):  # is not None
            return {"error": f"An Item with name {name} already exists"}, 400

        data = Item.parser.parse_args()

        item = {"name": name, "price": data["price"]}
        try:
            Item.insert(item)
        except:
            return {"error": "An error ocurred inserting the item"}, 500
        else:
            return item, 201

    def delete(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {"message": f"Item {name} deleted"}

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "UPDATE items SET price = ? WHERE name = ?"
        cursor.execute(query, (item["price"], item["name"]))

        connection.commit()
        connection.close()

    def put(self, name):
        data = Item.parser.parse_args()

        item = Item.find_by_name(name)
        updatedItem = {"name": name, "price": data["price"]}
        if item is None:
            try:
                Item.insert(updatedItem)
            except:
                return {"error": "An error ocurred inserting the item"}, 500
        else:
            try:
                Item.update(updatedItem)
            except:
                return {"error": "An error ocurred updating the item"}, 500
        return updatedItem

    # @jwt_required()
    # def get(self, name):
    #     item = next(filter(lambda item: item["name"] == name, items), None)
    #     result = item if item else {"error": f"Item with name {name} not founded"}
    #     return result, 200 if item else 404

    # def post(self, name):
    #     if next(filter(lambda item: item["name"] == name, items), None):  # is not None
    #         return {"error": f"An Item with name {name} already exists"}, 400

    #     # data = request.get_json()  # force=True (doesn't check for Header type)
    #     data = Item.parser.parse_args()

    #     item = {"name": name, "price": data["price"]}
    #     items.append(item)
    #     return item, 201

    # def delete(self, name):
    #     global items
    #     items = list(filter(lambda item: item["name"] != name, items))
    #     return {"message": f"Item {name} deleted"}

    # def put(self, name):
    #     data = Item.parser.parse_args()

    #     item = next(filter(lambda item: item["name"] == name, items), None)
    #     if item is None:
    #         item = {"name": name, "price": data["price"]}
    #         items.append(item)
    #     else:
    #         item.update(data)
    #     return item