import sqlite3
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
from models.item import ItemModel
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt


items =[]

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('complaint_details',
        type=str,
        required = True,
        help= "This field cannot be left blank."
    )
    
    @jwt_required
    def get(self, id):
        
        item= ItemModel.find_by_id(id)
        if item:
            return item.json()
        return {"message":"Item not found"}, 404

    @jwt_required
    def post(self,id):
        if ItemModel.find_by_id(id):
            return({"message":"An item with name {} already exists.".format(id)})
        data = Item.parser.parse_args()
        item = ItemModel(data["complaint_details"])
        try:
            item.insert_update()
        except:
            return({"message":"An error occurred in inserting the item."}), 500 #internal server error
        return item.json(), 201

    @jwt_required
    def delete(self, id):
       
        item = ItemModel.find_by_id(id)
        if item:
            item.delete()
            return {"message":"Item deleted"}
        else:
            return({"message":"Item not found."})

    @jwt_required
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_id(id)
        if item is None:
            item = ItemModel(data["complaint_details"])
        else:
            item.price = data["complaint_details"]
        item.insert_update()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {"items":list(map(lambda x: x.json(), ItemModel.query.all()))}