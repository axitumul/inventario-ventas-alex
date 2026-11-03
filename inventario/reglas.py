from abc import ABC, abstractmethod


class ReglaNegocio(ABC):
    """Define la operación común para las reglas del sistema."""

    @abstractmethod
    def aplicar(self, inventario):
        """Devuelve los productos a los que se aplica la regla."""
        pass


class AlertaStockMinimo(ReglaNegocio):
    """Encuentra productos cuyo stock llegó al mínimo o está por debajo."""

    def __init__(self, limite=3):
        """Crea la alerta con el límite indicado."""
        self.limite = limite

    @property
    def limite(self):
        """Devuelve el límite mínimo de stock."""
        return self._limite

    @limite.setter
    def limite(self, valor):
        """Valida y asigna el límite mínimo de stock."""
        valor = int(valor)
        if valor < 0:
            raise ValueError("El límite de stock no puede ser negativo.")
        self._limite = valor

    def aplicar(self, inventario):
        """Devuelve los productos con stock menor o igual al límite."""
        return [
            producto
            for producto in inventario
            if producto.stock <= self.limite
        ]


class AlertaStockAgotado(AlertaStockMinimo):
    """Especializa la alerta para productos sin existencias."""

    def __init__(self):
        """Configura la alerta para encontrar productos con stock cero."""
        super().__init__(limite=0)

    def aplicar(self, inventario):
        """Devuelve los productos cuyo stock es exactamente cero."""
        return [
            producto
            for producto in inventario
            if producto.stock == 0
        ]