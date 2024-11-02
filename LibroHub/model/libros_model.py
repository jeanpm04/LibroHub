import reflex as rx
from typing import Optional
from sqlmodel import Field

#mapeamos la tabla "libros"
class Libros(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    autor: str
    anio_publicacion: int
    genero: str