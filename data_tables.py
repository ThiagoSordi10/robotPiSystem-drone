import sqlite3

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

# connection = sqlite3.connect('data.db')
#
# cursor = connection.cursor()
#
# create_table = "CREATE TABLE IF NOT EXISTS raspberry (id String PRIMARY KEY, nome text, estacao_id text)"
# cursor.execute(create_table)
#
# create_table = "CREATE TABLE IF NOT EXISTS comando (name text, price real)"
# cursor.execute(create_table)
#
# create_only_raspberry_row = "a"
#
# connection.commit()
#
# connection.close()



Base = declarative_base()


class Raspberry(Base):
    __tablename__ = 'raspberry'
    # Here we define columns for the table raspberry
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    nome = Column(String(250), nullable=False)
    empresa_id = Column(String(250), nullable=True)
    estacao_id = Column(String(250), nullable=True)


class Comando(Base):
    __tablename__ = 'comando'
    # Here we define columns for the table comando.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    horario_chegada = Column(DateTime, nullable=True)
    estacao_id = Column(String(250), nullable=False)

class Estacao(Base):
    __tablename__ = 'estacao'
    # Here we define columns for the table comando.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), primary_key=True)
    nome = Column(String(250), nullable=False)
    empresa_id = Column(String(250), nullable=False)
    posicao = Column(Integer, nullable=False)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///data.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
