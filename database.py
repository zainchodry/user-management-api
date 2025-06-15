from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://ahmed:pgadmin789%40@localhost/mydb4")

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine)

