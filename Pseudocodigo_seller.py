print("------------- PROGRAMA --------------------")  

class Seller:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.seller = None

    def sell(self, seller):
        self.seller = seller

# instancias de vehículos y concesionarios
seller1 = Seller("Concesionario A", "Ciudad A")
seller2 = Seller("Concesionario B", "Ciudad B")

vehicle1 = Vehicle("Toyota", "Corolla", 2022, 25000)
vehicle2 = Vehicle("Honda", "Civic", 2021, 22000)

# Vender los vehículos y asignar los concesionarios
vehicle1.sell(seller1)
vehicle2.sell(seller2)

# Mostrar la información de los vehículos y los concesionarios que los vendieron
print(f"Vehicle 1 - Make: {vehicle1.make}, Model: {vehicle1.model}, Year: {vehicle1.year}, Price: {vehicle1.price}, Sold by: {vehicle1.seller.name} in {vehicle1.seller.location}")
print(f"Vehicle 2 - Make: {vehicle2.make}, Model: {vehicle2.model}, Year: {vehicle2.year}, Price: {vehicle2.price}, Sold by: {vehicle2.seller.name} in {vehicle2.seller.location}")

print("------------- PSEUDOCÓDIGO --------------------")  
Inicio

    // Creación de concesionarios
    concesionario1 = Seller("Concesionario ABC", "Calle 123")
    concesionario2 = Seller("Concesionario XYZ", "Avenida 456")

    // Creación de vehículos
    vehiculo1 = Vehicle("Toyota", "Corolla", 2020)
    vehiculo2 = Vehicle("Ford", "Fiesta", 2019)

    // Asignar concesionarios a los vehículos
    vehiculo1.asignar_seller(concesionario1)
    vehiculo2.asignar_seller(concesionario2)

    // Agregar vehículos al inventario del concesionario
    concesionario1.agregar_vehiculo(vehiculo1)
    concesionario2.agregar_vehiculo(vehiculo2)

    // Mostrar información del vehículo vendido y el concesionario
    Imprimir("Vehículo vendido: " + vehiculo1.info())
    Imprimir("Vendido por: " + concesionario1.nombre)

Fin