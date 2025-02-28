"""

Funcións e variables que adoito usar.

"""

import json
import tkinter as tk


# Función para gardar nun archivo .json
def save(datos, archivo):
    with open(archivo, "w") as file:
        json.dump(datos, file)


# Función para cargar os datos dun .json e devolvelos
def load(archivo):
    try:
        with open(archivo, "r") as file:
            data = json.load(file)
        return data
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []


# Función para limpar a pantalla de widgets
def clean(ventana):
    for widget in ventana.winfo_children():
        widget.grid_forget()
        widget.pack_forget()


# Funcións para gardar e saír
# Garda e confirma saída
def exit1(ventana, datos, archivo, b_menu):
    clean(ventana)
    l_e1 = tk.Label(ventana, text="").pack()
    l_exit1 = tk.Label(ventana, text="Datos gardados exitosamente").pack()
    b_exit = tk.Button(ventana, text="Saír", command=exit2).pack()
    b_menu.pack()

    save(datos, archivo)


# Acaba co programa
def exit2(ventana):
    ventana.destroy()
