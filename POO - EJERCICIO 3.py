"""Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar 
los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno)."""

class Triangulo:
    def inicializar(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def Imprimir(self):
        if self.a > self.b and self.a > self.c:
            print("{} es el lado con mayor tamaño".format(self.a))
        elif self.b > self.c:
            print("{} es el lado con mayor tamaño".format(self.b))
        else:
            print("{} es el lado con mayor tamaño".format(self.c))
    def tipo(self):    
        if self.a == self.b == self.c:
                print("Es un triangulo equilatero")
        elif self.a != self.b and self.a != self.c:
            print("Triangulo Escaleno")
        else:
            print("Triangulo Isosceles")    

Tri1 = Triangulo()
Tri1.inicializar(3,3,3)
Tri1.Imprimir()
Tri1.tipo()

Tri2 = Triangulo()
Tri2.inicializar(3,2,3)
Tri2.Imprimir()
Tri2.tipo()

Tri3 = Triangulo()
Tri3.inicializar(3,1,4)
Tri3.Imprimir()
Tri3.tipo()

