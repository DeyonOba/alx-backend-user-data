#!/usr/bin/env python3
"""
User Model Module.


User
----

Creates an SQLAlchemy model named `User` for a database table named
`Users` (by using the mapping declaration) of SQLAlchemy.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class User(Base):
    """
    Creates an SQLAlchemy model named `User` for a database table named
    `Users` (by using the mapping declaration) of SQLAlchemy.

    The model will have the following attributes:

        - `id`, the integer primary key
        - `email`, a non-nullable string
        - `hashed_password`, a non-nullable string
        - `session_id`, a nullable string
        - `reset_token`, a nullable string
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(length=250), nullable=False)
    hashed_password = Column(String(length=250), nullable=False)
    session_id = Column(String(length=250))
    reset_token = Column(String(length=250))
