# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:26:30 2023

@author: Everton
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas.schemas import product_schema
from src.orm.stock import Stock
from src.config.database import getDb  
from .dependences.logged_user import verifyLoggedUser


router = APIRouter()

# Endpoint para criar um produto específico 
@router.post("/create/product")
async def createProduct(product: product_schema.Product, 
                        db: Session = Depends(getDb),
                        logger_user = Depends(verifyLoggedUser)):                      
    product_created = Stock(db).createProduct(product)
    return product_created

# Endpoint para obter os detalhes de um produto específico pelo id
@router.get("/detail/product/{id}")
async def getProduct(id: int, db: Session = Depends(getDb)
                     ,logged_user = Depends(verifyLoggedUser)):
    product = Stock(db).detailProduct(id)
    if not product:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Não há um produto este id = {id}')
    return product

# Endpoint para listar todos os produtos em estoque
@router.get("/list/products")
async def listProducts(db: Session = Depends(getDb),\
                       logged_user = Depends(verifyLoggedUser)):
    products = Stock(db).listProduct()
    return products

# Endpoint para atualizar um produto do estoque pelo id
@router.put("/edit/product/{id}")
async def updateProduct(id: int, product: product_schema.Product,\
                        db: Session = Depends(getDb)\
                        ,logged_user = Depends(verifyLoggedUser)):
    product = Stock(db).editProduct(id, product)
    if not product:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Não há um produto este id = {id}')
    return product

# Endpoint para remover um produto do estoque pelo id
@router.delete("/delete/product/{id}")
async def removeProduct(id: int, db: Session = Depends(getDb),\
                        logged_user = Depends(verifyLoggedUser)):
    Stock(db).removeProduct(id)
    return {"message": "Product removed successfully"}


