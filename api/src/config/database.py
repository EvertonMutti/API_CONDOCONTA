# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:15:39 2023

@author: Everton
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:rootadmin@localhost/bancolegal"
engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def createDb():
    Base.metadata.create_all(bind=engine)
    
def resetDb():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind=engine)

def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
