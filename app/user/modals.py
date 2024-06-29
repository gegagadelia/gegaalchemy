from flask import *
from sqlalchemy import *
from  flask_sqlalchemy import *
from   sqlalchemy.orm import *

from app.extensions import db

class User(db.Modal):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    age: Mapped[int]
    adress: Mapped[str]
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str]



