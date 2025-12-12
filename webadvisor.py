from flask import Flask, render_template
from model.base import db
from controllers.user_controller import user_bp
from controllers.role_controller import role_bp
from controllers.permission_controller import perm_bp
from controllers.operation_controller import op_bp
from controllers.course_controller import course_bp
from controllers.component_controller import comp_bp

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///../SQLite_DB.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Redwo0d$@127.0.0.1:3306/webadvisor_reboot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize the db instance with the Flask app
db.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(role_bp)
app.register_blueprint(perm_bp)
app.register_blueprint(op_bp)
app.register_blueprint(course_bp)
app.register_blueprint(comp_bp)

# Create the database tables within the application context
def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return render_template('layout.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)