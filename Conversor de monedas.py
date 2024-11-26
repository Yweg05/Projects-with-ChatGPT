
'''

Programa que converte un valor dunha moeda a outra.

By Migel

'''
#   Importación de TKinter e de ttk

import tkinter as tk
from tkinter import ttk

#   Creación da ventana

ventana = tk.Tk()
ventana.title('Conversor de monedas')
ventana.geometry('270x200')

#   Diccionario coas tasas de cambio

tasascambio = {
    "EUR": {"USD": 1.1, "GBP": 0.85},
    "USD": {"EUR": 0.91, "GBP": 0.77},
    "GBP": {"EUR": 1.18, "USD": 1.3}
}

#   Función para facela conversión

def convertir():
    try:
        cantidade = float(entrada.get())
        moneda_orixe = moneda1.get()
        moneda_final = moneda2.get()

        if moneda_final == moneda_orixe:
            resultado.set('Elixa dúas monedas distintas')
        elif cantidade <= 0:
            resultado.set('A cantidade debe ser maior ca 0')
        else:
            tasa = tasascambio[moneda_orixe][moneda_final]
            conversion = cantidade * tasa
            resultado.set(f'{cantidade} {moneda_orixe} = {conversion} {moneda_final}')
    except ValueError:
        resultado.set('Introduza números válidos')

#   Entrada da cantidade

ttk.Label(ventana, text = 'Cantidade:').grid(row=0, column=0, pady=10, padx=10)
entrada = tk.Entry(ventana)
entrada.grid(row=0, column=1, pady=10)

#   Selección de moedas

ttk.Label(ventana, text='Dende:').grid(row=1, column=0, pady=10)
moneda1 = ttk.Combobox(ventana, values=['EUR', 'USD', 'GBP'], state='readonly')
moneda1.grid(row=1, column=1)

ttk.Label(ventana, text='A:').grid(row=2, column=0, pady=10)
moneda2 = ttk.Combobox(ventana, values=['EUR', 'USD', 'GBP'], state='readonly')
moneda2.grid(row=2, column=1)

#   Botón pra convertir

boton = ttk.Button(ventana, text='Convertir', command=convertir)
boton.grid(row=3, column=1, pady=10)

#   Resultado

resultado = tk.StringVar()
ttk.Label(ventana, textvariable=resultado).grid(row=4, column=0, columnspan=2, pady=10, padx=10)

#   Iniciar a ventá

ventana.mainloop()