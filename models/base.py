from sqlalchemy import Column,Integer,String,create_engine,JSON,BigInteger,DateTime
from sqlalchemy.orm import DeclarativeBase,Session
import datetime
engine = create_engine('sqlite:///models/histori.db')
class Base(DeclarativeBase): pass
class Histori(Base):
    __tablename__ = 'historis'
    id = Column(Integer,primary_key=True)
    user_id = Column(BigInteger)
    fractal_type = Column(String)
    parameters = Column(JSON)
    timestamp = Column(DateTime,default=datetime.datetime.utcnow)
    image_patch = Column(String)
Base.metadata.create_all(bind=engine)