from flask import Blueprint, jsonify
from ..models import Activity

activity_bp = Blueprint('activity_bp', __name__)

@activity_bp.route('/activities', methods=['GET'])
def list_activities():
    activities = Activity.query.all()
    return jsonify([{'id': activity.id, 'name': activity.name, 'payoff': activity.price} for activity in activities])
