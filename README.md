# Sistema de Inventario y Ventas — Tecnología Alex (Refactorización POO)

**Estudiante:** Alex  
**Curso:** Algoritmos — Universidad Mariano Gálvez de Guatemala (UMG)  
**Ciclo:** 2-2026 | **Modalidad:** Individual  

---

## 📝 Descripción del Proyecto
Este proyecto es la refactorización a **Programación Orientada a Objetos (POO)** del sistema de gestión de inventario y ventas para la empresa **Tecnología Alex**. El sistema permite administrar productos tecnológicos, registrar ventas con validación estricta de stock, consultar alertas automáticas de reabastecimiento y generar reportes históricos.

### 📌 Regla de Negocio Especial
* **Alerta de Stock Mínimo y Stock Agotado:** Implementada mediante el patrón de diseño abstracto/polimórfico (`ReglaNegocio`), notificando cuando un producto tiene 3 o menos unidades (`AlertaStockMinimo`) o cuando se ha agotado por completo (`AlertaStockAgotado`).

---

## 🚀 Instrucciones de Ejecución
Para ejecutar el proyecto no se requieren librerías externas (solo Python 3.10+):

```bash
python main.py