from flask import Flask
from flask_restful import Api
from resources import UserResource


app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/users', '/users/<user_id>')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
