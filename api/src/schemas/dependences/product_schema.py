# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:17:57 2023

@author: Everton
"""

from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    product_id: Optional[int] = None
    name : str 
    description : str 
    price: float 
    quantity: int
    
    class Config: 
        orm_mode = True