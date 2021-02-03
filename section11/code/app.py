from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
import os

from blacklist import BLACKLIST
from resources.user import UserRegister, User, UserLogin, TokenRefresh, UserLogout
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]
app.secret_key = "enrique"  # app.config['JWT_SECRET_KEY']
api = Api(app)

# Creating tables with sqlalchemy
@app.before_first_request
def create_tables():
    db.create_all()


# app.config['JWT_AUTH_URL_RULE'] = '/login' # This works if we want to change the default auth endpoint
# app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=1800) # token expiration time
# app.config["JWT_AUTH_USERNAME_KEY"] = "email"  # config JWT auth key to be email instead of default username
jwt = JWTManager(app)  # not creating /auth endpoint


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:  # Instead of hard-coding, you should read from a config file or a database
        return {"is_admin": True}
    return {"is_admin": False}


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["identity"] in BLACKLIST or decrypted_token["jti"] in BLACKLIST


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({"message": "The token has expired.", "error": "token_expired"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({"message": "Signature verification failed.", "error": "invalid_token"}), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"description": "Request does not contain an access token.", "error": "authorization_required"}), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({"description": "The token is not fresh.", "error": "fresh_token_required"}), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({"description": "The token has been revoked.", "error": "token_revoked"}), 401


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
api.add_resource(Store, "/store/<string:name>")  # http://localhost:5000/store/walmart
api.add_resource(StoreList, "/stores")  # http://localhost:5000/stores
api.add_resource(UserRegister, "/register")  # http://localhost:5000/register
api.add_resource(User, "/user/<int:user_id>")  # http://localhost:5000/user
api.add_resource(UserLogin, "/login")  # http://localhost:5000/login
api.add_resource(UserLogout, "/logout")  # http://localhost:5000/logout
api.add_resource(TokenRefresh, "/refresh")  # http://localhost:5000/refresh
if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
