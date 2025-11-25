from flask import Flask, jsonify, make_response#, request
from model.base import db
from model.permission import Permission

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
@app.route('/permissions', methods=['GET'])
def get_permissions():
    permissions = Permission.query.all()
    return make_response(jsonify([permission.json() for permission in permissions]), 200)

# Read a single role by ID (GET)
@app.route('/permissions/<int:perm_id>', methods=['GET'])
def get_permission(perm_id):
    permission = Permission.query.get_or_404(perm_id)
    return make_response(jsonify({'permission': permission.json()}), 200)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)