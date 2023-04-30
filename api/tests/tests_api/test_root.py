# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:14:54 2023

@author: Everton
"""

from fastapi.testclient import TestClient


def testGetRoot(client: TestClient) -> None:
    response = client.get("/")
    body = response.json()
    assert body["detail"] == "Not Found"
    assert response.status_code == 404
