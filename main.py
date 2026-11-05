"""Punto de entrada principal para el Sistema de Inventario y Ventas."""
from inventario.app import SistemaInventario

if __name__ == "__main__":
    app = SistemaInventario("datos/inventario.csv", "datos/log.txt")
    app.ejecutar()