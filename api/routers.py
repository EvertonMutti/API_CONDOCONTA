# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:44:59 2023

@author: Everton
"""

from fastapi import APIRouter
from src.controllers import product, user

router = APIRouter()

#Router products
router.include_router(product.router, prefix="/products", tags=['Products'])
#Router authentication and authorization
router.include_router(user.router, prefix="/User", tags=['Users'])
