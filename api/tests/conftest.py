# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:10:24 2023

@author: Everton
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except:
    raise

import pytest  
from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from jose import jwt
from api.main import app
from api.create_database import resetDb

DATABASE_URL = 'mysql+pymysql://root:rootadmin@localhost/teste'
os.environ['DATABASE_URL'] = DATABASE_URL
        
resetDb()

SECRET_KEY = "ImsexyandIknowit"
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3 * 10000

def createAccessToken(data: dict = {'sub': "admin@admin.com"}):
    data_copy = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    data_copy.update({'exp': expiration})
    token_jwt = jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


@pytest.fixture(scope="function") #the same thing setUp from unittest
def client():
    with TestClient(app) as client:
        user = {"name": "admin", "email": "admin@admin.com", "password": "mypassword"}
        client.post("/User/signup", json=user)
        token = createAccessToken({'sub': "admin@admin.com"})
        client.headers["Authorization"] = f"Bearer {token}"
        yield client
 