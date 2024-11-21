
'''

Xogo de adiviñanzas no cal o xogador debe de adiviñar un número entre un rango que el define e coas vidas que el elixa.
Pódese repetir tantas veces coma o creador queira.

By Migel

'''


import random
xogo = True

while xogo:
    intentos = 999999999
    intentos_infinitos = False

    a = int(input('Cantos intentos queres (<= 0 = infinitos)?  '))
    if a > 0:
            intentos = a
    else:
        intentos_infinitos = True
    def rango():
        print('Entre que dous números queres adiviñar?')
        x = int(input())
        y = int(input())
        while x >= y:
            print('O primeiro número ten que ser máis pequeno ca o segundo')
            print('Entre que dous números queres adiviñar?')
            x = int(input())
            y = int(input())
        nu = random.randint(x, y)
        return nu
    num = rango()
    while intentos > 0 or intentos_infinitos:
        n = int(input('Adiviña o número:  '))
        if n == num:
            print('Gañaches!')
            break
        elif n > num and intentos > 1:
            print('Máis pequeno')
        elif intentos > 1:
            print('Máis grande')
        intentos = intentos - 1
        intent = str(intentos)
        print('Quédanche ' + intent + ' intentos')

    if n != num:
        num = str(num)
        print('Perdeches!')
        print('O número era ' + num)

    print('Queres xogar outra vez?')
    outra = int(input('Se queres pon 1 (se non queres pon calquer outro número)  '))
    if outra != 1:
        xogo = False