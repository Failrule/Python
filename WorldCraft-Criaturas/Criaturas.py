from random import random, randrange

#Recibir como parámetros número de criaturas pasivas y hostiles
def generarCriaturas(cantPasivas, cantHostiles):
    #Validar que sean mayores a cero y no sumen más de 50 entre ambos
    if cantPasivas > 0 and cantHostiles > 0 and  cantPasivas + cantHostiles > 50:
        print("Número de criaturas inválido")
        return False
    else:
        CriatHostiles={"Creeper":{"Cantidad":0},"Zombie":{"Cantidad":0},"Ender":{"Cantidad":0}}
        CriatPasivas={"Cerdo":{"Cantidad":0},"Vaca":{"Cantidad":0},"Gato":{"Cantidad":0}}

        #Asignar aleatoriamente cantidades de hostiles
        CantCreeper = randrange(cantHostiles)
        CantZombie = randrange(cantHostiles-CantCreeper)
        CantEnder = randrange(cantHostiles-(CantCreeper+CantZombie))

        #Asigna aleatoriamente cantidades de pasivos
        CantCerdo = randrange(cantPasivas)
        CantVaca = randrange(cantPasivas-CantCerdo)
        CantGato = randrange(cantPasivas-(CantVaca+CantCerdo))

        #Añadir a las listas de hostiles y pasivos sus números correspondientes
        CriatHostiles["Creeper"]["Cantidad"]=CantCreeper
        CriatHostiles["Zombie"]["Cantidad"]=CantZombie
        CriatHostiles["Ender"]["Cantidad"]=CantEnder

        CriatPasivas["Cerdo"]["Cantidad"]=CantCerdo
        CriatPasivas["Vaca"]["Cantidad"]=CantVaca
        CriatPasivas["Gato"]["Cantidad"]=CantGato

        #Retornar dos colas, una para las criaturas pasivas y otra para hostiles, que genere de manera aleatoria tipo de criaturas
        return CriatPasivas, CriatHostiles