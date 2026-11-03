from .modelos import Producto
from .excepciones import ProductoNoEncontradoError


class Inventario:
    """Administra los productos disponibles en el sistema."""

    def __init__(self):
        """Crea un inventario vacío."""
        self._productos = {}

    @property
    def categorias(self):
        """Devuelve las categorías presentes en el inventario."""
        return {producto.categoria for producto in self._productos.values()}

    def agregar(self, producto: Producto):
        """Agrega un producto; rechaza códigos que ya existen."""
        if producto.codigo in self._productos:
            raise ValueError(f"Ya existe el producto {producto.codigo}.")
        self._productos[producto.codigo] = producto

    def buscar(self, termino):
        """Busca por código exacto o por parte del nombre."""
        termino = str(termino).strip()
        if not termino:
            return None

        codigo = termino.upper()
        if codigo in self._productos:
            return self._productos[codigo]

        termino = termino.casefold()
        for producto in self._productos.values():
            if termino in producto.nombre.casefold():
                return producto
        return None
    def obtener(self, termino):
        """Devuelve un producto o informa si no se encontró."""
        producto = self.buscar(termino)
        if producto is None:
            mensaje = f"No se encontró el producto: {termino}."
            raise ProductoNoEncontradoError(mensaje)
        return producto
    
    def ordenar(self, criterio="nombre"):
        """Devuelve los productos ordenados por nombre o precio."""
        productos = list(self._productos.values())

        if criterio == "nombre":
            return sorted(productos, key=lambda producto: producto.nombre.casefold())
        if criterio == "precio":
            return sorted(productos, key=lambda producto: producto.precio)
        raise ValueError("El criterio debe ser 'nombre' o 'precio'.")

    def __iter__(self):
        """Permite recorrer los productos con un ciclo for."""
        return iter(self._productos.values())

    def __len__(self):
        """Devuelve cuántos productos contiene el inventario."""
        return len(self._productos)

    def __contains__(self, codigo):
        """Indica si el código está registrado."""
        codigo = str(codigo).strip().upper()
        return codigo in self._productos

    def __str__(self):
        """Devuelve un resumen legible del inventario."""
        return f"Inventario con {len(self)} productos."

    def __repr__(self):
        """Devuelve una representación técnica del inventario."""
        return f"Inventario(productos={len(self)})"