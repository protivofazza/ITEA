from flask_restful import Resource
from flask import request, jsonify
from models import Category, Goods
from schemas import CategorySchema, GoodsSchema, ValidationError


class CategoryResource(Resource):

    def get(self, c_id=None):
        if c_id:
            category = Category.objects.get(id=c_id)
            category = CategorySchema().dump(category)
            return category
        else:
            categories = Category.objects
            return CategorySchema().dump(categories, many=True)

    def post(self):
        try:
            category = CategorySchema().load(request.get_json())
        except ValidationError as err:
            return str(err)
        return CategorySchema().dump(Category.objects.create(**category).save())

    def put(self):
        pass

    def delete(self):
        pass


class GoodsResource(Resource):

    def get(self, g_id=None):
        if g_id:
            goods = Goods.objects.get(id=g_id)
            goods.seen_by += 1
            goods.save()
            return GoodsSchema().dump(goods)
        else:
            return GoodsSchema().dump(Goods.objects, many=True)

    def post(self):
        try:
            goods = GoodsSchema().load(request.get_json())
        except ValidationError as err:
            return str(err)
        return GoodsSchema().dump(Goods.objects.create(**goods).save())

    def put(self):
        pass

    def delete(self):
        pass


class TotalSumResource(Resource):

    def get(self):
        goods = Goods.objects
        s = 0
        for good in goods:
            s += good.price
        return {"sum": s}
