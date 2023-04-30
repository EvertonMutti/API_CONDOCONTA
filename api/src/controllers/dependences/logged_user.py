# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 17:13:26 2023

@author: Everton
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
from src.config.database import getDb
from src.orm.user import UserAuth

from src.security.token_provider import verifyAcessToken


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


async def verifyLoggedUser(token: str = Depends(oauth2_schema), 
                     session: Session = Depends(getDb)):
    try:
        payload = verifyAcessToken(token)
            
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
        
    user = UserAuth(session).locationUser(payload)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
