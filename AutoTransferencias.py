import pandas as pd
import pyautogui
import time
import keyboard
import pytesseract
from PIL import Image

# Ruta al ejecutable de Tesseract (modificar según la instalación)
pytesseract.pytesseract.tesseract_cmd = r'<RUTA_TESSERACT>'

# Configuración de la ruta del archivo Excel
file_path = r'<RUTA_EXCEL>'

# Leer el archivo Excel
data = pd.read_excel(file_path)

# Diferencia entre las filas (en píxeles)
fila_offset = 15

# Coordenadas de la columna VL
x_vl, y_vl, width_vl, height_vl = 1578, 214, 99, 179

# Altura de cada fila de la columna VL
altura_fila_vl = 25  

# Coordenadas del mensaje de error en la columna "Código artículo"
error_x, error_y, error_width, error_height = 1100, 300, 300, 50  

time.sleep(2)

def check_stop():
    """Verifica si el usuario presionó la barra espaciadora para detener el script."""
    if keyboard.is_pressed('space'):
        print("El script ha sido detenido por el usuario.")
        exit()

def detectar_error():
    """Captura la pantalla en la región del mensaje de error y extrae el texto con OCR."""
    screenshot_error = pyautogui.screenshot(region=(error_x, error_y, error_width, error_height))
    texto_error = pytesseract.image_to_string(screenshot_error)
    
    if "Artículo desconocido o no pedible" in texto_error:
        print("Error detectado: Artículo desconocido o no pedible.")
        return True
    return False

for index, row in data.iterrows():
    check_stop()
    
    articulo = row['Articulo']
    unidades = row['Unidades']

    codigo_articulo_x = 1245
    codigo_articulo_y = 257 + index * fila_offset

    cantidad_x = 1716
    cantidad_y = 261 + index * fila_offset

    pyautogui.click(x=codigo_articulo_x, y=codigo_articulo_y)  
    pyautogui.write(str(articulo))
    print(f"Ingresado código artículo: {articulo} en ({codigo_articulo_x}, {codigo_articulo_y})")

    time.sleep(1.5)
    check_stop()

    error_detectado = detectar_error()
    if error_detectado:
        pyautogui.click(x=codigo_articulo_x, y=codigo_articulo_y)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        print(f"Código artículo {articulo} eliminado debido a error. Continuando con la siguiente iteración.")
        time.sleep(0.5)
        continue  

    pyautogui.click(x=cantidad_x, y=cantidad_y)
    time.sleep(1)
    check_stop()

    screenshot_vl = pyautogui.screenshot(region=(x_vl, y_vl, width_vl, height_vl))
    screenshot_vl.save("columna_vl.png")

    img_vl = screenshot_vl.convert('L')
    
    custom_config = r'--oem 3 --psm 6'
    texto_extraido_vl = pytesseract.image_to_string(img_vl, config=custom_config)
    
    print("Texto extraído de la columna VL:")
    print(texto_extraido_vl)
    check_stop()

    valores_vl = [int(s) for s in texto_extraido_vl.split() if s.isdigit()]
    if valores_vl:
        max_valor_vl = max(valores_vl)
        print(f"Valor máximo encontrado en la columna VL: {max_valor_vl}")

        lineas = texto_extraido_vl.split('\n')
        for i, linea in enumerate(lineas):
            if str(max_valor_vl) in linea:
                pos_y_vl = y_vl + 10 + (i * fila_offset)  
                pos_x_vl = x_vl + 20  

                pyautogui.click(pos_x_vl, pos_y_vl)  
                time.sleep(1)  
                pyautogui.doubleClick(pos_x_vl, pos_y_vl)  
                print(f"Clic y doble clic en el valor máximo ({max_valor_vl}) en ({pos_x_vl}, {pos_y_vl})")
                check_stop()
                break
    else:
        print("No se encontraron valores numéricos en la columna VL.")

    time.sleep(1.5)
    check_stop()

    pyautogui.click(cantidad_x, cantidad_y)
    pyautogui.hotkey('ctrl', 'a')  
    pyautogui.press('backspace')  
    time.sleep(0.5)

    pyautogui.write(str(unidades))
    print(f"Ingresado cantidad: {unidades} en ({cantidad_x}, {cantidad_y})")
    check_stop()

    time.sleep(2.0)

    pyautogui.click(x=1847, y=458)  
    print(f"Fila agregada en iteración {index + 1}")
    check_stop()

    time.sleep(2.0)
