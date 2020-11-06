from database import cursor, connection
from flask import Blueprint, request, jsonify
authors = Blueprint("authors", __name__, url_prefix="/authors")


@authors.route("/", methods=["GET"])
def authors_index():
    return "authors"