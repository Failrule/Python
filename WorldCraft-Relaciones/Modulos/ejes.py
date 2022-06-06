import csv

def crearejes(linea,red):
 """
  Toma una línea del archivo de entrada y una red, y agrega bordes a la red

 :param linea: una lista de cadenas, cada cadena es un nodo en el grafo
 :param red: el objeto gráfico networkx
 :return: El gráfico con los nuevos bordes agregados.
 """
 origen=linea[0]
 relacion=linea[1]
 for destino in linea[2:len(linea)]:
    red.add_edge(origen,destino,tipo=relacion)
 return red

def ejes(red):
   """
  Toma una lista de listas (el archivo csv) y un gráfico (la red) y devuelve un gráfico con los bordes
  adicional

  :param rojo: el gráfico
  :return: la red con los bordes añadidos.
   """
   with open('Modulos/criaturas.csv',newline='')as File:
     archivo=csv.reader(File)
     for linea in archivo:
       redCompleta=crearejes(linea,red)
     return redCompleta