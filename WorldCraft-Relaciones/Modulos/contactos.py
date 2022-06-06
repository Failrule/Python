def crear(red): 
  """
  **Dada una red, devuelve los contactos de una criatura dada.**
  
  Ahora, escribamos una función que haga lo contrario: dada una criatura, devuelva las criaturas que tienen
  una relacion con el
  
  :param rojo: la red
  :return: La lista de contactos de la criatura
  """
  nombre=input("digite el nombre de la criatura para conocer los contactos")
  return red[nombre]
  