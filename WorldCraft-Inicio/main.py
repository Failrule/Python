import Modulos.CDIA_UNICO as cdiaunico
import Modulos.age as edad
import Modulos.CDIA_VALIDAR as cdia_validar
import Modulos.MUNDO as mundo
from datetime import datetime


CDIA = ""
edad_jugador = 0
fecha_nacimiento = ""
edad_jugador = 0
jugador_nuevo = False
alias_usuario = ""
nivel_alcanzado = ""



def validarFormato(CDIA):
  if cdia_validar.validarCadena(CDIA):
    return True
  
CDIA="Lukkke@=g+"

#"Luisfe@=g+"
#CDIA = input("Escriba su CDIA: ")
    
#Verificar formato de CDIA
if not validarFormato(CDIA):
  print("CDIA inválido")
else:
  print("CDIA válido")
  #Si cumple: Verficar existencia de CDIA
  if cdiaunico.CDIA_UNICO(CDIA):
    print("CDIA ya existe")
    #Si no existe: Preguntar fecha de nacimiento
  else:
    print("CDIA no existe")
    #Pedir fecha de nacimiento
    #date_time_str = input("Fecha de nacimiento [dd/mm/aaaa]: ")
    
    date_time_str = '18/04/1987'
    
    #Debe ser convertida a tipo Date eliminando el símbolo /
    fecha_nacimiento = datetime.strptime(date_time_str, '%d/%m/%Y')
    edad_jugador = edad.calculateAge(fecha_nacimiento)
    print("Su edad es", edad_jugador)
    #Si es mayor o igual a 12 años: Solicitar alias
    if edad_jugador<=12:
      print("No tiene edad para jugar")
    else:
      alias_usuario = ""
      while len(alias_usuario)<=5 or alias_usuario.count(" ")!=0:
        #Pedir alias de usuario
        #alias_usuario = input("Alias:\n\t*No debe ser menor a 5 caractéres\n\t*No debe tener espacios")
        
        alias_usuario = "cuchiflí"
        
      #Si es mayor a 5 carácteres y sin espacios. Preguntar: ¿Ya has jugado?
      #jugador_nuevo = input("¿Ya has jugado?: ")

      jugador_nuevo = "s"
      
      if jugador_nuevo == "s" or jugador_nuevo == "S" or jugador_nuevo == "si" or jugador_nuevo == "SI" or jugador_nuevo == "Si" or jugador_nuevo == "sI" or jugador_nuevo == "sizas" or jugador_nuevo == "Sizas":
        jugador_nuevo = True;
        nivel_alcanzado = 0
        while not (nivel_alcanzado>=1 and nivel_alcanzado<=100):
          #Si ya ha jugado. Preguntar: ¿Hasta qué nivel llegaste?
          #nivel_alcanzado = int(input("¿Hasta qué nivel llegaste? [1-100] : "))
          
          nivel_alcanzado = 1
        

    print("Su mundo asignado es:",mundo.ASIGNAR(edad_jugador, jugador_nuevo, nivel_alcanzado)
  

  
"""
#prueba CDIA validar código unico
CDIA="Luisfe@=g+"#codigo en la lista
print(cdia_unico.CDIA_UNICO(CDIA))#True el código encontrado
CDIA="Luiofe@=g+"#codigo no en  la lista
print(cdia_unico.CDIA_UNICO(CDIA))#False código no encontrado
#prueba edad
birthDate=date(1987,4,18)
print(type(birthDate))
print(edad.calculateAge(birthDate))
"""