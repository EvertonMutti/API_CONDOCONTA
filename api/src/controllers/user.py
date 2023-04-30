# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 00:19:56 2023

@author: Everton
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas.schemas import user_schema, user_response
from src.config.database import getDb
from src.orm.user import UserAuth
from src.security import hash_provider, token_provider


router = APIRouter()


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=user_response.UserResponse)
async def signup(user: user_schema.User, session: Session = Depends(getDb)):
    usuario_localizado = UserAuth(session).locationUser(user.email)

    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Já existe um usuário com esse email')

    # criar novo usuario
    user.password = hash_provider.getPasswordHash(user.password)
    user_created = UserAuth(session).createUser(user)
    return user_created


@router.post("/login")
async def Login(login: user_schema.Login, session: Session = Depends(getDb)):
    user = UserAuth(session).validatorLogin(login)

    if not user or not hash_provider.verifyPassword(login.password,user.password):#hash password
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='Email ou Senha incorreta')

    token = token_provider.createAcessToken({'sub': login.email})
    return {'email': login.email, 'token': token}


