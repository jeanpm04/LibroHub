class Nodo:
    def __init__(self, libro):
        self.libro = libro
        self.siguiente = None  # Puntero al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Puntero al primer nodo de la lista

    def insertar(self, libro):
        nuevo_nodo = Nodo(libro)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"Libro '{libro}' agregado a la lista.")

    def eliminar(self, titulo):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.libro['titulo'] == titulo:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"Libro '{titulo}' eliminado de la lista.")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"Libro '{titulo}' no encontrado en la lista.")

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.libro)
            actual = actual.siguiente