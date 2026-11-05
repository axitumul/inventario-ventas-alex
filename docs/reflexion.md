# Reflexión Escrita — Refactorización a POO
**Estudiante:** Alex  
**Curso:** Algoritmos — Universidad Mariano Gálvez (UMG)  
**Proyecto:** Sistema de Inventario y Ventas (Tecnología Alex)

---

### 1. Cambios entre el Proyecto 1 y el Proyecto Final
En el Proyecto 1, el código estaba estructurado de forma procedimental (monolítica), utilizando listas de diccionarios, funciones sueltas y variables globales. Aunque era funcional, el código era difícil de escalar y mantener.

Con la refactorización a **Programación Orientada a Objetos (POO)**:
* Se encapsuló el estado y comportamiento de cada entidad en clases independientes (`Producto`, `Venta`, `Inventario`).
* Se desacopló la persistencia (lectura/escritura de CSV y Bitácora) de la lógica de negocio.
* Se reemplazaron los mensajes de error genéricos por una jerarquía de **excepciones personalizadas**.

### 2. Criterios de diseño y asignación de responsabilidades
Se aplicó el **Principio de Responsabilidad Única (SRP)** creando 7 clases principales:
1. `Producto`: Modela la entidad del producto y valida sus datos mediante propiedades (`@property`).
2. `Venta`: Representa un registro inmutable de cada transacción.
3. `Inventario`: Contenedor de productos que gestiona altas, búsquedas y ordenamiento.
4. `RepositorioCSV`: Encargado exclusivo de la persistencia de datos en disco.
5. `Bitacora`: Maneja el registro de eventos en archivo append con marca de tiempo.
6. `ReglaNegocio` (y subclases): Encapsula la lógica de alertas sobre existencias.
7. `SistemaInventario`: Coordina la interfaz de consola con los objetos del dominio.

### 3. Aplicación de Herencia y Polimorfismo
* **Herencia y Abstracción:** Se definió la clase base abstracta `ReglaNegocio` con el método abstracto `aplicar(inventario)`. Las clases `AlertaStockMinimo` y `AlertaStockAgotado` heredan de esta estructura.
* **Polimorfismo:** En la Opción 5 del menú (`app.py`), el sistema itera sobre la tupla `(self.alerta_stock, self.alerta_agotado)` y ejecuta `.aplicar(self.inventario)` sobre cada una sin verificar su tipo con `isinstance()`, ejecutando el comportamiento específico de cada alerta de forma dinámica.

### 4. Retos durante la refactorización
El mayor reto fue garantizar el **encapsulamiento estricto** en las mutaciones de stock, resuelto trasladando la lógica de validación e incremento/descuento directamente al método de la clase `Producto`.

### 5. Declaración de uso de herramientas de apoyo
Se utilizaron herramientas de IA como asistente para la estructuración inicial de plantillas de clases, resolución de dudas sintácticas de Git y generación de diagramas UML. El diseño del dominio, las pruebas y la comprensión del flujo del sistema fueron validados y ajustados manualmente.