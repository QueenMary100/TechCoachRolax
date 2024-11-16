from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy import Column, Integer, String, TEXT, ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'tbl_user'
    
    id =  Column(Integer, primary_key=True, nullable=False)
    username = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(30))

class Course(db.Model):
    __tablename__ = 'tbl_course'

    id = Column(Integer, primary_key=True, nullable=False)
    course_name = Column(String(50))
    progress = Column(String(50))
    user_id = Column(Integer, ForeignKey('tbl_user.id'))

class QA(db.Model):
    __tablename__ = 'tbl_qa'

    id =   Column(Integer, primary_key=True, nullable=False)
    question = Column(String(255), nullable=False)
    answer = Column(TEXT, nullable=True)
    course_id = Column(Integer, ForeignKey('tbl_course.id'))