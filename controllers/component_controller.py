from flask import Blueprint, jsonify, make_response#, request
from model.component import Component

comp_bp = Blueprint('component', __name__,
                    template_folder='templates',
                    static_folder='static', url_prefix='/comp')
# --- C[R]UD Operations [READ ONLY] ---

# Read all components (GET)
@comp_bp.route('/all', methods=['GET'])
def get_components():
    components = Component.query.all()
    return make_response(jsonify([component.json() for component in components]), 200)

# Read a single component by ID (GET)
@comp_bp.route('/<int:perm_id>', methods=['GET'])
def get_component(perm_id):
    component = Component.query.get_or_404(perm_id)
    return make_response(jsonify({'component': component.json()}), 200)