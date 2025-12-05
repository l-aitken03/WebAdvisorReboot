from flask import Blueprint, jsonify, make_response#, request
from model.operation import Operation

op_bp = Blueprint('operation', __name__,
                    template_folder='templates',
                    static_folder='static', url_prefix='/op')

# --- C[R]UD Operations [READ ONLY] ---

# Read all operations (GET)
@op_bp.route('/all', methods=['GET'])
def get_operations():
    operations = Operation.query.all()
    return make_response(jsonify([operation.json() for operation in operations]), 200)

# Read a single operation by ID (GET)
@op_bp.route('/<int:perm_id>', methods=['GET'])
def get_operation(perm_id):
    operation = Operation.query.get_or_404(perm_id)
    return make_response(jsonify({'operation': operation.json()}), 200)