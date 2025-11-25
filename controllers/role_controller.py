from flask import Flask, request, jsonify, make_response
from model.base import db
from model.role import Role

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../SQLite_DB.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Redwo0d$@127.0.0.1:3306/webadvisor_reboot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

# --- C[R]UD Operations [READ ONLY] ---

# Read all roles (GET)
@app.route('/roles', methods=['GET'])
def get_roles():
    roles = Role.query.all()
    return make_response(jsonify([role.json() for role in roles]), 200)

# Read a single role by ID (GET)
@app.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    role = Role.query.get_or_404(role_id)
    return make_response(jsonify({'role': role.json()}), 200)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)