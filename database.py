from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()
engine = create_engine()

class Poll(Base):
    __tablename__ = 'polls'
    
    id = Column(Integer, primary_key=True)
    content = Column(String)
    
class Vote(Base):
    __tablename__ = 'votes'
    
    id = Column(Integer, primary_key=True)
    option = Column(Integer)
    poll_id = Column(Integer, ForeignKey('polls.id'))
    poll = relationship("Poll", backref=backref('polls', order_by=id)
    post_date = Column(DateTime)
    
class Forum(Base):
    __tablename__ = 'fora'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    
class Reaction(Base):
    __tablename__ = 'reactions'
    
    id = Column(Integer, primary_key=True)
    content = Column(String)
    name = Column(String)
    forum_id = Column(Integer, ForeignKey('fora.id'))
    forum = relationship("Fora", backref=backref('reactions', order_by=id)
    post_date = Column(DateTime)
    
Base.metadata.create_all(engine)

Session = sessionmaker()