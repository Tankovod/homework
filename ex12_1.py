# ------------- LESSON 11, EXERCISE 1 -------------------
# make some tables with relations



from sqlalchemy import Column, INT, VARCHAR, ForeignKey, TEXT, create_engine, DECIMAL
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return ''.join('_' + i.lower() if i.isupper() else i for i in cls.__name__).strip('_')


class Shop(Base):
    address = Column(VARCHAR(127), nullable=False)


class ShopProduct(Base):
    count = Column(INT, nullable=False)
    product_id = Column(INT, ForeignKey('product.id', ondelete='CASCADE'), nullable=False)
    shop_id = Column(INT, ForeignKey('shop.id', ondelete='CASCADE'), nullable=False)


class Product(Base):
    name = Column(VARCHAR(255), nullable=False)
    description = Column(TEXT, nullable=False)
    slug = Column(VARCHAR(255), nullable=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete='NO ACTION'), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    image = Column(VARCHAR(255), nullable=True)  # path to image


class Category(Base):
    name = Column(VARCHAR(255), nullable=False)
    slug = Column(VARCHAR(255), nullable=False)
    parent_id = Column(INT, ForeignKey('category.id', ondelete='SET NULL'), nullable=True)


class Customer(Base):
    username = Column(VARCHAR(127), nullable=False)
    email = Column(VARCHAR(127), nullable=False)
    role_id = Column(INT, ForeignKey('role.id', ondelete='SET DEFAULT'), default=1, nullable=False)
    referrer_id = Column(INT, ForeignKey('customer.id', ondelete='NO ACTION'), nullable=True)
    points = Column(INT, nullable=False, default=0)


class Role(Base):
    name = Column(VARCHAR(127), nullable=False)

