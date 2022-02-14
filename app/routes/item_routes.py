from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.item import Item

item_bp = Blueprint("item_bp", __name__, url_prefix="/items")

@item_bp.route("/<item_id>/increment", methods=["PATCH"])
def add_one(item_id):
    item = Item.query.get(item_id)

    if item is None:
        return {"message": f"No item {item_id}"}
    
    item.amount += 1
    db.session.commit()

    return item.to_dict()

@item_bp.route("/<item_id>/decrement", methods=["PATCH"])
def subtract_one(item_id):
    item = Item.query.get(item_id)

    if item is None:
        return {"message": f"No item {item_id}"}
    
    item.amount -= 1
    db.session.commit()

    return item.to_dict()

@item_bp.route("/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get(item_id)

    if item is None:
        return {"message": f"No item {item_id}"}
    
    db.session.delete(item)
    db.session.commit()

    return f"Item {item_id} deleted"

