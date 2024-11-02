import reflex as rx
from .model.libros_model import Libros
from .service.libros_service import select_all_libros_service, select_libros_by_tipo_service, create_libros_service, delete_libros_service

class LibrosState(rx.State):
    #states
    libros:list[Libros]
    libros_buscar: str

    def agregar_al_carrito(self, titulo: str):
        self.carrito.append(titulo)

    @rx.background
    async def get_all_libros(self):
        async with self:
            self.libros = select_all_libros_service()

    @rx.background
    async def get_libros_by_tipo(self):
        async with self:
            self.libros = select_libros_by_tipo_service(self.libros_buscar)

    @rx.background
    async def create_libros(self, data: dict):
        async with self:
            try:
                self.libros = create_libros_service(titulo=data['titulo'], autor=data['autor'], anio_publicacion=data['anio_publicacion'], genero=data['genero'])
            except BaseException as be:
                print(be.args)

    def buscar_on_change(self, value: str):
        self.libros_buscar = value

    @rx.background
    async def delete_libros_by_nombre(self, nombre):
        async with self:
            self.libros = delete_libros_service(nombre)

#barra de navegación
def navigation_menu() -> rx.Component:
    return rx.hstack(
        rx.link(rx.button("Inicio", variant="ghost"), href="/home"),
        rx.link(rx.button("Administrar Libros", variant="ghost"), href="/libros"),
        justify="center",
        style={"padding": "16px", "background-color": "#f8f9fa"}
    )

#página de inicio
@rx.page(route='/home', title='Inicio', on_load=LibrosState.get_all_libros)
def home_page() -> rx.Component:
    return rx.flex(
        navigation_menu(), #menú
        rx.heading('Libros Disponibles', align='center'),
        card_grid_libros(LibrosState.libros), #diseño en tarjetas para los libros
        direction='column',
        style={"width": "80vw", "margin": "auto"}
    )

@rx.page(route='/libros', title='Administrar Libros', on_load=LibrosState.get_all_libros)
def libros_page() -> rx.Component:
    return rx.flex(
        navigation_menu(),  #menú
        rx.heading('Administrar Libros', align='center'),
        rx.hstack(
            buscar_libros_component(),
            create_libros_dialog_component(),
            justify='center',
            style={'margin-top': '30px'}
        ),
        table_libros(LibrosState.libros),  #tabla de administración de libros
        direction='column',
        style={"width": "60vw", "margin": "auto"}
    )

def table_libros(list_libros: list[Libros]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('Titulo'),
                rx.table.column_header_cell('Autor'),
                rx.table.column_header_cell('Año de publicación'),
                rx.table.column_header_cell('Género'),
                rx.table.column_header_cell('Acción')
            )
        ),
        rx.table.body(
            rx.foreach(list_libros, row_table)
        )
    )

def row_table(libros: Libros) -> rx.Component:
    return rx.table.row(
        rx.table.cell(libros.titulo),
        rx.table.cell(libros.autor),
        rx.table.cell(libros.anio_publicacion),
        rx.table.cell(libros.genero),
        rx.table.cell(rx.hstack(
            delete_libros_dialog_component(libros.titulo),
        ))
    )

def buscar_libros_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese tipo/género', on_change=LibrosState.buscar_on_change),
        rx.button('Buscar libro', on_click=LibrosState.get_libros_by_tipo)
    )

def create_libros_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder='Titulo',
                name='titulo'
            ),
            rx.input(
                placeholder='Autor',
                name='autor'
            ),
            rx.input(
                placeholder='Año de publicación',
                name='anio_publicacion'
            ),
            rx.input(
                placeholder='Género',
                name='genero'
            ),
            rx.dialog.close(
                rx.button('Guardar', type='submit')
            ),
        ),
        on_submit=LibrosState.create_libros,
    )

def create_libros_dialog_component() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button('Crear libro')),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title('Crear libro'),
                create_libros_form(),
                justify='center',
                align='center',
                direction='column',
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button('Cancelar', color_scheme='gray', variant='soft')
                ),
                spacing='3',
                margin_top='16px',
                justify='end',
            ),
            style={'width': '300px'}
        ),
    )

def delete_libros_dialog_component(titulo: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon('trash-2'))),
        rx.dialog.content(
            rx.dialog.title('Eliminar libro'),
            rx.dialog.description('¿Realmente desea eliminar el libro?: ' + titulo),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    ),
                ),
                rx.dialog.close(
                    rx.button('Continuar', on_click=LibrosState.delete_libros_by_nombre(titulo)),
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            )
        )
    )

def card_grid_libros(list_libros: list[Libros]) -> rx.Component:
    return rx.flex(
        rx.foreach(list_libros, create_libro_card),
        wrap="wrap",
        justify="flex-start",
        style={
            "margin-top": "30px",
            "width": "100%",
            "gap": "10px",
        }
    )

def create_libro_card(libros: Libros) -> rx.Component:
    return rx.box(
        rx.heading(libros.titulo, size="sm", align="center"),
        rx.text(f"Autor: {libros.autor}", align="center"),
        rx.text(f"Año: {libros.anio_publicacion}", align="center"),
        rx.text(f"Género: {libros.genero}", align="center"),
        rx.spacer(),
        rx.button(
            "Agregar", 
            color_scheme="green", 
            variant="solid", 
            size="sm", 
            on_click=lambda: LibrosState.agregar_al_carrito(libros.titulo)
        ),
        style={
            "border": "1px solid #ccc",
            "border-radius": "8px",
            "padding": "12px",
            "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
            "text-align": "center",
            "display": "flex",
            "flex-direction": "column",
            "align-items": "center",
            "justify-content": "space-between",
            "width": "200px",
            "height": "250px",
        }
    )