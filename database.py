from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean

engine = create_engine("sqlite:///database.sqlite3", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer)
    guardian_id = Column(Integer)
    parent = Column(String)
    name = Column(String)
    description = Column(String)
    location = Column(String)
    usage_frequency_frequency = Column(String)
    usage_function_function = Column(String)
    stored = Column(Boolean)
    placa = Column(String)
    working_state_state = Column(String)
    working_state_description = Column(String)
    picture_path = Column(String)
    barcode_id = Column(String)


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    picture_path = Column(String)
    barcode_id = Column(String)


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    picture_path = Column(String)
    punishment = Column(String)
