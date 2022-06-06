import networkx as nx
import matplotlib.pyplot as plt
import Modulos.criaturasunicas as lista
import Modulos.nodos as nodos
import Modulos.ejes as ejes
import Modulos.contactos as contactos
import Modulos.centralidad as centralidad
import Modulos.camino as ver 

#Crear un gráfico vacío.
red=nx.Graph()
def main():  
  listaCriaturas=lista.crearlistaunica()
  RedConNodos=nodos.crear(listaCriaturas,red)
  RedCompleta=ejes.ejes(RedConNodos)
  print("contactos ",contactos.crear(RedCompleta))
  print("el nodo central es ",centralidad.ver(RedCompleta))
  print("el camino es ",ver.camino(RedCompleta))
  nx.draw(RedCompleta,with_labels=True)
  plt.show()
  
  
  
