import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
import datetime

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    favorites = relationship('Favorite', backref='user')
    logins = relationship('Login', backref='user')

    def to_dict(self):
        return {
            'id': self.id, 
            'email': self.email,
            'username': self.username
        }

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    datetime = Column(DateTime, default=datetime.datetime.now)
    success = Column(Boolean, default=False)
    
class Favorite(Base):
    __tablename__='favorite'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    planet_id= Column(Integer, ForeignKey('planet.id'))
    character_id= Column(Integer, ForeignKey('character.id'))

class Planet(Base):
    __tablename__='planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    pic = Column(String(512))
    favorites = relationship('Favorite', backref='planet')

class Character(Base):
    __tablename__= 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    pic = Column(String(512))
    favorites = relationship('Favorite', backref='character')



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
