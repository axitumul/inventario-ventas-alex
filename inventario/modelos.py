from dataclasses import dataclass
from .excepciones import CodigoInvalidoError, StockInsuficienteError
class Producto:
    """Representa un producto del inventario."""

    def __init__(self, codigo, nombre, categoria, precio, stock):
        """Inicializa un producto con sus datos."""
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria or "General"
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self):
        """Devuelve el código del producto."""
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        """Valida y asigna el código del producto."""
        valor = str(valor).strip().upper()
        if len(valor) != 3 or valor[0] != "P" or not valor[1:].isdigit():
            raise CodigoInvalidoError("El código debe tener formato P01, P02, etc.")
        self._codigo = valor

    @property
    def nombre(self):
        """Devuelve el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Valida y asigna el nombre del producto."""
        valor = str(valor).strip()
        if not valor:
            raise ValueError("El nombre no puede quedar vacío.")
        self._nombre = valor

    @property
    def categoria(self):
        """Devuelve la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        """Valida y asigna la categoría del producto."""
        valor = str(valor).strip() or "General"
        self._categoria = valor

    @property
    def precio(self):
        """Devuelve el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor):
        """Valida y asigna el precio del producto."""
        valor = float(valor)
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    @property
    def stock(self):
        """Devuelve las unidades disponibles."""
        return self._stock

    @stock.setter
    def stock(self, valor):
        """Valida y asigna las unidades disponibles."""
        valor = int(valor)
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    def __str__(self):
        """Devuelve un resumen legible del producto."""
        return f"{self.codigo} - {self.nombre} (Q{self.precio:.2f}, stock: {self.stock})"
    def __repr__(self):
        """Devuelve una representación técnica del producto."""
        return f"Producto(codigo={self.codigo!r}, nombre={self.nombre!r})"

    def descontar_stock(self, cantidad):
        """Reduce el stock si la cantidad es positiva y está disponible."""
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero.")
        if cantidad > self.stock:
            raise StockInsuficienteError("No hay suficiente stock para completar la venta.")
        self.stock -= cantidad

@dataclass(frozen=True)
class Venta:
    """Guarda los datos de una venta sin permitir que se modifiquen."""

    fecha: str
    codigo_producto: str
    nombre_producto: str
    cantidad: int
    precio_unitario: float

    @property
    def total(self):
        """Calcula el total de la venta."""
        return self.cantidad * self.precio_unitario