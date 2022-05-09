def validarCadena(CDIA):
  #Convertir a mayúscula
  CDIA=CDIA.upper()
  valido = True
  #Debe tener 10 caracteres
  if len(CDIA)==10:
    valido=True
  else:
    return False
  #No debe tener números
  for caracter in CDIA:
    if caracter.isdigit():
      return False
    else:
      valido=True
  #Posición 6 debe ser @
  if CDIA.find("@")==6:
    valido=True
  else:
    return False
  #Primer y último caracter deben ser diferentes
  if CDIA[0]!=CDIA[-1]:
    valido=True
  else:
    return False
  #El caracter + debe existir en cualquier posición
  if CDIA.count("+")!=0:
    valido=True
  else:
    return False
  #No debe existir más de 3 veces la letra K
  if CDIA.count("K")<=3:
    valido=True
  else:
    return False
  #Debe contener al menos uno de estos caractéres: ?, =, &
  if CDIA.count("?")!=0 or CDIA.count("=")!=0 or CDIA.count("&")!=0:
    valido=True
  else:
    return False
  return  valido
  
  
    
