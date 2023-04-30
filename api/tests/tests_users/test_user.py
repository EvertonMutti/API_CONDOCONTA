# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 00:08:18 2023

@author: Everton
"""
from fastapi.testclient import TestClient


def test_signup(client: TestClient):
    user = {"name": "admin", "email": "admin@admin2.com", "password": "mypassword"}
    response = client.post("/User/signup", json=user)
    assert response.status_code == 201 #http created
    assert "user_id" in response.json()
    assert "email" in response.json()
    assert "name" in response.json()

def test_login(client: TestClient):
    user = {"email": "admin@admin.com", "password": "mypassword"}
    response = client.post("/User/login", json=user)
    assert response.status_code == 200
    assert "token" in response.json()
    