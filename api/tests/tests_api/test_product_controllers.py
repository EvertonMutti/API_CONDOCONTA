# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 20:53:29 2023

@author: Everton
"""

from fastapi.testclient import TestClient


def test_create_product(client: TestClient):
    product = {
        "name": "Produto teste",
        "description": "Descrição do produto de teste",
        "price": 12.50,
        "quantity": 10
    }
    response = client.post("/products/create/product", json=product)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == product["name"]
    assert response.json()["description"] == product["description"]
    assert response.json()["price"] == product["price"]
    assert response.json()["quantity"] == product["quantity"]


def test_get_product(client: TestClient):
    response = client.get("/products/detail/product/1")
    assert response.status_code == 200
    assert response.json()["Product"]["product_id"] == 1


def test_list_products(client: TestClient):
    response = client.get("/products/list/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_update_product(client: TestClient):
    product = {
        "name": "Produto teste atualizado",
        "description": "Nova descrição do produto de teste",
        "price": 15.99,
        "quantity": 20
    }
    response = client.put("/products/edit/product/1", json=product)
    assert response.status_code == 200
    assert response.json()["Product"]["name"] == product["name"]
    assert response.json()["Product"]["description"] == product["description"]
    assert response.json()["Product"]["price"] == product["price"]
    assert response.json()["Product"]["quantity"] == product["quantity"]


def test_remove_product(client: TestClient):
    response = client.delete("/products/delete/product/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Product removed successfully"
