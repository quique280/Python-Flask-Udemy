from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

# from datetime import timedelta

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList


app = Flask(__name__)
app.secret_key = "enrique"
api = Api(app)

# app.config['JWT_AUTH_URL_RULE'] = '/login' # This works if we want to change the default auth endpoint
# app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=1800) # token expiration time
# app.config["JWT_AUTH_USERNAME_KEY"] = "email"  # config JWT auth key to be email instead of default username
jwt = JWT(app, authenticate, identity)  # /auth


# Authentication response handler
# @jwt.auth_request_handler
# def customized_response_handler(access_token, identity):
#     return jsonify({"access_token": access_token.decode("utf-8"), "user_id": identity.id})


# Error handler
# @jwt.jwt_error_handler
# def customized_error_handler(error):
#     return jsonify({"message": error.description, "code": error.status_code}), error.status_code


api.add_resource(Item, "/item/<string:name>")  # http://localhost:5000/item/chair
api.add_resource(ItemList, "/items")  # http://localhost:5000/items
api.add_resource(UserRegister, "/register")  # http://localhost:5000/register
if __name__ == "__main__":
    app.run(port=5000, debug=True)
