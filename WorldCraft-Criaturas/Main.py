from Jugador import configurarJugador
from Criaturas import generarCriaturas
from Mundo import generarMundo

aliasJug="Pepito"
dimensionTablero=15
criaturasPasivas=25
criaturasHostiles=25

#Parámetros func configurarJugador
#   Ingreso
#       aliasJugador
#       dimensionTablero
#   Retorno
#       Diccionario con
#           Tipo
#           Nombre
#           Fila aparición
#           Columna aparición
#           Fecha
#           Vidas
print("Alias",configurarJugador(aliasJug, dimensionTablero))

#Parámetros func generarCriaturas
#   Ingreso
#       criaturasPasivas
#       criaturasHostiles
#   Retorno
#       listaPasivas
#       listaHostiles
print(generarCriaturas(criaturasHostiles,25))


#Parámetros func generarMundo
#   Ingreso
#       dimensionTablero
#   Retorno
#       muros en mundo
generarMundo(dimensionTablero)

