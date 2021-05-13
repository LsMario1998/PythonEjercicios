if __name__ == '__main__':
    
    Curso = []
    Notas = set()
    ListFinal = []

    Alu = int(input("Cantidad de Alumnos: "))
    
    for i in range(Alu):
        names = input("Names: ")
        Scores = float(input("Scores: "))
    
        Curso.append([names,Scores]) #LISTA DE LISTAS
        Notas.add(Scores) #GUARDA LAS NOTAS EN LA LISTA

        Orden = sorted(Notas) #ORDENA DE MENOR A MAYOR
    
    Orden.remove(min(Orden)) #SE ELIMINA LA NOTA MAS BAJA
    
    for names, Scores in Curso:
        if Scores == Orden[0]:
            ListFinal.append(names)
    
    Alphab = sorted(ListFinal)

    for names in Alphab:
        print(names)