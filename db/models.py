import enum

from sqlalchemy import DECIMAL, create_engine, Column, BigInteger
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from db import Base
from db.utils import CreatedModel


class Product(CreatedModel):
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(55), nullable=True)
    price: Mapped[float] = mapped_column(DECIMAL(9, 2))
    price2: Mapped[float] = mapped_column(DECIMAL(9, 2), nullable=True)


class LanguageEnum(str, enum.Enum):
    RU = '🇷🇺 Русский'
    UZ = '🇺🇿 Ozbek'


class User(CreatedModel):
    __tablename__ = 'users'
    fullname: Mapped[str] = mapped_column(String(55), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(13))
    language: Mapped[LanguageEnum] = mapped_column(
        Enum(LanguageEnum, name="language_enum"),
        default=LanguageEnum.UZ,
        nullable=False
    )
    age: Mapped[str] = mapped_column(String(55))


class idk(CreatedModel):
    __tablename__ = 'otziv'
    text: Mapped[str] = mapped_column(String(255), nullable=True)


engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/idk")
# engine = create_engine("postgresql+psycopg2://postgres:1@pg:5432/idk")

metadata = Base.metadata.create_all(engine)
