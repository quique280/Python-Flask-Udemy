from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"error": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"error": f"A store with name {name} already exists"}, 400
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {"error": "An error ocurred inserting the store"}, 500
            else:
                return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return store.json()
        else:
            return {"error": "That stored doesn't exists"}, 404


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.find_all()]}
