def ver(red):
  """
  Recorre todos los nodos de la red y realiza un seguimiento del nodo con el grado más alto.
  
  :param red: El objeto gráfico networkx
  :return: El nodo con el grado más alto.
  """
  contador=0
  for nodo in red.nodes():
    if contador==0:
      lineas=red.degree(nodo)
      Mayor=nodo
    else:
      if lineas<red.degree(nodo):
        lineas=red.degree(nodo)
        Mayor=nodo
    contador=contador+1
  return Mayor