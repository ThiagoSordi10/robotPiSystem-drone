# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_tables import Raspberry, Base

engine = create_engine('sqlite:///data.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

def get_raspberry():
    raspberry = session.query(Raspberry).first()
    if( raspberry is None):
        return None
        #raspberry = Raspberry(id="none", nome="Insira meu novo nome")
        #session.add(raspberry)
        #session.commit()

    return raspberry

def salvar_raspberry(_id, nome, empresa_id, estacao_id):
    raspberry = Raspberry(id = _id, nome = nome, empresa_id = empresa_id, estacao_id = estacao_id)
    session.add(raspberry)
    session.commit()


