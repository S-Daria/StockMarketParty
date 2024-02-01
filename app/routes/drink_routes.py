from flask import Blueprint, jsonify
from ..models import Drink

drink_bp = Blueprint('drink_bp', __name__)

@drink_bp.route('/drinks', methods=['GET'])
def list_drinks():
    drinks = Drink.query.all()
    return jsonify([{'id': drink.id, 'name': drink.name, 'price': drink.price} for drink in drinks])
