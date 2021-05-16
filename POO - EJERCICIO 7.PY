"""
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 

La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.

La clase PlazoFijo tendrá dos atributos propios, plazo e interés. 
Tendrá un método para obtener el importe del interés (cantidad*interés/100) 
y otro método para mostrar la información, datos del titular plazo, 
interés y total de interés.
Crear al menos un objeto de cada subclase.
"""
class Cuenta:
    def __init__(self, titular, cantidad) -> None:
        self.titular = titular
        self.cantidad = cantidad
    
    def Imprimir(self):
        print("Titular: {}\n Cantidad: {} ".format(self.titular, self.cantidad))

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
    def Imprimir(self):
        print("------Caja de ahorros------")
        super().Imprimir()

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def Plazo(self, plazo):
        self.plazo = plazo
    
    def ImporteInteres(self):
        importeinteres = (self.cantidad * self.interes/100)
        print("el importe de interes es: ", importeinteres)
    
    def Imprimir(self):
        print("------Cuenta a plazo fijo------")
        super().Imprimir()
        print("Plazo disponible: ", self.plazo)
        print("Interes: ", self.interes)
        self.ImporteInteres()



caja1 = CajaAhorro("Mario", 6000)
caja1.Imprimir()
plazo1=PlazoFijo("Mario",8000,365,1.2)
plazo1.Imprimir()

