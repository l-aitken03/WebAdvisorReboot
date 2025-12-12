from flask import Blueprint, request, jsonify, make_response, render_template
from model.base import db
from model.user import User

user_bp = Blueprint('user', __name__, url_prefix='/user')

# --- CRUD Operations ---
# Create a user (POST)
@user_bp.route('/create', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
                    user_id=data.get('user_id', None),
                    user_username=data.get('username', None),
                    user_first_name=data.get('first_name', None),
                    user_last_name=data.get('last_name', None),
                    user_email=data.get('email', None),
                    is_prof=data.get('prof', False),
                    is_student=data.get('student', True),
                    )
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({'message': 'user created', 'user': new_user.json()}), 201)

# Read all users (GET)
@user_bp.route('/all', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('user/list_all.html', users=[user for user in users])
    #return make_response(jsonify([user.json() for user in users]), 200)

# Read a single user by ID (GET)
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user/profile.html', user=user)
    #return make_response(jsonify({'user': user.json()}), 200)

# Update a user by ID (PUT/PATCH)
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    # see create user method for why USER_ID exists here
    user.user_id = data.get('id', user.user_id)
    user.user_username = data.get('username', user.user_username)
    user.user_first_name = data.get('first_name', user.user_first_name)
    user.user_last_name = data.get('last_name', user.user_last_name)
    user.user_email = data.get('email', user.user_email)
    user.is_prof = data.get('is_prof', user.is_prof)
    user.is_student = data.get('is_student', user.is_student)
    db.session.commit()
    return make_response(jsonify({'message': 'user updated', 'user': user.json()}), 200)

# Delete a user by ID (DELETE)
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return make_response(jsonify({'message': 'user deleted'}), 200)