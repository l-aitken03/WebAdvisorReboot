from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
# from os import environ
from model.user import User

app = Flask(__name__)
# Configure the database (using SQLite here, modify the URI for PostgreSQL, MySQL, etc.)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../webadvisor.sqllite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create the database tables within the application context
def create_tables():
    with app.app_context():
        db.create_all()

# --- CRUD Operations ---
# Create a user (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(user_username=data.get('username', None),
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
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return make_response(jsonify([user.json() for user in users]), 200)

# Read a single user by ID (GET)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return make_response(jsonify({'user': user.json()}), 200)

# Update a user by ID (PUT/PATCH)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.user_username = data.get('username', user.user_username)
    user.user_first_name = data.get('first_name', user.user_first_name)
    user.user_last_name = data.get('last_name', user.user_last_name)
    user.user_email = data.get('email', user.user_email)
    user.is_prof = data.get('prof', user.is_prof)
    user.is_student = data.get('student', user.is_student)
    db.session.commit()
    return make_response(jsonify({'message': 'user updated', 'user': user.json()}), 200)

# Delete a user by ID (DELETE)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return make_response(jsonify({'message': 'user deleted'}), 200)

if __name__ == '__main__':
    create_tables() # Ensure tables are created before running the app
    app.run(debug=True)
