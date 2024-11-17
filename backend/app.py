from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from urllib.parse import quote
import os


user = os.environ.get('DB_USERNAME')
pwd = os.environ.get('PASSWORD')
pwd = quote(pwd)
print(pwd)
host = os.environ.get('HOST')
database = os.environ.get('DATABASE')


app = Flask(__name__)

uri = f'mysql+mysqldb://{user}:{pwd}@{host}:3306/{database}'

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
from model import User, Course, QA

@app.route("/")
def main():
    return "success hit"

# defining routes

# post question
@app.route('/query', methods=['POST'])
def query():
    username = request.json.get('username')
    course = request.json.get('course')
    question = request.json.get('question')

    course_obj = db.session.execute(db.select(Course).filter_by(course_name=course)).scalar()
    print("Course", course_obj)
    course_id = course_obj.id

    user_query = QA(question=question, course_id=course_id)
    try:
        db.session.add(user_query)
        db.session.commit()
        return make_response(jsonify({
            "message": "question sent successfully"
        }),201)
    except Exception as e:
        return make_response(jsonify({
            "message": f"{str(e)}"
        }), 400)

# get question

@app.route('/query')
def get_queries():
    questions = db.session.execute(db.select(QA)).scalars()

    query_list = []
    
    for query in questions:
        print(query)
        query_list.append({
            'question': query.question
        })
    return make_response(jsonify({
        "questions": query_list
    }), 200)

# track progress
@app.route("/progress")
def set_progress():
    pass


@app.route("/answer", methods=['POST'])
def answer():
    username = request.json.get('username')
    question_id = request.json.get('question_id')
    answer = request.json.get('answer')
    
    question = db.session.execute(db.select(QA).filter_by(id=question_id)).scalar()

    try:
        question.answer = answer
        db.session.commit()
        return make_response(jsonify({
            "message": "answer submitted successfully"
        }), 200)
    except Exception as e:
        return make_response(jsonify({
            "message": f"{str(e)}"
        }), 400)



try:
    with app.app_context():
        db.create_all()  # Create tables
        print("Database tables created successfully.")
except Exception as e:
    print(f"Error initializing the database: {e}")
app.run(port=5000, debug=True)