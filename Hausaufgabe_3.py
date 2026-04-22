import sqlalchemy
from sqlalchemy import Column, ForeignKey, Table, DECIMAL, Boolean, String, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base, relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(DECIMAL(10, 2))
    in_stock = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey('category_id'))

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))

    products = relationship('Product', backref='category')