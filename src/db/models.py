from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Uuid, Float
from sqlalchemy.orm import relationship

from .database import Base


class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(Uuid, primary_key=True)
    nome = Column(String, unique=True, index=True)
    


class Produto(Base):
    __tablename__ = "produto"

    id = Column(Uuid, primary_key=True)
    nome = Column(String, unique=True, index=True)
    descricao = Column(String, index=True)
    imagem_url = Column(String, index=True)
    preco = Column(Float)
    categoria = relationship("Categoria", foreign_keys="categoria.id")
