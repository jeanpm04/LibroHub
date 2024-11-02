from ..repository.libros_repository import select_all, select_libros_by_tipo, create_libros, delete_libros
from ..model.libros_model import Libros

def select_all_libros_service():
    libros = select_all()
    print(libros)
    return libros

def select_libros_by_tipo_service(tipo: str):
    if(len(tipo) != 0):
        return select_libros_by_tipo(tipo)
    else:
        return select_all()

def create_libros_service(titulo: str, autor: str, anio_publicacion: int, genero: str):
    libros_save = Libros(titulo=titulo, autor=autor, anio_publicacion=anio_publicacion, genero=genero)
    return create_libros(libros_save)

def delete_libros_service(nombre:str):
    return delete_libros(nombre=nombre)