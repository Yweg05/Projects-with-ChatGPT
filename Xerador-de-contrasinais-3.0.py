"""

3ª versión do xerador de contraseñas, este fai o mesmo ca o anterior (engadir, eliminar, amosar todo, gardar e cargar).
Ademais tamén ten moitas melloras polo medio e interfaz gráfica.

By Migel.

"""

# Importación de json (para gardar os datos), random (para xerar os contrasinais) e de tkinter (para facer unha interfaz gráfica)
import json
import random
import tkinter as tk
from tkinter import ttk

# Lista con todos os caracteres que se van usar aleatoriamente para os contrasinais
caracteres = [
    "abcdefghilmnñopqrstuvwxz",
    "ABCDEFGHILMNÑOPQRSTUVWXZabcdefghilmnñopqrstuvwxz",
    "12345678901234567890ABCDEFGHILMNÑOPQRSTUVWXZabcdefghilmnñopqrstuvwxz",
    "._*@%¿?!-&._*@%¿?!-&12345678901234567890ABCDEFGHILMNÑOPQRSTUVWXZabcdefghilmnñopqrstuvwxz",
]

# Creación da ventana
ventana = tk.Tk()
ventana.title("Contrasinais")
ventana.geometry("500x500")


# Creación da clase contrasinal
class Contrasinal:

    # Creación da lista onde se gardan todas as instancias
    all = []

    # Creación de variables que logo serán entradas
    e_name = None
    e_length = None
    e_security = None
    e_del = None

    # Creación de variables que van ir cambiando de valor
    material = None
    length = None
    name = None
    generated_password = None

    # Creación das variables para o nome e o contrasinal
    def __init__(self, name="", contrasinal=""):
        self.name = name
        self.contrasinal = contrasinal

    # Representación do objeto, par nome-contrasinal
    def __repr__(self):
        return f"Contrasinal('{self.name}', '{self.contrasinal}')"

    # Método de clase para gardar os datos nun .json
    @classmethod
    def save(cls):
        with open("contrasinais.json", "w") as file:
            json.dump([instancia.__dict__ for instancia in cls.all], file)

    # Método de clase para cargar os datos dun .json
    @classmethod
    def load(cls):
        try:
            with open("contrasinais.json", "r") as file:
                data = json.load(file)
                cls.all = [cls(**item) for item in data]
        except json.decoder.JSONDecodeError:
            return []
        except FileNotFoundError:
            pass

    # Método estático para xerar un novo contrasinal
    @staticmethod
    def create_password(x, y):
        return "".join(random.choices(x, k=y))

    # Métodos para engadir un novo contrasinal
    # Parte 1: Recibe as especificacións do usuario
    @staticmethod
    def add1():
        clean()
        b_menu.grid(row=0, column=0, padx=25, pady=25)

        l_name = tk.Label(ventana, text="Nome: ")
        l_name.grid(row=1, column=1)
        Contrasinal.e_name = tk.Entry(ventana)
        Contrasinal.e_name.grid(row=1, column=2, columnspan=2, pady=5)

        l_length = tk.Label(ventana, text="Lonxitude: ")
        l_length.grid(row=2, column=1)
        Contrasinal.e_length = tk.Entry(ventana)
        Contrasinal.e_length.grid(row=2, column=2, columnspan=2, pady=5)

        l_security = tk.Label(ventana, text="Nivel de seguridade: ")
        l_security.grid(row=3, column=1)
        Contrasinal.e_security = ttk.Combobox(
            ventana, values=["1", "2", "3", "4"], state="readonly"
        )
        Contrasinal.e_security.grid(row=3, column=2, columnspan=2, pady=5)

        b_next = tk.Button(ventana, text="Xerar contrasinal", command=Contrasinal.add2)
        b_next.grid(row=4, column=1, pady=25)

    # Parte 2: Cos datos do anterior método xera un novo contrasinal
    @staticmethod
    def add2():
        clean()
        b_menu.grid(row=0, column=0, padx=25, pady=25)

        name = Contrasinal.e_name.get().capitalize()
        length = Contrasinal.e_length.get()
        security = Contrasinal.e_security.get()

        for x in Contrasinal.all:
            if name == x.name:
                clean()

                l_e1 = tk.Label(ventana, text="").pack()
                l_e2 = tk.Label(
                    ventana, text="Xa existe un contrasinal con ese nome"
                ).pack()
                b_menu.pack()
                break
        else:
            try:
                length = int(length)
                security = int(security) - 1

                if 0 < length < 26:
                    material = caracteres[security]
                    Contrasinal.generated_password = Contrasinal.create_password(
                        material, length
                    )
                    Contrasinal.material = material
                    Contrasinal.length = length
                    Contrasinal.name = name

                    clean()
                    b_menu.grid(row=0, column=0, padx=25, pady=25)

                    l_add0 = tk.Label(ventana, text="").grid(row=1, column=1, pady=2)
                    l_add1 = tk.Label(
                        ventana,
                        text=f"O contrasinal xerado é {Contrasinal.generated_password}",
                    )
                    l_add1.grid(row=2, column=1, columnspan=2, pady=5, padx=10)

                    b_add1 = tk.Button(
                        ventana,
                        text="Confirmar contrasinal",
                        command=Contrasinal.confirm,
                    )
                    b_add1.grid(row=3, column=1, pady=3, padx=1)
                    b_add2 = tk.Button(
                        ventana, text="Xerar unha nova", command=Contrasinal.create_loop
                    )
                    b_add2.grid(row=3, column=2, pady=3, padx=1)

                else:
                    clean()
                    l_e1 = tk.Label(ventana, text="").pack()
                    l_e2 = tk.Label(
                        ventana, text="A lonxitude debe ser maior ca 0 e máximo 25"
                    ).pack()
                    b_menu.pack()

            except ValueError:
                clean()
                l_e1 = tk.Label(ventana, text="").pack()
                l_e2 = tk.Label(
                    ventana, text="Escriba un número enteiro na lonxitude"
                ).pack()
                b_menu.pack()

    # Parte 3: Método por si o usuario quere cambiar o contrasinal coas mesmas especificacións
    @staticmethod
    def create_loop():
        Contrasinal.generated_password = Contrasinal.create_password(
            Contrasinal.material, Contrasinal.length
        )

        clean()
        b_menu.grid(row=0, column=0, padx=25, pady=25)

        l_add0 = tk.Label(ventana, text="").grid(row=1, column=1, pady=2)
        l_add1 = tk.Label(
            ventana, text=f"O contrasinal xerado é {Contrasinal.generated_password}"
        )
        l_add1.grid(row=2, column=1, columnspan=2, pady=5, padx=10)

        b_add1 = tk.Button(
            ventana, text="Confirmar contrasinal", command=Contrasinal.confirm
        )
        b_add1.grid(row=3, column=1, pady=3, padx=1)
        b_add2 = tk.Button(
            ventana, text="Xerar unha nova", command=Contrasinal.create_loop
        )
        b_add2.grid(row=3, column=2, pady=3, padx=1)

    # Parte 4: Método que se usa nas partes 2 e 3 para gardar o contrasinal
    @staticmethod
    def confirm():
        contrasinal = Contrasinal.generated_password
        Contrasinal.all.append(Contrasinal(Contrasinal.name, contrasinal))

        clean()
        l_e1 = tk.Label(ventana, text="").pack()
        l_e2 = tk.Label(ventana, text="Contrasinal gardado exitosamente").pack()
        b_menu.pack()

    # Métodos para borrar un contrasinal
    # Parte 1: Recibe o nome do contrasinal a borrar
    @staticmethod
    def delete1():
        clean()
        b_menu.grid(row=0, column=0, padx=25, pady=25)

        l_del1 = tk.Label(ventana, text="Qué contrasinal desexa eliminar?")
        l_del1.grid(row=1, column=1, padx=5, pady=3)
        Contrasinal.e_del = tk.Entry(ventana)
        Contrasinal.e_del.grid(row=2, column=1, padx=5, pady=3)
        b_del = tk.Button(ventana, text="Eliminar", command=Contrasinal.delete2)
        b_del.grid(row=3, column=1, padx=5, pady=7)

    # Parte 2: Elimina o contrasinal cos datos da parte 1
    @staticmethod
    def delete2():
        name = Contrasinal.e_del.get().capitalize()

        for index, x in enumerate(Contrasinal.all):
            if name == x.name:
                del Contrasinal.all[index]
                clean()
                l_e1 = tk.Label(ventana, text="").pack()
                l_e2 = tk.Label(
                    ventana, text="Contrasinal eliminado exitosamente"
                ).pack()
                b_menu.pack()
                break
        else:
            clean()
            l_e1 = tk.Label(ventana, text="").pack()
            l_e2 = tk.Label(
                ventana, text="Non hai ningún contrasinal con ese nome"
            ).pack()
            b_menu.pack()

    # Método estático para amosar todos os contrasinais
    @staticmethod
    def show():

        if not Contrasinal.all:
            clean()
            l_e1 = tk.Label(ventana, text="").pack()
            l_e2 = tk.Label(ventana, text="Non hai ningún contrasinal gardado").pack()
            b_menu.pack()

        else:
            clean()
            b_menu.grid(row=0, column=0, padx=25, pady=25)

            l_show1 = tk.Label(ventana, text="-----Contrasinais-----")
            l_show1.grid(row=1, column=1, padx=5, pady=15, columnspan=2)

            for x, instancia in enumerate(Contrasinal.all):
                l_show2 = tk.Label(
                    ventana, text=f"> {instancia.name}: {instancia.contrasinal}"
                )
                l_show2.grid(row=x + 2, column=1, padx=5, pady=1, columnspan=2)


