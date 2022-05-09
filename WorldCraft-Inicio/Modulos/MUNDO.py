def ASIGNAR(edad_jugador, jugador_nuevo, nivel_alcanzado):
  if (edad_jugador>=12 and edad_jugador<=20) and (jugador_nuevo==True):
    return 1
  if (edad_jugador>=12 and edad_jugador<=20) and (jugador_nuevo==False):
    return 2
  if (edad_jugador>=12 and edad_jugador<=20) and (jugador_nuevo==False) and (nivel_alcanzado>=50):
    return 3
  if (edad_jugador>20) and (jugador_nuevo==False):
    return 4
  if (edad_jugador>20) and (jugador_nuevo==False) and (nivel_alcanzado<50):
    return 5
  if (edad_jugador<20) and (nivel_alcanzado>=50):
    return 6
  
  