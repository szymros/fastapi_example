from sqlalchemy import Boolean, Coulmn, ForeginKey, Integer, String
from sqlalchemy.orm import relationship

from .databse import Base

class User(Base):
    __tablename__ = "users"

    id = Coulmn(Integer, primary_key=True, index=True)
    email = Coulmn(String, unique=True, index=True)

    items = relationship("Item", backpopulates="user")

class Item(Base):
    __tablename__: "items"

    id = Coulmn(Integer, primary_key=True, index=True)
    name = Coulmn(String, index=True)
    qty = Coulmn(Integer, index=True)

    user_id = relationship("User", backpopulates="items")