# Función do menú principal
def menu():
    clean()
    b_menu.grid(row=0, column=0, padx=25, pady=25)

    l_menu = tk.Label(ventana, text="Qué quere facer?").grid(
        row=0, column=1, padx=25, pady=25
    )

    b_add = tk.Button(
        ventana, text="Engadir un novo contrasinal", command=Contrasinal.add1
    )
    b_add.grid(row=1, column=1, padx=25, pady=5)

    b_del = tk.Button(
        ventana,
        text="Eliminar un contrasinal xa existente",
        command=Contrasinal.delete1,
    )
    b_del.grid(row=2, column=1, padx=25, pady=5)

    b_show = tk.Button(
        ventana, text="Amosar todos os contrasinais", command=Contrasinal.show
    )
    b_show.grid(row=3, column=1, padx=25, pady=5)

    b_exit = tk.Button(ventana, text="Gardar e saír", command=exit1)
    b_exit.grid(row=4, column=1, padx=25, pady=5)


# Función para limpar a pantalla de widgets
def clean():
    for widget in ventana.winfo_children():
        widget.grid_forget()
        widget.pack_forget()


# Botón para volver ó menú
b_menu = tk.Button(ventana, text="Volver ó menú", command=menu)


# Funcións para gardar e saír
# Garda e confirma saída
def exit1():
    clean()
    l_e1 = tk.Label(ventana, text="").pack()
    l_exit1 = tk.Label(ventana, text="Contrasinais gardados exitosamente").pack()
    b_exit = tk.Button(ventana, text="Saír", command=exit2).pack()
    b_menu.pack()

    Contrasinal.save()


# Acaba co programa
def exit2():
    ventana.destroy()


# Función que carga, chama ó menú e ventana.mainloop()
def main():
    Contrasinal.load()
    menu()
    ventana.mainloop()


# Chamada a main()
main()
