from flask import Flask
from flask_restful import Api
from resources import CategoryResource, GoodsResource, TotalSumResource
import models as m
import db_generator

app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResource, '/categories', '/categories/<c_id>')
api.add_resource(GoodsResource, '/goods', '/goods/<g_id>')
api.add_resource(TotalSumResource, '/sum')

if __name__ == '__main__':
    app.run(debug=True)