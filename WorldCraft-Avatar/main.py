from os import system
from Crear import CrearRostro as Crear
from VerRostros import VerRostro
from Decodificador import Decodificar
system('clear')
print("Seleccione una opción\n\t1.- Crear rostro\n\t2.- Ver rostro\n\t3.- Ver todos los rostros")



opcion=input()
if opcion.isnumeric():
    opcion=int(opcion)
    if opcion == 1:
        print("Uno")
        Crear()
    elif opcion == 2:
        rostro=VerRostro()
        Decodificar(rostro)
    elif opcion == 3:
        print("Tres")
    else:
        print("Opción no válida")
else:
    print("Debe seleccionar un número")
