# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 22:45:57 2023

@author: Everton
"""

from src.config.database import createDb, resetDb
from src.models.models import Product, User

if __name__ == "__main__":
    createDb() #drop table and create table