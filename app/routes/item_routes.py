from flask import Blueprint, request, jsonify, make_response
from app.models.user import User
from app import db

item_bp = Blueprint("item_bp", __name__, url_prefix="/items")


