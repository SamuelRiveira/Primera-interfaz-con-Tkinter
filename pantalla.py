import os
import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

def comprobar(event=None):
    global puntos
    if letra_actual.get() == resultado.get():
        print("Correcto")
        puntos += 1
        print(puntos)
    else:
        print("Incorrecto")
        print(puntos)
    root.destroy()

image_folder = 'hiragana'
listaImagenes = os.listdir(image_folder)
print(listaImagenes)
image_refs = []
listaImagenesElegidas = set()

while len(listaImagenesElegidas) != 10:
    listaImagenesElegidas.add(random.choice(listaImagenes))
print(listaImagenesElegidas)

puntos = 0

def cerrarPrograma():
    print("Programa finalizado")
    sys.exit()

for imagen in listaImagenesElegidas:
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Traducir el hiragana")
    letra_actual = tk.StringVar()
    resultado = tk.StringVar()
    letra_actual.set(imagen.split(".")[0])
    image_path = os.path.join(image_folder, imagen)
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label_img = ttk.Label(root, text="Traduce el hirigana al español", padding=20)
    label_img.config(font=("Segoe UI", 20))
    label_img.pack()
    image_label = ttk.Label(root, image=photo, padding=5)
    image_label.pack()
    input = ttk.Entry(root, textvariable = resultado)
    input.pack()
    input.focus()
    print(f"{letra_actual.get()}")
    root.bind('<Return>', comprobar)
    boton_comprobar = ttk.Button(root, text = "Comprobar", command = comprobar)
    boton_comprobar.pack(pady=(10, 10))
    image_refs.append(photo)
    print(resultado)
    root.protocol("WM_DELETE_WINDOW", cerrarPrograma)
    root.mainloop()

root = tk.Tk()
root.resizable(False, False)
root.title("Resultado")

if puntos < 5:
    resultadoFinal = "Suspendido"
    imagenResultado = "suspendido.png"
elif puntos == 5:
    resultadoFinal = "Suficiente"
    imagenResultado = "suficiente.png"
elif puntos == 6:
    resultadoFinal = "bien"
    imagenResultado = "bien.png"
elif puntos == 7 or puntos == 8:
    resultadoFinal = "Notable"
    imagenResultado = "notable.png"
elif puntos == 9 or puntos == 10:
    resultadoFinal = "Sobresaliente"
    imagenResultado = "sobresaliente.png"

image_folder = "imagenes"
image_path = os.path.join(image_folder, imagenResultado)
image = Image.open(image_path).resize(size = (200, 150))
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(root, image=photo)
image_label.pack(padx=(30, 30), pady = (15, 15))
mostrarResultado = ttk.Label(root, text = resultadoFinal, padding=5)
mostrarResultado.config(font=("Segoe UI", 20))
mostrarResultado.pack()
tituloResultado = ttk.Label(root, text = f"Los puntos obtenidos: {puntos}", padding=5)
tituloResultado.pack()
root.mainloop()

