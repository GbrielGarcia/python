from time import sleep # para ejecuciones controladas.

import pyautogui # nos permite controlar el teclado ( nos interesa para poder cerrar la pestaña del navegador con “ctrl w”).
import webbrowser # nos permite mostrar documentos por internet.

numero = input("Ingrese el numero (WhatsApp): ")
mensaje = input("Ingrese el mensaje a enviar: ")
reenviar = int(input("Repeticiones del mensaje: "))

webbrowser.open("https://web.whatsapp.com/send?phone="+numero)

sleep(10)

try: # para manejar errores
    for i in range(reenviar): # utilizamos for para la iteraciones “repeticiones del mensaje”
        pyautogui.typewrite(mensaje)
        pyautogui.press('enter')
    sleep(10)
    pyautogui.hotkey('ctrl', 'w') # nos permite cerrar la pestaña del navegador una vez envía los mensajes con una espera de 10s
    print("Mensaje enviado")
except:
    print("Error")