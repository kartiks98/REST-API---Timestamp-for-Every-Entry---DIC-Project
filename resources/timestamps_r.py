# from flask_restful import Resource, reqparse
from flask_restful import Resource
# from flask_jwt_extended import jwt_required
from models.timestamps_m import NameModel

from datetime import datetime

class Name(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #                     type=float,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    # parser.add_argument('store_id',
    #                     type=int,
    #                     required=True,
    #                     help="Every item needs a store_id."
    #                     )

    # @jwt_required
    def get(self, name):
        item = NameModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        
        t_s = str(datetime.now())

        item = NameModel(name, t_s)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = NameModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': f'Latest Item deleted. (id = {item.id})'}
        return {'message': 'Item not found.'}, 404

    # def put(self, name):
    #     t_s = "timestamp"

    #     item = NameModel.find_by_name(name)

    #     if item:
    #         item.timestamp = t_s
    #     else:
    #         item = NameModel(name, t_s)

    #     item.save_to_db()

    #     return item.json()


class NameList(Resource):
    def get(self):
        return {'NameList': [x.json() for x in NameModel.query.all()]}