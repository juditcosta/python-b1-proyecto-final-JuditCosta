"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
#Write your code here
from users import *
import os

from util import *
from products import *
from orders import *

# Ruta a la carpeta data/ relativa a este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


class PrepareOrder:
    def __init__(self):
        self.cashiers = []
        self.customers = []
        self.products = []

# 1/2) Llegir CSV i convertir-ho a llista d'objectes
    def loadData(self):
        self.cashiers = self._loadCashiers()
        self.customers = self._loadCustomers()
        self.products = self._loadProducts()

    def _read(self, filename):
        manager = CSVFileManager(os.path.join(DATA_DIR, filename))
        return manager.read()

    def _loadCashiers(self):
        df = self._read("cashiers.csv")
        return CashierConverter().convert(df)

    def _loadCustomers(self):
        df = self._read("customers.csv")
        return CustomerConverter().convert(df)

    def _loadProducts(self):
        converter = ProductConverter()
        products = []
        # Cada archiu CSV s'associa amb la seva classe concret de producte
        products += converter.convert(self._read("hamburgers.csv"), Hamburger)
        products += converter.convert(self._read("sodas.csv"), Soda)
        products += converter.convert(self._read("drinks.csv"), Drink)
        products += converter.convert(self._read("happyMeal.csv"), HappyMeal)
        return products

 # 3) Buscar per DNI / id
    def findCashier(self, dni: str):
        for cashier in self.cashiers:
            if cashier.dni == str(dni):
                return cashier
        return None

    def findCustomer(self, dni: str):
        for customer in self.customers:
            if customer.dni == str(dni):
                return customer
        return None

    def findProduct(self, id: str):
        for product in self.products:
            if product.id.upper() == str(id).upper():
                return product
        return None

 # Mostrar productes disponibles
    def showProducts(self):
        print("\n----- Productes disponibles -----")
        for product in self.products:
            print(product.describe())
        print("---------------------------------\n")

    def showCashiers(self):
        print("\n----- Caixers -----")
        for cashier in self.cashiers:
            print(cashier.describe())
        print("-------------------\n")

    def showCustomers(self):
        print("\n----- Clients -----")
        for customer in self.customers:
            print(customer.describe())
        print("--------------------\n")

 # Menu interactiu
    def run(self):
        self.loadData()
        print("=== Sistema de menjar ràpid ===")

        # a) Buscar caixer per DNI
        self.showCashiers()
        cashier = None
        while cashier is None:
            dni = input("Introdueix el DNI del caixer: ").strip()
            cashier = self.findCashier(dni)
            if cashier is None:
                print("Caixer no trobat. Intenta de nou.")
        print(f"Caixer seleccionat: {cashier.name}\n")

        # b) Buscar client per DNI
        self.showCustomers()
        customer = None
        while customer is None:
            dni = input("Introdueix el DNI del client: ").strip()
            customer = self.findCustomer(dni)
            if customer is None:
                print("Client no trobat. Intenta de nou.")
        print(f"Client seleccionat: {customer.name}\n")

        # c) Inicialitzar l'ordre
        order = Order(cashier, customer)

        # d/e) Mostrar productes i escollir-los
        self.showProducts()
        print("Introdueix els ID dels productes (un per linea).")
        print("Escriu 'fin' per acabar i mostrar l'ordre.\n")
        while True:
            id = input("Id del producte (o 'fin'): ").strip()
            if id.lower() in ("fin", "end", ""):
                break
            product = self.findProduct(id)
            if product is None:
                print("Producte no trobat. Intenta de nou.")
                continue
            # f) Agregar producte a l'ordre
            order.add(product)
            print(f"Agregat: {product.name} ({product.price} euros)")

        # 4) Mostrar l'ordre
        print("\n========== ORDRE ==========")
        order.show()
        print("===========================")


if __name__ == "__main__":
    PrepareOrder().run()

