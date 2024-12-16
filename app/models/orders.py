import enum

from sqlalchemy import Column, Integer, String, Boolean, DECIMAL, func, Enum
from sqlalchemy.dialects.postgresql import TIMESTAMP, ENUM
from sqlalchemy.orm import relationship

from app.db.session import DBBase


class CreateOrderDB(DBBase):
    __tablename__ = "order_details"
    id = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    side = Column('order_side', String, index=True, nullable=False)
    instrument = Column('instrument', String, nullable=False)
    type = Column('order_type', String, nullable=False)
    price = Column('price', DECIMAL)
    quantity = Column('quantity', Integer)
    created_at = Column('created_at', TIMESTAMP, server_default=func.now())
    updated_at = Column('updated_at', TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    orderPlaced = Column('order_placed', Boolean, default=False)