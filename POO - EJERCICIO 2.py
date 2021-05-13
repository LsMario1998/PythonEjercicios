#               Ej2

"""Realizar un programa que tenga una clase Persona con las siguientes características. 
La clase tendrá como atributos el nombre y la edad de una persona.
Implementar los métodos necesarios para inicializar los atributos, 
mostrar los datos e indicar si la persona es mayor de edad o no."""

class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def printeo(self):
        print("Nombre: {} \nEdad: {} años".format(self.nombre, self.edad))
    
    def resultados(self):
        if self.edad >= 18:
            print("------------->{} es mayor de edad".format(self.nombre))
        else:
            print("------------->{} es menor de edad".format(self.nombre))

persona1 = Persona()
persona1.inicializar("Juan", 18)
persona1.printeo()
persona1.resultados()


persona3 = Persona()
persona3.inicializar("José", 16)
persona3.printeo()
persona3.resultados()