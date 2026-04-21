import sqlalchemy
from sqlalchemy import (
    create_engine, Integer, String, Numeric, Boolean, ForeignKey, inspect, text
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column,
    relationship, sessionmaker
)


engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    in_stock: Mapped[bool] = mapped_column(Boolean, default=True)

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))

    products = relationship('Product', backref='category')


Base.metadata.create_all(engine)

# cat = Category(name='Cars', description='All types of cars')
#
# mers = Product(name='Mercedes', price=50000, in_stock=True, category=cat)
# bmw = Product(name='BWM', price=35000, in_stock=False, category=cat)
# audi = Product(name='Audi', price=45000, in_stock=True, category=cat)
#
# session.add(cat)
# session.add_all([mers, bmw, audi])
# session.commit()
#
# with engine.connect() as connect:
#     print(f"Products: ")
#     rows = connect.execute(text("SELECT * FROM products")).fetchall()
#     for _ in rows:
#         print(_)
#
#     print(f"\nCategories: ")
#     rows = connect.execute(text("SELECT * FROM categories")).fetchall()
#     for _ in rows:
#         print(_)
#
# insp = inspect(engine)
#
# print(insp.get_table_names())
# print(insp.get_columns('products'))
# print(insp.get_columns('categories'))

