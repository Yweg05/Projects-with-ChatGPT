
'''

Programa dun inventario dunha tienda que pode engadir, eliminar, modificar e buscar produtos.
Tamén pode amosar todo o inventario e gárdase nun archivo .csv

By Migel

'''

# Importar csv e crear a lista de productos

import csv
products=[]

# Crear a clase de Producto

class Producto:

    # Asignar as variables da instancia

    def __init__(self, name:str, price:float, quantity:int):
        self.name=name.capitalize()
        self.price=price
        self.quantity=quantity

    # Método de clase para cargar os datos dun .csv e convertilos en instancias

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open('productos.csv', newline='') as file:
                items=list(csv.DictReader(file))
            for item in items:
                produto=Producto(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )
                products.append(produto)
        except FileNotFoundError:
            pass
    
    # Método estático para gardar as instancias cos seus datos nun .csv

    @staticmethod
    def save_to_csv():
        with open('productos.csv', mode='w', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(['name', 'price', 'quantity'])
            for produto in products:
                writer.writerow([produto.name, produto.price, produto.quantity])

    # Método estático para engadir un novo produto como unha instancia nova

    @staticmethod
    def add():
        new_name=input("Qué nome lle quere por ó produto?  ").capitalize()
        for dic in products:
            if new_name == dic.name:
                print(f"O produto {new_name} xa existe")
                break
            
        else:    
            try:
                new_price=float(input("Qué prezo ten?  "))
                if new_price <= 0:
                        print("O prezo debe ser maior ca 0")
                else:
                    try:
                        new_quantity=int(input("Cal é a cantidade?  "))
                        if new_quantity < 0:
                            print("A cantidade debe ser polo menos 0")
                        else:
                            products.append(Producto(new_name, new_price, new_quantity))
                            print("O produto foi engadido exitosamente")
                    except ValueError:
                        print("Asegúrese de escribir un número enteiro")
            except ValueError:
                print("Asegúrese de escribir un número")
    
    # Método estático para borrar un produto

    @staticmethod
    def delete():
        name=input("Qué produto quere eliminar?  ").capitalize()
        for dic in products:
            if dic.name == name:
                products.remove(dic)
                print("O produto foi eliminado exitosamente")
                break
        else:
            print(f"Non se encontrou ningún produto co nome de {name}")
    
    # Método para modificar un produto

    def mod(self):
        try:
            choice=int(input("Qué quere modificar:\n1. Prezo\n2. Cantidade\n3. Ambos\n???  "))
            if choice == 1:
                try:
                    new_price=float(input("Cal é o novo prezo?  "))
                    if new_price <= 0:
                        print("O prezo debe ser maior ca 0")
                    else:
                        self.price=new_price
                        print("O prezo foi gardado exitosamente")
                except ValueError:
                    print("Asegúrese de escribir un número")

            elif choice == 2:
                try:
                    new_quantity=int(input("Cal é a nova cantidade?  "))
                    if new_quantity < 0:
                        print("A cantidade debe ser polo menos 0")
                    else:
                        self.quantity=new_quantity
                        print("O produto foi modificado exitosamente")
                except ValueError:
                    print("Asegúrese de escribir un número enteiro")

            elif choice == 3:
                try:
                    new_price=float(input("Cal é o novo prezo?  "))
                    if new_price <= 0:
                        print("O prezo debe ser maior ca 0")
                    else:
                        try:
                            new_quantity=int(input("Cal é a nova cantidade?  "))
                            if new_quantity < 0:
                                print("A cantidade debe ser polo menos 0")
                            else:
                                self.price=new_price
                                self.quantity=new_quantity
                                print("O produto foi modificado exitosamente")
                        except ValueError:
                            print("Asegúrese de escribir un número enteiro")
                except ValueError:
                    print("Asegúrese de escribir un número")
            
            else:
                print("Asegúrese de escribir un número enteiro entre 1 e 3")
        except ValueError:
            print("Introduzca un número enteiro")
    
    # Método estático para amosar todos os produtos cos seus datos

    @staticmethod
    def show():
        if not products:
            print("O inventario está baleiro")
        else:
            print("---Inventario---")
            for dic in products:
                print(f"> {dic.name} -> Prezo: {dic.price}, Cantidade: {dic.quantity}")

    # Método para buscar e amosar os datos dun produto en concreto

    def search(self):
        print(f"> {self.name} -> Prezo: {self.price}, Cantidade: {self.quantity}")

    # Función principal para pedir instruccións ó usuario e chamar ós demais métodos

def main():
    Producto.instantiate_from_csv()

    while True:
        print('''
Qué quere facer:
    1. Engadir un novo produto
    2. Eliminar un produto
    3. Modificar un produto
    4. Amosar os datos dun produto
    5. Amosar todo o inventario
    6. Gardar e saír do programa
???''')
        try:
            choice = int(input(""))

            if choice == 1:
                Producto.add()
        
            elif choice == 2:
                Producto.delete()
        
            elif choice == 3:
                name = input("Qué produto desexa modificar?  ").capitalize()
                for produto in products:
                    if produto.name == name:
                        produto.mod()
                        break
                else:
                    print(f"Non se atopou ningún produto co nome {name}")
        
            elif choice == 4:
                name=input("Qué produto desexa ver?  ").capitalize()
                for produto in products:
                    if produto.name == name:
                        produto.search()
                    break
                else:
                    print(f"Non se atopou ningún produto co nome {name}")
        
            elif choice == 5:
                Producto.show()
        
            elif choice == 6:
                Producto.save_to_csv()
                print("""
Gardando inventario...
Inventario gardado
Saíndo do programa...""")
                break
        
            else:
                print("Introduza un número enteiro entre 1 e 6")

        except ValueError:
            print("Introduzca un número enteiro")

# Chamada á función principal

main()
