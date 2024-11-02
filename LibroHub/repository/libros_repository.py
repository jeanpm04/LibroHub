from .connect_db import connect
from sqlmodel import Session, select
from ..model.libros_model import Libros

#función para seleccionar todos los registros
#select * from libros
def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Libros)
        return session.exec(query).all()

#select * from libros where genero = tipo
def select_libros_by_tipo(tipo: str):
    engine = connect()
    with Session(engine) as session:
        query = select(Libros).where(Libros.genero == tipo)
        return session.exec(query).all()

#función para registrar libros
def create_libros(libros:Libros):
    engine = connect()
    with Session(engine) as session:
        session.add(libros)
        session.commit()
        query = select(Libros)
        return session.exec(query).all()

#función para eliminar libros
def delete_libros(nombre: str):
    engine = connect()
    with Session(engine) as session:
        query = select(Libros).where(Libros.titulo == nombre)
        libros_delete = session.exec(query).one()
        session.delete(libros_delete)
        session.commit()
        query = select(Libros)
        return session.exec(query).all()