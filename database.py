from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()
engine = create_engine()

class Stelling(Base):
    __tablename__ = 'stellingen'
    
    id = Column(Integer, primary_key=True)
    content = Column(String)
    
class Stem(Base):
    __tablename__ = 'stemmen'
    
    id = Column(Integer, primary_key=True)
    stelling_id = Column(Integer, ForeignKey('stellingen.id'))
    stelling = relationship("Stelling", backref=backref('stemmen', order_by=id)
    


Base.metadata.create_all(engine)

Session = sessionmaker()