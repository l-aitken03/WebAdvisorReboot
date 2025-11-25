from flask import Flask, jsonify, make_response#, request
from model.base import db
from model.operation import Operation

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
@app.route('/operations', methods=['GET'])
def get_operations():
    operations = Operation.query.all()
    return make_response(jsonify([operation.json() for operation in operations]), 200)

# Read a single role by ID (GET)
@app.route('/operations/<int:perm_id>', methods=['GET'])
def get_operation(perm_id):
    operation = Operation.query.get_or_404(perm_id)
    return make_response(jsonify({'operation': operation.json()}), 200)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)