from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="An username is required and must be a string")
    parser.add_argument("password", type=str, required=True, help="A password is required and must be a string")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"error": "A user with that username already exists."}, 400

        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()

        # query = "INSERT INTO users(username, password) VALUES (?,?)"
        # cursor.execute(query, (data["username"], data["password"]))

        # connection.commit()

        # connection.close()
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User create successfully."}, 201
