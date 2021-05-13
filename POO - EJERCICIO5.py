"""Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora."""

class Calculadora:
    def __init__(self):
        self.numero1 = int(input("Primer Valor: "))
        self.numero2 = int(input("Segundo Valor: "))

    def Suma(self):
        resSuma = self.numero1 + self.numero2
        print("resultadp suma: ", resSuma)
    def Resta(self):
        resResta = self.numero1 - self.numero2
        print("resultado resta: ", resResta)
    def Multiplicacion(self):
        resMult = self.numero1 * self.numero2
        print("resultado multiplicacion: ", resMult)
    def Division(self):
        resDiv = self.numero1/self.numero2
        print("resultado division: ", resDiv)
    
Num = Calculadora()
Num.Suma()
Num.Resta()
Num.Multiplicacion()
Num.Division()