import random

Player = input("Seleccione "  
                "Piedra, " 
                "Papel, " 
                "Tijeras: ")

OP = ["Piedra", "Papel", "Tijeras"]
x = random.choice(OP)

if x == "Piedra" and Player == "Tijeras":
    print("Pierdes")
elif x == "Piedra" and Player == "Piedra":
    print("Empatas")
if x == "Piedra" and Player == "Papel":
    print("Ganas")
######################
if x == "Papel" and Player == "Tijeras":
    print("Ganas")
elif x == "Papel" and Player == "Piedra":
    print("Pierdes")
if x == "Papel" and Player == "Papel":
    print("Empatas")
######################
if x == "Tijeras" and Player == "Tijeras":
    print("Empatas")
elif x == "Tijeras" and Player == "Piedra":
    print("Ganas")
if x == "Tijeras" and Player == "Papel":
    print("Pierdes")