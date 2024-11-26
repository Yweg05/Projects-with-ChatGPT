
'''

Programa usando TKinter que sirve para sumar 1, restar 1 e resetear pero ten un apartado gráfico.

By Migel

'''

#   Importación de TKinter

import tkinter as tk

#   Creación da venta onde ocurre todo e do contador

ventana = tk.Tk()
ventana.title('Contador')
ventana.geometry('720x800')

contador = 0

#   Función para sumar 1

def incrementar():
    global contador
    contador += 1
    etiqueta.config(text = str(contador))

#   Función para restar 1

def reducir():
    global contador
    contador -= 1
    etiqueta.config(text = str(contador))

#   Función para resetear

def resetear():
     global contador
     contador = 0
     etiqueta.config(text = str(contador))

#   Creación da etiqueta que amosa o contador

etiqueta = tk.Label(ventana, text = '0' )
etiqueta.grid(row = 0, column = 0, columnspan = 3, sticky = 'EW')

#   Botóns que activan as funcións de sumar, restar e resetear respectivamente

boton1 = tk.Button(ventana, text = 'Aumentar en 1', command=incrementar, width=10)
boton1.grid(row = 1, column = 0, sticky = 'EW')

boton2 = tk.Button(ventana, text='Diminuír en 1', command=reducir, width=10)
boton2.grid(row=1, column=1, sticky = 'EW')

boton3 = tk.Button(ventana, text='Reiniciar', command=resetear, width=10)
boton3.grid(row=1, column=2, sticky='EW')

#   Idk que por aquí

ventana.mainloop()