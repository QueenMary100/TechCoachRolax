from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from urllib.parse import quote
import os


user = os.environ.get('USERNAME')
pwd = quote(os.environ.get('PASSWORD'))
host = os.environ.get('HOST')
database = os.environ.get('DATABASE')


app = Flask(__name__)

db = SQLAlchemy()

uri = f'mysql+mysqldb://{user}:{pwd}@{host}:3306/{database}'

app.config['SQLALCHEMY_DATABASE_URI'] = uri

# defining routes

# post question

# get question

# track progress



if __name__ == '__main__':
    app.run(port=5000, debug=True)