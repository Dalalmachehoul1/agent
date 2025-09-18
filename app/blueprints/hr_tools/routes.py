from flask import Blueprint, jsonify

hr_tools_bp = Blueprint("hr_tools", __name__)

@hr_tools_bp.route("/tool1", methods=["GET"])
def tool1():
    return jsonify({"message": "Outil RH 1"})

@hr_tools_bp.route("/tool2", methods=["GET"])
def tool2():
    return jsonify({"message": "Outil RH 2"})

# Répéter pour tool3 à tool8
