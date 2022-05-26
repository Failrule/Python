#Recibir 4 listas
from random import randrange


def generarMundo(dimensionTablero):

    listaFil={}
    listaCol={}
    listaAnc={}
    listaLar={}

    cantMuros = int(dimensionTablero/2)
    for i in range(cantMuros):
        listaFil[i]=randrange(cantMuros)
        listaCol[i]=randrange(cantMuros)
        listaAnc[i]=randrange(cantMuros)
        listaLar[i]=randrange(cantMuros)

    #Verificar la cantidad de muros que se van a insertar en el mundo
    muro = len(listaCol)

    #Crear el mundo columnas y filas
    mundoAncho=dimensionTablero
    mundoLargo=dimensionTablero

    mundo = [["⬛" for i in range(mundoAncho)] for j in range(mundoLargo)]

    #Para cada muro (posición de las listas):
    #Insertar coordenadas y dimensiones a variables
    for a in range(muro):
        Fil = listaFil[a]
        Col = listaCol[a]
        Anc = listaAnc[a]
        Lar = listaLar[a]

    #Insertar lista mundo con las "X" correspondientes
    #de las anteriores variables
        for i in range(Lar):
            for j in range(Anc):
                mundo[Fil+i][Col+j]="⬜"

    #Imprimir mundo
    for row in mundo:
            print(*row, sep='')