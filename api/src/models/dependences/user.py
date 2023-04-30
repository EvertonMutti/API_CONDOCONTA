# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 00:10:29 2023

@author: Everton
"""

from sqlalchemy import Column, Integer, VARCHAR
from src.config.database import Base


class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(VARCHAR(100))
    