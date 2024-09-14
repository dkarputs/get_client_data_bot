from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Настройка базы данных
Base = declarative_base()

class User(Base):
    __tablename__ = 'audience'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

engine = create_engine('postgresql:///users.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()