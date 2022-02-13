from flask import Blueprint, request, jsonify, make_response
from app.models.user import User
from app import db

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")
root_bp = Blueprint("root_bp", __name__)

@root_bp.route("/", methods=["GET"])
def root():
    return {
        "name": "Tally Sheet API",
    }
