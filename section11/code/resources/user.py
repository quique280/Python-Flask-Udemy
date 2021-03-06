from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)
from blacklist import BLACKLIST

from werkzeug.security import safe_str_cmp


_user_parser = reqparse.RequestParser()
_user_parser.add_argument("username", type=str, required=True, help="An username is required and must be a string")
_user_parser.add_argument("password", type=str, required=True, help="A password is required and must be a string")


class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"error": "A user with that username already exists."}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User create successfully."}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"error": f"User with id={user_id} not found"}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"error": f"User with id={user_id} not found"}, 404

        user.delete_from_db()
        return {"message": f"USer with id={user_id} deleted"}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        # get data from parser
        data = _user_parser.parse_args()

        # find user in database
        user = UserModel.find_by_username(data["username"])
        # check password
        # create access token
        # create refresh token
        if user and safe_str_cmp(user.password, data["password"]):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        return {"error": "Invalid credentials"}, 401
        # return them


class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()["jti"]  # jti is JWT ID, a unique identifier for a JWT
        BLACKLIST.add(jti)
        return {"message": "Successfully logged out"}


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200
