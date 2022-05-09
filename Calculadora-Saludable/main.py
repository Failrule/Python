#Algoritmo para calcular peso ideal según dr. Miller
#Versión 1
#Autor: Sebastián Salguero Carvajal
from os import system

"""
Identificar:
Se requiere crear una calculadora que calcule varios índices

Determinar:
Se debe usar métodos y poder calcular
    - Índice metabólico basal
    - Porcentaje de grasa corporal
    - Quema de calorías
    - Peso ideal

Explorar:
Usar un método para calcular cada índice y hacer un menú inicial en el método menú
para seleccionar algún cálculo

Actuar:
El código de este algoritmo.

Lograr:
Se logró aplicar un menú para elegir eficientemente los datos para calcular todos
los índices solicitados según el usuario lo requiera

"""


def menu():
    print("Bienvenido la calculadora fitness\n")
    opcion = 0
    genero=(input("Ingresar género [m]asculino o [f]emenino: "))
    altura=int((input("Ingresar altura [cm]: ")))
    peso = int(input("Ingrese su peso actual [kg]: "))
    edad=int((input("Ingresar edad [años]: ")))
    
    while(opcion!=99):
        system("clear")
        print("\nElija qué quiere calcular\n\n[1] Cuál es mi peso ideal?\n[2] Cuántas calorías quemé?\n[3] Calcular porcentaje de grasa corporal\n[4] Calcula mi índice calórico basal\n[5] Salir\n")
        opcion = int(input("Debe seleccionar un número [1]-[5]: "))
        if (opcion == 1):
            IBW(genero, altura)
        if (opcion == 2):
            CAL(peso)
        if (opcion == 3):
            PGC(genero, edad, altura, peso)
        if (opcion == 4):
            TMB(genero, edad, altura, peso)
        if (opcion == 5):
            opcion = 99
        pausa = input("\nPresione enter para continuar.")

def IBW(genero, altura):
    if (genero=='m' or genero=='M'):
        ibw = 56.2+1.41*(altura/2.54-60)
    if (genero=='f' or genero=='F'):
        ibw = 53.1+1.36*(altura/2.54-60)
    return int(ibw)

def CAL(peso):
    met = 0
    print("\n[1] Caminar\n[2] Tenis\n[3] Bicicleta\n[4] Correr\n[5] Nadar\n")
    actividad = int(input("Seleccione la actividad realizada: "))
    tiempo = int(input("Ingrese el tiempo que realizó la actividad [min]: "))
    if (actividad == 1):
        met = 2
    if (actividad == 2):
        met = 5
    if (actividad == 3):
        met = 14
    if (actividad == 4):
        met = 6
    if (actividad == 5):
        met = float(9.8)
    if (actividad < 1 or actividad > 5 ):
        print("Debe seleccionar un número")
    return int(tiempo*met*peso)/200

def PGC(genero, edad, altura, peso):
    altura=float(altura/100)
    if (genero=='m' or genero=='M'):
        pgc = 1.20 * (peso/(altura*2))+0.23*edad-16.2
    if (genero=='f' or genero=='F'):
        pgc =  1.20 * (peso/(altura*2))+0.23*edad-5.4
    print("\nUsted tiene %.2f porciento de grasa corporal" % pgc)


def TMB(genero, edad, altura, peso):
    if (genero=='m' or genero=='M'):
        tmb = (13.397*peso)+(4.799*edad)-(5.677*altura)+88.362
    if (genero=='f' or genero=='F'):
        tmb = (9.247*peso)+(3.098*edad)-(4.330*altura)+447.593
    print("\nUsted necesita %.2f calorías para sobrevivir" % tmb)

#menu()



