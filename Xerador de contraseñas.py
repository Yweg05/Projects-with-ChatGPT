
'''

Programa que crea unha contrasinal coas especificacións que o usuario decida. Pódese repetir.

By Migel

'''

import random

#   Creación de variables
min_letras = 'abcdefghijklmnñopqrstuvwxyz'
mai_letras = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
num = '12345678901234567890'
esp = '?¿¡!$%#.:()`+-_^*¨;,'
espec = 'caca'
a = 0
repeat = True

#   Función para pedir as especificacións da contrasinal
def pedir_especificacions():
    while True:
        x = int(input('Qué tan segura queres que sexa a túa contrasinal (1-4)?  '))
        a = int(input('Cantos carácteres queres que teña a contrasinal?  '))

        niveis_seguranza = {
            1: min_letras,
            2: min_letras + mai_letras,
            3: min_letras + mai_letras + num,
            4: min_letras + mai_letras + num + esp
        }
        if 1 <= x <= 4 and a > 0:
            espec = niveis_seguranza[x]
            break
        else:
            print('Na seguridade introduza un número entre 1 e 4')
            print('Na lonxitude introduzca un número maior ca 0')

    return espec, a

while repeat:
#   Chamada á función anterior e creación da contrasinal
    espec, a = pedir_especificacions()
    contrasinal = ''.join(random.choices(espec, k=a))

#   Entrega da contrasinal
    print(contrasinal)

#   O usuario decide se repetir o bucle ou finalizar co programa
    t = input('Queres xerar unha nova contrasinal (si = Y)?  ').lower()

    if t != 'y':
        print('Bueno vale')
        break