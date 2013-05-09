from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///jeugddienst.db')

class Poll(Base):
    __tablename__ = 'polls'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    option1 = Column(String)
    option2 = Column(String)
    option3 = Column(String)
    option4 = Column(String)

class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True)
    option = Column(Integer)
    poll_id = Column(Integer, ForeignKey('polls.id'))
    poll = relationship("Poll", backref=backref('polls', order_by=id))
    post_date = Column(DateTime)
    
    def __init__(self, option, poll):
        self.option = option
        self.poll = poll
        self.post_date = datetime.today()

class Forum(Base):
    __tablename__ = 'fora'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    extra_questions = Column(String)

class Reaction(Base):
    __tablename__ = 'reactions'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    name = Column(String)
    forum_id = Column(Integer, ForeignKey('fora.id'))
    forum = relationship("Forum", backref=backref('reactions', order_by=id))
    post_date = Column(DateTime)
    
    def __init__(self, content, name, forum):
        self.content = content
        self.name = name
        self.forum = forum
        self.post_date = datetime.today()

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)