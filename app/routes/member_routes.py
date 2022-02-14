from flask import Blueprint, request, jsonify, make_response
from app.models.member import Member
from app.models.sheet import Sheet
from app import db

member_bp = Blueprint("member_bp", __name__, url_prefix="/members")
root_bp = Blueprint("root_bp", __name__)

@root_bp.route("/", methods=["GET"])
def root():
    return {"name": "Tally Sheet API"}

@member_bp.route("/", methods=["POST"])
def create_member():
    request_body = request.get_json()
    if "username" not in request_body:
        return {"message": "username must be in request body"}, 400
    new_member = Member(username=request_body["username"])

    db.session.add(new_member)
    db.session.commit()
    return new_member.to_dict()

@member_bp.route("/", methods=["GET"])
def read_all_members():
    members = Member.query.all()
    members_list = Member.create_list_of_members(members)

    return jsonify(members_list)

@member_bp.route("/<member_id>/sheets", methods=["POST"])
def create_sheet(member_id):

    member = Member.query.get(member_id)
    if member is None:
        return {"message": f"no member {member_id}"}, 404

    request_body = request.get_json()
    if "sheet_name" not in request_body:
        return {"message": "sheet_name must be in request body"}, 400

    new_sheet = Sheet(
        sheet_name=request_body["sheet_name"],
        member_id=member_id
        )

    db.session.add(new_sheet)
    db.session.commit()
    return new_sheet.to_dict()

@member_bp.route("/<member_id>/sheets", methods=["GET"])
def read_all_sheets(member_id):

    member = Member.query.get(member_id)
    if member is None:
        return {"message": f"no member with {member_id}"}, 404

    return jsonify(member.to_dict()["sheets"])