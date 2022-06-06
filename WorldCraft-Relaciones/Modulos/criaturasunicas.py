import csv
def quitarvaloresrepetididos(lista):
  """
  Toma una lista de cadenas, elimina las cadenas "amigo", "enemigo" y "neutro" de la lista, y
  devuelve la lista resultante
  
  :param lista: La lista de valores a procesar
  :return: una lista con los valores de la lista sin los valores repetidos.
  """
  resultadosLista=[]
  for elemento in lista:
    if elemento not in resultadosLista:
      resultadosLista.append(elemento)
  resultadosLista.remove("amigo")
  resultadosLista.remove("enemigo")
  resultadosLista.remove("neutro")
  return resultadosLista

def crearlistaunica():
  # Abriendo el archivo criaturas.csv, leyéndolo y devolviendo una lista con los valores del archivo sin
  # los valores repetidos.
   criaturas=[]
   with open('Modulos/criaturas.csv',newline='')as File:
    archivo=csv.reader(File)
    for linea in archivo:
      for elemento in linea:
        criaturas.append(elemento)
    return quitarvaloresrepetididos(criaturas)
