
'''

Programa que serve como almacén dunha tienda. Permite añadir, borrar, modificar e buscar un producto e tamén amosalos todos.
Cada producto ten un nome único e un prezo e cantidade asignados a el.
Repítese ata que o usuario salga do programa mediante o menú.

By Migel

'''
# Creación do diccionario

inventario = {}

# Función que serve para añadir novos productos ó inventario

def add():
    nome = input('Qué nome lle quere por ó producto?  ').capitalize()
    if nome in inventario:
        print(f'{nome} xa está no inventario.')
    else:
        cant = int(input('Cal é a cantidade dese producto?  '))
        prezo = float(input('Cal é o prezo dese producto?  '))
        if cant >= 0 and prezo >= 0:
            inventario[nome] = {'cantidade' : cant, 'prezo' : prezo}
            print(f'O producto {nome} foi añadido con éxito.')
        else:
            print('Asegúrese de que tanto o prezo como a cantidade non sexan negativos.')

# Función que permite borrar productos do inventario

def delete():
    nome = input('Qué producto desexa eliminar?  ').capitalize()
    if nome in inventario:
        del inventario[nome]
        print(f'O producto {nome} foi eliminado con éxito.')
    else:
        print(f'Non existe un producto de nome {nome}.')

# Función que permite a modificación dos datos dun producto

def mod():
    nome = input('Qué producto desexa modificar?  ').capitalize()
    if nome not in inventario:
        print(f'Non existe un producto de nome {nome}.')
    else:
        choise = int(input('Qué desexa modificar:\n1. Prezo\n2. Cantidade\n3. Ambos\n???  '))

        if choise == 1:
            new_prezo = float(input(f'Qué novo prezo lle quere por ó producto {nome}?  '))
            if new_prezo >= 0:
                inventario[nome]['prezo'] = new_prezo
                print('Os cambios gardáronse exitosamente.')
            else:
                print('O valor non pode ser negativo.')
        elif choise == 2:
            new_cant = int(input(f'Cal é a nova cantidade que lle quere por ó producto {nome}?  '))
            if new_cant >= 0:
                inventario[nome]['cantidade'] = new_cant
                print('Os cambios gardáronse exitosamente.')
            else:
                print('O valor non pode ser negativo.')
        elif choise == 3:
            new_prezo = float(input(f'Qué novo prezo lle quere por ó producto {nome}?  '))
            new_cant = int(input(f'Cal é a nova cantidade que lle quere por ó producto {nome}?  '))
            if new_cant >= 0 and new_prezo >= 0:
                inventario[nome]['cantidade'] = new_cant
                inventario[nome]['prezo'] = new_prezo
                print('Os cambios gardáronse exitosamente.')
            else:
                print('Ambos os valores non poden ser negativos.')
        else:
            print('As únicas opcións dispoñíbeis son 1 e 2.')

# Función que amosa todo o inventario

def show():
    if not inventario:
        print('O inventario está vacío.')
    else:
        print('Inventario actual:')
        for nome, datos in inventario.items():
            print(f'{nome} -> Cantidade: {datos['cantidade']}, Prezo: {datos['prezo']:.2f}')

# Función que amosa datos dun producto concreto

def search():
    nome = input('Qué producto desearía revisar?  ').capitalize()
    if nome not in inventario:
        print(f'{nome} non está no inventario.')
    else:
        datos = inventario[nome]
        print(f'{nome} -> Cantidade: {datos['cantidade']}, Prezo: {datos['prezo']:.2f}')

# Función principal

def main():
    while True:
        print('Qué quere facer:')
        print('1. Añadir un novo producto')
        print('2. Eliminar un producto')
        print('3. Modificar un producto')
        print('4. Amosar todo o inventario')
        print('5. Consultar os datos dun producto')
        print('6. Saír do programa')
        print('???')

        try:
            a = int(input())
            if a == 1:
                add()
            elif a == 2:
                delete()
            elif a == 3:
                mod()
            elif a == 4:
                show()
            elif a == 5:
                search()
            elif a == 6:
                print('Cerrando programa...')
                break
            else:
                print('Opción non válida.')
        except ValueError:
            print('Por favor, introduza un número enteiro entre 1 e 6.\n')

# Chamada á función principal

main()