from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_properties_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Properties(DeclarativeBase):
    """Sqlalchemy properties model"""
    __tablename__ = "properties"

    id = Column(String(255), primary_key=True)
    title = Column('title', String(255))
    img = Column('img', String(255), nullable=True)
    description = Column('description', String(255), nullable=True)
    price = Column('price', String(255), nullable=True)
    date = Column('date', String(255), nullable=True)
