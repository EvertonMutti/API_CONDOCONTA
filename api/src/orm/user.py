# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 00:40:07 2023

@author: Everton
"""

from sqlalchemy import select
from src.schemas.schemas import user_schema
from src.models import models


class UserAuth():
    def __init__(self, db):
        self.db = db

    def createUser(self, user: user_schema.User):
        db_user = models.User(
            name=user.name,
            email=user.email,
            password=user.password,
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def locationUser(self, email: str):
        query = select(models.User).where((models.User.email == email))
        user = self.db.execute(query).first()
        return user

    def validatorLogin(self, login: user_schema.Login):
        query = select(models.User.user_id, models.User.name, models.User.email,
                       models.User.password).where((models.User.email == login.email)
                                                   and (models.User.password == login.password))
        user = self.db.execute(query).first()
        return user

