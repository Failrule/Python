import networkx as nx
"""
Toma un gráfico como entrada y devuelve el camino más corto entre dos nodos en el gráfico

:param rojo: el gráfico
:return: El camino más corto entre las dos criaturas.
"""
def camino(red):
  origen=input("digite la criatura origen")
  destino=input("digite la criatura destino")
  red=nx.dijkstra_path(red,source=origen,target=destino,weight=True)
  return(red)