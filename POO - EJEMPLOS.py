"""class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print("hi,", self.nombre, self.apellido)

class Admin(Usuario):
    def Sasaludo(self):
        print("hola, soy", self.nombre, "y soy admin")
        

usuario = Usuario('hola', 'mundo')

print(usuario.nombre, usuario.apellido)
usuario.saludo()

#                   HERENCIA
admin = Admin("Queso", "Amarillo")
admin.saludo()
admin.Sasaludo()
"""
"""class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("Soy un", self.tipo, "mi nombre es", self.nombre, "y mi sonido es el", self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print("AAAAA")
        
class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("perrrroooooo")
class Ave(Animal):
    tipo = 'pollo'

gato = Gato("algodon", "maullido")
gato.saludo()

perro = Perro("susi", "ladrido")
perro.saludo()

ave = Ave("piolin", "pio")
ave.saludo()

"""



