from datetime import datetime
import csv
from pathlib import Path

from .inventario import Inventario
from .modelos import Producto


class RepositorioCSV:
    """Lee y guarda los productos en un archivo CSV."""

    CAMPOS = ["codigo", "nombre", "categoria", "precio", "stock"]

    def __init__(self, ruta):
        """Prepara la ruta del archivo de inventario."""
        self._ruta = Path(ruta)

    def cargar(self):
        """Carga los productos y devuelve un objeto Inventario."""
        inventario = Inventario()

        if not self._ruta.exists():
            self.guardar(inventario)
            return inventario

        with self._ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                producto = Producto(
                    codigo=fila["codigo"],
                    nombre=fila["nombre"],
                    categoria=fila["categoria"],
                    precio=fila["precio"],
                    stock=fila["stock"],
                )
                inventario.agregar(producto)

        return inventario

    def guardar(self, inventario):
        """Escribe todos los productos en el archivo CSV."""
        self._ruta.parent.mkdir(parents=True, exist_ok=True)

        with self._ruta.open("w", encoding="utf-8-sig", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=self.CAMPOS)
            escritor.writeheader()

            for producto in inventario:
                escritor.writerow({
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "precio": producto.precio,
                    "stock": producto.stock,
                })
class Bitacora:
    """Registra las operaciones del sistema en un archivo."""

    def __init__(self, ruta):
        """Prepara la ruta donde se guardará la bitácora."""
        self._ruta = Path(ruta)

    def registrar(self, mensaje):
        """Agrega un mensaje con fecha y hora al final del archivo."""
        self._ruta.parent.mkdir(parents=True, exist_ok=True)
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with self._ruta.open("a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha_hora}] {mensaje}\n")