def crear(listaCriaturas,red): 
  """
  Toma una lista de nombres y una red, y agrega los nombres a la red como nodos.
  
  :param listaCriaturas: una lista de cadenas, cada cadena es el nombre de una criatura
  :param red: el objeto gráfico networkx
  :return: Un grafo con los nodos de la listaCriaturas
  """
  for nombre in listaCriaturas:
    red.add_node(nombre)
  return red