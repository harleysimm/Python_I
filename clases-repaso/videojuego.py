#Haz un motor de videojuegos para dos personajes A y B: Funciona de la siguiente manera:
#si ataca A restará su ataqueA a defensaB, cambio de turno, le toca a B, reliaza el ataque. Así hasta que alguno sea derrotado.
import random

personajes = ["A", "B"]

ataqueA = 100
defensaA = 50
vidaA = 200

ataqueB = 100
defensaB = 50
vidaB = 200

turno = random.choice(personajes)

while vidaA > 0 and vidaB > 0:
    if turno == "A":
        daño = max(ataqueA - defensaB, 0)
        vidaB -= daño
        print(f"A ataca a B y le hace {daño} puntos de daño")
        turno = "B"
    else:
        daño = max(ataqueB - defensaA, 0)
        vidaA -= daño
        print(f"B ataca a A y le hace {daño} puntos de daño")
        turno = "A"

if vidaA <= 0:
    print("B ha ganado la partida")
else:
    print("A ha ganado la partida")
