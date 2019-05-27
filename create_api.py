from flask import Flask 
from flask_restful import Api, Resource, reqparse

# we are telling app to run in this speicific place
app = Flask(__name__)
api = Api(app)

# list of users. In reality data is stored in a database
users = [
    {
        "name": "Ulan",
        "age": 25,
        "occupation": "software engineer"
    }, 
    {
        "name": "Derek",
        "age": 40,
        "occupation": "Doctor"
    }, 
    {
        "name": "John",
        "age": 18,
        "occupation": "college student"
    }
]

class User(Resource):

    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = response.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = response.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"],
                user["occupation"] = args["occupation"]
                return user, 200
                
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201 # created code

    def delete(self, name):
        # TODO change this later for more understandable code
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted ".format(name), 200
 
# <string:name> indicates that it is a variable part in the route which accepts any name 
api.add_resource(User, "/user/<string:name>")
app.run(debug=True)

# TODO 
# add config
# add JWT
# add requirements txt file



