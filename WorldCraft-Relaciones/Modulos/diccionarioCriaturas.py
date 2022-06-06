def diccionarioCriaturas(listacriaturas):
  """
  Toma una lista de criaturas y devuelve una lista de listas, donde cada sublista contiene un número y un
  nombre de criatura
  
  :param listacriaturas: una lista de cadenas, cada cadena es un nombre de criatura
  :return: Una lista de listas, donde cada lista contiene el número de nodo y el nombre de la criatura.
  """
  diccCriatura={}
  c=0
  listaconnodos=[]
  for i in listacriaturas:
    diccCriatura[c]={'nombre':i}
    listaconnodos.append([c,i])
    c=c+1
  return listaconnodos
  