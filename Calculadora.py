'''

Calculadora moi chula que pode facer operacións básicas (sumar, restar, multiplicar e dividir),
truncar e repetirse en bucle se o usuario o solicita.

By Migel

'''

# Nombrar variables
x = True
num1 = 0
num2 = 0
op = 0
val = 0
result = 0
red = 0

# Empezar bucle
while x == True:


# Ingresar o primeiro número
    num1 = float(input("Escribe o primeiro número: "))

# Ingresar o segundo número
    num2 = float(input('Escribe o segundo número: '))

# Ingresar o signo de operación
    op = input('Queres sumar, restar, multiplicar ou dividir?: ')

# Truncar ou non truncar
    red = input('Queres truncar o resultado: ')
    if red == 'si':
        val = True
    else:
        val = False

# Suma sin truncar
    if op == 'sumar' and val == False:
        result = num1 + num2
        print('O resultado da suma ', str(num1) , ' máis ', str(num2), ' é:')
        print(result)

# Suma truncando
    if op == 'sumar' and val == True:
        result = num1 + num2
        print('O resultado da suma ', str(num1), ' máis ', str(num2), ' é:')
        print(int(result))

# Resta sin truncar
    if op == 'restar' and val == False:
        result = num1 - num2
        print('O resultado da resta ', num1, ' menos ', num2, ' é:')
        print(result)

# Resta truncando
    if op == 'restar' and val == True:
        result = num1 - num2
        print('O resultado da resta ', num1, ' menos ', num2, ' é:')
        print(int(result))

# Multiplicación sin truncar
    if op == 'multiplicar' and val == False:
        result = num1 * num2
        print('O resultado da multiplicación ', num1, ' por ', num2, ' é:')
        print(result)

# Multiplicación truncando
    if op == 'multiplicar' and val == True:
        result = num1 * num2
        print('O resultado da multiplicación ', num1, ' por ', num2, ' é:')
        print(int(result))

# División sin truncar
    if op == 'dividir' and val == False:
        result = num1 / num2
        print('O resultado da división ', num1, ' entre ', num2, ' é:')
        print(result)

# División truncando
    if op == 'dividir' and val == True:
        result = num1 / num2
        print('O resultado da división ', num1, ' entre ', num2, ' é:')
        print(int(result))

# Repetir ou non o bucle
    x = input('Queres facer outra operación? ')
    if x == 'si':
        x = True
    else:
        print('Bueno vale, chau!')