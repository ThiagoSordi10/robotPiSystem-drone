# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_tables import Comando, Base

engine = create_engine('sqlite:///data.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def salvar_comando(_id, estacao_id):
    comando = Comando(id = _id, estacao_id = estacao_id)
    session.add(comando)
    session.commit()
    return comando


