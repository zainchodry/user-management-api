from sqlalchemy import String, Column, Integer

from database import Base, engine

def create_tables():
    Base.metadata.create_all(engine)



class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = True)
    email = Column(String(100), nullable = True)
    phone = Column(String(15), nullable=False)
    