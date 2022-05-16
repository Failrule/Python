#Recibir 4 listas

listaFil  = [0,3,5,6]
listaCol  = [1,3,11,12]
listaAnc  = [2,9,1,4]
listaLar  = [5,2,2,1]

#Verificar la cantidad de muros que se van a insertar en el mundo
muro = len(listaCol)

#Crear el mundo columnas y filas
mundoAncho=18
mundoLargo=8

mundo = [[" " for i in range(mundoAncho)] for j in range(mundoLargo)]

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
            mundo[Fil+i][Col+j]="x"

#Imprimir mundo
for row in mundo:
        print(row)
    