from .inventario import Inventario
from .persistencia import RepositorioCSV, Bitacora
from .reglas import AlertaStockMinimo, AlertaStockAgotado
from .modelos import Producto


class SistemaInventario:
    """Coordina el inventario, los archivos y las opciones del programa."""
    def __init__(self, ruta_csv, ruta_bitacora):
        """Prepara los objetos que coordina el sistema."""
        self.repositorio = RepositorioCSV(ruta_csv)
        self.inventario = self.repositorio.cargar()
        self.bitacora = Bitacora(ruta_bitacora)
        self.alerta_stock = AlertaStockMinimo()
        self.alerta_agotado = AlertaStockAgotado()
    def mostrar_menu(self):
        """Muestra las opciones principales del programa."""
        print("\n=== SISTEMA DE INVENTARIO Y VENTAS ===")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Registrar venta")
        print("4. Consultar inventario")
        print("5. Revisar alertas de stock")
        print("6. Consultar ventas")
        print("7. Salir")
    def ejecutar(self):
        """Muestra el menú y lee la opción del usuario."""
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción (1-7): ").strip()

            if opcion == "7":
                print("Programa finalizado.")
                break
            elif opcion == "4":
                if len(self.inventario) == 0:
                    print("El inventario está vacío.")
                else:
                    for producto in self.inventario:
                        print(producto)
            elif opcion == "1":
                codigo = input("Código del producto (ej. P11): ").strip()
                nombre = input("Nombre del producto: ").strip()
                categoria = input("Categoría: ").strip()

                try:
                    precio = float(input("Precio: "))
                    stock = int(input("Existencias: "))
                    producto = Producto(codigo, nombre, categoria, precio, stock)
                    self.inventario.agregar(producto)
                    self.repositorio.guardar(self.inventario)
                    print(f"Producto {producto.nombre} agregado.")
                except Exception as error:
                    print(f"No se pudo agregar el producto: {error}")
            elif opcion == "2":
                termino = input("Código o nombre del producto: ").strip()
                producto = self.inventario.buscar(termino)

                if producto is None:
                    print("No se encontró el producto.")
                else:
                    print(producto)

            elif opcion == "3":
                codigo = input("Código del producto: ").strip()
                cantidad = input("Cantidad que desea vender: ").strip()

                try:
                    venta = self.inventario.registrar_venta(codigo, cantidad)
                    self.repositorio.guardar(self.inventario)
                    self.bitacora.registrar(
                    f"Venta de {venta.cantidad} unidades del producto {venta.codigo_producto}"
                    )
                    print(f"Venta registrada. Total: Q{venta.total:.2f}")
                except (ProductoNoEncontradoError, StockInsuficienteError, ValueError) as error:
                    print(f"No se pudo registrar la venta: {error}")
            elif opcion == "5":
                for regla in (self.alerta_stock, self.alerta_agotado):
                    productos = regla.aplicar(self.inventario)
                    print(f"\n{regla.__class__.__name__}:")
                    if productos:
                        for producto in productos:
                            print(producto)
                    else:
                        print("No hay productos que reportar.")
            elif opcion == "6":
                if not self.inventario.ventas:
                    print("No hay ventas registradas.")
                else:
                    for venta in self.inventario.ventas:
                        print(
                            f"{venta.fecha} | {venta.codigo_producto} | "
                            f"{venta.nombre_producto} | {venta.cantidad} x "
                            f"Q{venta.precio_unitario:.2f} = Q{venta.total:.2f}"
                            )
            else:
                print("Esa opción todavía no está conectada.")