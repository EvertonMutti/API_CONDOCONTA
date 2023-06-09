# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:47:42 2023

@author: Everton
"""

from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    user_id: Optional[int] = None
    name : str 
    email : str 
    
    class Config: 
        orm_mode = True