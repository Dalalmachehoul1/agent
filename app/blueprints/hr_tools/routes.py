from flask import Blueprint, jsonify

hr_tools_bp = Blueprint("hr_tools", __name__)

@hr_tools_bp.route("/tool1", methods=["GET"])
def tool1():
    return jsonify({"message": "Exemple outil RH 1"})

