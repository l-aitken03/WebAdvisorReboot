from flask import Blueprint, jsonify, make_response#, request
from model.base import db
from model.permission import Permission

perm_bp = Blueprint('permission', __name__, url_prefix='/perm')

# --- C[R]UD Operations [READ ONLY] ---

# Read all permissions (GET)
@perm_bp.route('/all', methods=['GET'])
def get_permissions():
    permissions = Permission.query.all()
    return make_response(jsonify([permission.json() for permission in permissions]), 200)

# Read a single permission by ID (GET)
@perm_bp.route('/<int:perm_id>', methods=['GET'])
def get_permission(perm_id):
    permission = Permission.query.get_or_404(perm_id)
    return make_response(jsonify({'permission': permission.json()}), 200)