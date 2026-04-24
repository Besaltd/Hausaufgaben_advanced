from unicodedata import name, category

import sqlalchemy
from sqlalchemy import Column, ForeignKey, Table, DECIMAL, Boolean, String, Integer, create_engine, func
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base, relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(DECIMAL(10, 2))
    in_stock = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey('category.id'))

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))

    products = relationship('Product', backref='category')

engine = create_engine("sqlite:///products.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# electronics = Category(name='Electronics', description="Gadgets and devices")
# books = Category(name='Books', description="Printed and electronic books")
# clothing = Category(name='Clothing', description="Men's and women's clothing")
#
# session.add_all([electronics, books, clothing])
# session.commit()
#
# smartphone = Product(name='Smartphone', price=299.99, in_stock=True, category=electronics)
# laptop = Product(name='Laptop', price=499.99, in_stock=True, category=electronics)
# book = Product(name='Science fiction novel', price=15.99, in_stock=True, category=books)
# t_shirt = Product(name='T-shirt', price=20.00, in_stock=True, category=clothing)
#
# session.add_all([smartphone, laptop, book, t_shirt])
# session.commit()

print("'READ'")

session = Session(bind=engine)
products = session.query(Product).all()

for p in products:
    print(
        f"ID: {p.id}, "
        f"Name: {p.name}, "
        f"Price: {p.price}, "
        f"In stock: {p.in_stock}, "
        f"Category: {p.category.name}")

print("\n'UPDATE'")

updated = session.query(Product).filter(Product.name == 'Smartphone').first()
print(f"Updated: {updated.name}, {updated.price}")

print("\n'GROUP BY'")

total_count = session.query(Category.name, func.count(Product.id)).join(Category.products).group_by(Category.id).all()
for name, count in total_count:
    print(name, count)

print("\n'FILTER'")

filtered = session.query(Category.name, func.count(Product.id)).join(Category.products).group_by(Category.id).having(func.count(Product.id) > 1).all()

for name, count in filtered:
    print(name, count)