# Automatización del Ingreso de Artículos con Detección de Errores mediante OCR

Este proyecto automatiza el ingreso de artículos en una plataforma específica, resolviendo uno de los principales desafíos: detectar errores generados en la base de datos mediante reconocimiento de imagen con Tesseract OCR.

## 🚀 Herramientas Utilizadas
- **Python** - Lenguaje de programación principal.
- **OpenCV** - Procesamiento de imágenes para mejorar la precisión del OCR.
- **Tesseract OCR** - Reconocimiento óptico de caracteres (OCR) para extraer información de la interfaz de usuario.
- **PyAutoGUI** - Simulación de interacción con el teclado y el mouse.
- **Pandas** - Manipulación y análisis de datos en Excel.
- **OpenPyXL** - Lectura y escritura de archivos Excel.
- **Time** - Control de pausas y delays en la ejecución.
- **Keyboard** - Detección de teclas para funcionalidades como la pausa con la barra espaciadora.

---

## 🔍 Pasos del Desarrollo

### **1. Lectura de datos desde Excel**
El script lee un archivo Excel que contiene los artículos a ingresar y extrae las columnas necesarias.

### **2. Automatización de la entrada de datos**
Para cada artículo, el script simula la escritura y navegación en la plataforma con `PyAutoGUI`.

### **3. Detección de errores en la plataforma con OCR**
Si el código ingresado no es válido, la plataforma muestra un mensaje de error.  
Se captura la pantalla y se analiza la imagen con `Tesseract OCR` para detectar el mensaje.

### **4. Manejo de errores y corrección automática**
Si se detecta un error, el script borra el código erróneo y avanza al siguiente artículo sin afectar la cantidad ingresada.

### **5. Implementación de un sistema de pausa**
Se incorpora una funcionalidad para pausar el script con la barra espaciadora y reanudarlo con Enter.

---

