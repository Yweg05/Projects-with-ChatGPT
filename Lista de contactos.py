
'''

Programa que funciona coma unha lista de contactos interactiva que se manten en bucle mentres o usuario queira.
Pode añadir, borrar e buscar un contacto ou amosalos todos á vez.

(Update): Agora carga e garda os contactos automaticamente

By Migel

'''

# Función para cargar a lista de contactos

def load():
    try:
        with open('contactos.json', 'r') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return {}

# Creación do diccionario da lista de contactos e import json

import json
contactos = load()

# Función que añade un novo contacto

def add(diccionario):
    contacto = input('\nQué nome lle desea por ó novo contacto?  ').strip().capitalize()
    if contacto in diccionario:
        print(f'\n{contacto} xa está na lista de contactos.')
    else:
        try:
            num = int(input('Qué número ten ese contacto?  '))
            diccionario [contacto] = num
            print(f'\nO contacto {contacto} foi añadido con éxito.')
        except ValueError:
            print('Ingrese solo números enteiros, por favor.')

# Función que borra un contacto

def delete(diccionario):
    contacto = input('\nQué contacto desea eliminar?  ').strip().capitalize()
    if contacto not in diccionario:
        print(f'\n{contacto} non está na lista de contactos.')
    else:
        del diccionario[contacto]
        print(f'\nO contacto {contacto} foi eliminado con éxito.')

# Función que amosa todolos contactos

def show():
    if not contactos:
        print('\nA lista de contactos esta baleira')
    else:
        print('\nLista de contactos:')
        for nome, num in contactos.items():
            print(f'\n{nome}: {num}')

# Función que devolve o número dun contacto elixido

def search(diccionario):
    contacto = input('\nQué contacto desea revisar?  ').strip().capitalize()
    if contacto not in diccionario:
        print(f'\n{contacto} non está na lista de contactos.')
    else:
        print(f'\nO número é {diccionario[contacto]}')

# Función que garda a lista de contactos

def save():
    with open('contactos.json', 'w') as archivo:
        json.dump(contactos, archivo)

# Función principal do programa

def main():
    while True:
        print('\nQué desexa facer?\n')
        print('1. Añadir un novo contacto')
        print('2. Eliminar un contacto')
        print('3. Amosar toda a lista de contactos')
        print('4. Buscar un contacto específico')
        print('5. Gardar e saír do programa')
        try:
            x = int(input())
            if x == 1:
                add(contactos)
            elif x == 2:
                delete(contactos)
            elif x == 3:
                show()
            elif x == 4:
                search(contactos)
            elif x == 5:
                print('Gardando contactos...\nContactos gardados.\nSaíndo do programa...')
                save()
                break
            else:
                print(f'\n{x} non é un número válido')

        except ValueError:
            print('\nIngrese un número enteiro entre 1 e 5, por favor.')

# Executación da función principal

main()