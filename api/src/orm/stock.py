# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:34:18 2023

@author: Everton
"""

from sqlalchemy import update, delete, select
from src.schemas.schemas import product_schema as Product
from src.models import models
from datetime import datetime


class Stock():
    def __init__(self, db):
        self.db = db

    def createProduct(self, product: Product):
        db_product = models.Product(
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def listProduct(self):
        db_products = self.db.query(models.Product.product_id, models.Product.name ).all()
        return db_products

    def detailProduct(self, id: int):
        query = select(models.Product).where(models.Product.product_id == id)
        product = self.db.execute(query).first()
        return product

    def editProduct(self, id: int, product: Product):
        update_product = update(models.Product).where(
            models.Product.product_id == id).values(name=product.name,
                                                    description=product.description,
                                                    price=product.price,
                                                    quantity=product.quantity,
                                                    updated_at=datetime.now()
                                                    )

        self.db.execute(update_product)
        self.db.commit()
        updated_product = self.detailProduct(id)
        return updated_product

    def removeProduct(self, id: int):
        delete_product = delete(models.Product).where(
            models.Product.product_id == id
        )

        self.db.execute(delete_product)
        self.db.commit()
        return None
