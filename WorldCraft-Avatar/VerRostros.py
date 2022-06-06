from os import system
def VerRostro():
    print("Rostros disponibles:")
    system("ls")
    print("Escribe nombre del rostro que quieres ver")
    consulta=input()
    archivo = open(consulta, "r")
    rostro=[]
    me=[]
    for linea in archivo:
        print(linea)
        for i in linea:
            print(i)
            me.append(i)
        rostro.insert(me)       