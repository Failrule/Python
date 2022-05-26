from datetime import datetime
from random import randrange
from time import strftime

def configurarJugador(alias, dimensionTablero):
    jugador={"Alias":alias}
    jugador={"Tipo":"Jugador"}
    jugador["PosicionX"]=randrange(dimensionTablero)
    jugador["PosicionY"]=randrange(dimensionTablero)
    jugador["Fecha"]=datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    jugador["Vida"]=10
    return jugador