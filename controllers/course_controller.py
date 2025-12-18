from flask import Blueprint, request, jsonify, make_response, render_template
from model.base import db
from model.course import Course
from model.user import User

course_bp = Blueprint('course', __name__, url_prefix='/course')

# --- CRUD Operations ---
# Create a course (POST)
@course_bp.route('/create', methods=['POST'])
def create_course():
    data = request.get_json()

    _class_id = data.get('class_id', None)
    _course_id = data.get('course_id', None)
    _section_id = data.get('section_id', None)
    _course_title = data.get('course_title', None)
    _department = data.get('department', None)
    _campus = data.get('campus', None)
    _term = data.get('term', None)
    _days_offered = data.get('days_offered', None)
    _times_offered = data.get('times_offered', None)
    _enroll_status = data.get('enroll_status', None)
    _credits = data.get('credits', None)

    new_course = Course(class_id=_class_id,
                        course_id=_course_id,
                        section_id=_section_id,
                        course_title=_section_id,
                        department=_department,
                        campus=_campus,
                        term=_term,
                        days_offered=_days_offered,
                        times_offered=_times_offered,
                        enroll_status=_enroll_status,
                        credits=_credits,
                        )
    db.session.add(new_course)
    db.session.commit()
    return make_response(jsonify({'message': 'course created', 'course': new_course.json()}), 201)

# Read all courses (GET)
@course_bp.route('/all', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return render_template('course/list_all.html', courses=[course for course in courses])
    # return make_response(jsonify([course.json() for course in courses]), 200)

# Read a single course by ID (GET)
@course_bp.route('/register', methods=['GET'])
def get_course():
    courses = Course.query.all()
    return render_template(template_name_or_list='course/register.html', courses=[course for course in courses])
    #return make_response(jsonify({'course': course.json()}), 200)

# Update a course by ID (PUT/PATCH)
@course_bp.route('/<int:class_id>', methods=['PUT'])
def update_course(class_id):
    course = Course.query.get_or_404(class_id)
    data = request.get_json()
    course.class_id = data.get('class_id', course.class_id)
    course.course_id = data.get('course_id', course.course_id)
    course.section_id = data.get('section_id', course.section_id)
    course.course_title = data.get('course_title', course.course_title)
    course.department = data.get('department', course.department)
    course.campus = data.get('campus', course.campus)
    course.term = data.get('term', course.term)
    course.days_offered = data.get('days_offered', course.days_offered)
    course.times_offered = data.get('times_offered', course.times_offered)
    course.enroll_status = data.get('enroll_status', course.enroll_status)
    course.credits = data.get('credits', course.credits)
    db.session.commit()
    return make_response(jsonify({'message': 'course updated', 'course': course.json()}), 200)

# Delete a course by ID (DELETE)
@course_bp.route('/<int:class_id>', methods=['DELETE'])
def delete_course(class_id):
    course = Course.query.get_or_404(class_id)
    db.session.delete(course)
    db.session.commit()
    return make_response(jsonify({'message': 'class deleted'}), 200)


# Add a user by username to a class by id
@course_bp.route('/<int:class_id>/add/<username>', methods=['GET'])
def add_user_to_course(username, role_id):
    user = User.query.filter_by(user_username=User.username).first()
     # Need to query the model/table correctly, copied from role controller
    course = Course.query.filter_by(class_id=Course.class_id)
    user.roles.append(course)
    db.session.add(user)
    db.session.commit()

    return make_response(jsonify({'r': role_id, 'un': username}))