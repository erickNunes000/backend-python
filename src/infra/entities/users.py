# from config import Base, DBConnectionHandler
from src.infra.config import Base, DBConnectionHandler
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship


from sqlalchemy.ext.declarative import declarative_base

MyBase = declarative_base()


class Users(Base):
    """Users Entity Class"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pets")

    def __repr__(self) -> str:
        return f"Usr name={self.name}"
