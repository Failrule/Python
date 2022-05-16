# Identificar
    Objetivo según el PDF:
    "Implementar una función que recibe como entrada cuatro
    listas que corresponden a: 1) lista con número de filas x, 2) lista
    número de columnas, 3) lista con ancho del muro y 4) lista con largo
    del muro Estas listas indican la fila y la columna en la que debe
    hacerse un muro de las dimensiones dadas, es decir retornar una
    lista en Python de muros"

    Ejemplo de entrada de listas
                       a,b,c,d
    Lista columnas  = [1,3,11,12]
    Lista filas:    = [0,3,5,6]
    Lista largos    = [5,2,2,1]
    Lista anchos    = [2,9,1,4]

    4 muros: a,b,c & d
    a = Muro 1 comienza en x=0 & y=1, tiene 2 de ancho y 5 de alto
    b = Muro 2 comienza en x=3 & y=3, tiene 9 de ancho y 2 de alto
    c = Muro 3 comienza en x=5 & y=11, tiene 1 de ancho y 2 de alto
    d = Muro 4 comienza en x=6 & y=12, tiene 4 de ancho y 1 de alto

    Restricciones: El mundo debe ser 32 x 32

# Determinar
    El tamaño del tablero: 32 x 32
    
    La cantidad de muros: Esto lo determina el len() de las listas
        Lista Filas = listaFil
        Lista Columnas = listaCol
        Lista anchos = listaAnc
        Lista Largos = listaLar
    Por lo cual todas deben tener el mismo len() en el caso de este reto el len()=4

    La geometría de los muros: 
    
    Coordenadas: listaCol y listaFil determinan las coordenadas del muro en su posición "i" donde "i" = muro
    Dimensiones: listaAnc y listaLar determinan el ancho y largo del muro en su posición "i" donde "i" = muro

    Insertar coordenadas y dimensiones a la lista mundo:

    Se piensa realizar una especie de algoritmo que traiga cada uno de las posiciones de las listas (es decir cada muro y sus características), las ponga en variables y luego inserte en la lista mundo las x correspondientes, para finalmente imprimir esto en pantalla.

# Experimentar
    Inicio
        Recibir 4 parámetros en la función (listas)
        Verificar la cantidad de muros que se van a insertar
        en el mundo: listas.len()
        Crear el mundo columnas y filas
            Para cada muro (posición de las listas)
                Insertar coordenadas y dimensiones a variables
                Insertar lista mundo con las "X" correspondientes de las anteriores variables
        imprimir mundo

# Actuar
    Plasmar en código el pseudocódigo de #Experimentar para reproducir un programa funcional

# Lograr
    Entregar un algoritmo que tenga el método ideal y el código documentado que cuente con los comentarios pertinentes.