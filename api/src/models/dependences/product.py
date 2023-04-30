# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:16:12 2023

@author: Everton
"""

from sqlalchemy import Column, Integer, Float, DATETIME, TEXT, INT, VARCHAR
from src.config.database import Base


class Product(Base):
    __tablename__ = 'Product'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name= Column(VARCHAR(100))
    description = Column(TEXT)
    price = Column(Float)
    quantity = Column(INT)
    created_at = Column(DATETIME)
    updated_at= Column(DATETIME)
