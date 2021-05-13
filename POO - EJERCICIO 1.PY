#           EJERCICIO 1
""" Realizar un programa que conste de una clase llamada Alumno que tenga 
como atributos el nombre y la nota del alumno. Definir los métodos para 
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado 
de la nota y si ha aprobado o no."""

#                       Fuente: https://byte-mind.net/curso-python-poo/

class Alumno:
    def __init__(self):
        self.datosAlumno=[]

    def iniciacion(self):
        name = input("Introduzca el nombre del alumno: ")
        nota = int(input("Ingrese la nota: "))
        self.datosAlumno.append({' NOMBRE ':name, ' NOTA ':nota})   
        
        for x in range(len(self.datosAlumno)):
            if self.datosAlumno[x][' NOTA '] >= 40:
                print({"aprobo con nota ":nota})
            else:
                print({"reprobo con nota ":nota})

datos=Alumno()
datos.iniciacion()