from flask import Blueprint, jsonify
from ..models import Guest

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/guests', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    return jsonify([{'id': guest.id, 'name': guest.name, 'balance': guest.balance} for guest in guests])
