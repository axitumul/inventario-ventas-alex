class InventarioError(Exception):
    """Error base para las excepciones propias del inventario."""

class CodigoInvalidoError(InventarioError):
    """Se lanza cuando el código de un producto tiene formato inválido."""

class ProductoNoEncontradoError(InventarioError):
    """Se lanza cuando no se encuentra un producto en el inventario.""" 

class StockInsuficienteError(InventarioError):
    """Se lanza cuando no hay unidades suficientes para una venta."""