class Producto:
    """Representa un producto del inventario."""

    def __init__(self, codigo, nombre, categoria, precio, stock):
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
        valor = str(valor).strip().upper()
        if len(valor) != 3 or valor[0] != "P" or not valor[1:].isdigit():
            raise ValueError("El código debe tener formato P01, P02, etc.")
        self._codigo = valor

    @property
    def nombre(self):
        """Devuelve el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
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
        valor = str(valor).strip() or "General"
        self._categoria = valor

    @property
    def precio(self):
        """Devuelve el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor):
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
            raise ValueError("No hay suficiente stock para completar la venta.")
        self.stock -= cantidad