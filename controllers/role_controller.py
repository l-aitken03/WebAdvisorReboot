from flask import Blueprint, jsonify, make_response
from model.base import db
from model.role import Role
from model.user import User

role_bp = Blueprint('role', __name__,
                    template_folder='templates',
                    static_folder='static', url_prefix='/role')

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

# Add a user by username to a role by id
@role_bp.route('/<int:role_id>/add/<username>', methods=['GET'])
def add_user_to_role(username, role_id):
    user = User.query.filter_by(user_username=username).first()
    role = Role.query.filter_by(role_id=role_id).first()
    user.roles.append(role)
    db.session.add(user)
    db.session.commit()

    return make_response(jsonify({'r': role_id, 'un': username}))
