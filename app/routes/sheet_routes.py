from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.item import Item
from app.models.sheet import Sheet

sheet_bp = Blueprint("sheet_bp", __name__, url_prefix="/sheets")

@sheet_bp.route("/<sheet_id>", methods=["DELETE"])
def delete_sheet(sheet_id):
    sheet = Sheet.query.get(sheet_id)

    db.session.delete(sheet)
    db.session.commit()

    return {"message": f"sheet {sheet_id} successfully deleted"}

@sheet_bp.route("/<sheet_id>/items", methods=["POST"])
def create_item(sheet_id):
    sheet = Sheet.query.get(sheet_id)
    if sheet is None:
        return {"message": f"no sheet {sheet_id}"}, 404

    request_body = request.get_json()
    if "item_name" not in request_body:
        return {"message": "item_name must be in request body"}, 400

    new_item = Item(
        item_name=request_body["item_name"],
        sheet_id=sheet_id,
        amount=0
        )

    db.session.add(new_item)
    db.session.commit()
    return new_item.to_dict()
    

