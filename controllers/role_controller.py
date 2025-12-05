from flask import Blueprint, jsonify, make_response
from model.role import Role

role_bp = Blueprint('role', __name__, url_prefix='/role')

# --- C[R]UD Operations [READ ONLY] ---

# Read all roles (GET)
@role_bp.route('/all', methods=['GET'])
def get_roles():
    roles = Role.query.all()
    return make_response(jsonify([role.json() for role in roles]), 200)

# Read a single role by ID (GET)
@role_bp.route('/<int:role_id>', methods=['GET'])
def get_role(role_id):
    role = Role.query.get_or_404(role_id)
    return make_response(jsonify({'role': role.json()}), 200)