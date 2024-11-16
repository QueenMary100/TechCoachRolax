from flask import Flask
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
    return "<h1>Project working fine</h1>"

# defining routes

# post question

# get question

# track progress



try:
    with app.app_context():
        db.create_all()  # Create tables
        print("Database tables created successfully.")
except Exception as e:
    print(f"Error initializing the database: {e}")
app.run(port=5000, debug=True)