
'''

Modificación do xerador de contrasinais que, aparte do que fai o anterior, pode gardar os contrasinais nun diccionario.
Este diccionario gárdase ó saír do programa e cárgase nada máis entrar.

By Migel

'''
#   Función para cargar os contrasinais

def load():
    with open('contrasinais.json', 'r') as archivo:
        datos = json.load(archivo)
        return datos

#   Creación do diccionario e import random e json

import json
import random

contrasinais = load()

#   Especificacións da contrasinal

min_letras = 'abcdefghijklmnñopqrstuvwxyz'
mai_letras = 'abcdefghijklmnñopqRSTuVWxyZ'
num = '12345678901234567890'
simbolos = '>.<-_^*[]?¿()¡&%$#@'

niveis_seguridade = {
            1: min_letras,
            2: min_letras + mai_letras,
            3: min_letras + mai_letras + num,
            4: min_letras + mai_letras + num + simbolos
        }

#   Función para crear contrasinais

def add():
    nome = input('\nQué nome lle queres por ó contrasinal?  ').capitalize()
    while True:
        try:
            length = int(input('\nCantos carácteres queres que teña?  '))
            seguridade = int(input('\nQué nivel de seguridade queres que teña (1-4)?  '))

            if 0 < length < 26  and 0 < seguridade <= 4:
                nivel = niveis_seguridade[seguridade]
                contrasinal = ''.join(random.choices(nivel, k=length))
                contrasinais[nome] = contrasinal
                print(f'\n{contrasinal} será añadida coma unha nova contrasinal de nome {nome}.')
            else:
                print('\nAsegúrese de que o tamaño sexa maior que 0 e menor que 26.\nAsegúrese tamén de que o nivel de seguridade sexa un enteiro entre 1 e 4.')
                break
        except ValueError:
            print('\nIntroduza valores válidos.')
            break

        choise = input('\nQuere quedarse con ese contrasinal ou xerar unha novo (quedarso = Y)?  ').lower()
        if choise == 'y':
            print('\nContrasinal confirmado')
            break

#   Función para eliminar unha contrasinal

def delete():
    print('\nDe todolos contrasinais que tes, cal queres borrar?  ')
    for nome, contrasinal in contrasinais.items():
        print(f'->  {nome}:    {contrasinal}')

    nom = input().capitalize()
    if nom in contrasinais:
        del contrasinais[nom]
        print(f'\n{nom} foi eliminado con éxito.')
    else:
        print(f'\nNon existe ningun contrasinal de nome {nom}.')

#   Función para mostrar todos os contrasinais

def show():
    print('\nEstos son todos os contrasinais que tes gardados:\n')
    if not contrasinais:
        print('Non tes ningún contrasinal gardado.')
    else:
        for nome, contrasinal in contrasinais.items():
            print(f'->  {nome}: {contrasinal}')

#   Función para gardar os contrasinais

def save():
    with open('contrasinais.json', 'w') as archivo:
        json.dump(contrasinais, archivo)

#   Función principal

def menu():
    while True:
        print('\nBenvido ó xestor de contrasinais. Qué queres facer?')
        print('1.   Añadir un novo contrasinal')
        print('2.   Eliminar un contrasinal xa existente')
        print('3.   Amosar todos os contrasinais')
        print('4.   Gardar e saír do programa')
        try:
            choise = int(input())
            if choise == 1:
                add()
            elif choise == 2:
                delete()
            elif choise == 3:
                show()
            elif choise == 4:
                save()
                print('\nGardando contrasinais...\nContrasinais gardados.\nSaíndo do programa...')
                break
            else:
                print('\nElixa un número entre 1 e 4.')
        except ValueError:
            print('\nAsegúrese de elixir un número enteiro entre 1 e 4.')

#   Chamada á función principal

menu()