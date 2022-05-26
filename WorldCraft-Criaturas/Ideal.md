# Identificar

Implementar un programa que permita poblar
al mundo WorldCraft ASCII.

# Determinar

Objetivo: Generar un número dado de criaturas pasivas y otro de criaturas hostiles

## Especificaciones:

### Función generar criaturas
- Debe hacerse el uso de tuplas
- Debe instanciarse a modo de función
    - Recibir como parámetros número de criaturas pasivas y hostiles
    - Validar que sean mayores a cero y no sumen más de 50 entre ambos
    - Retornar dos colas, una para las criaturas pasivas y otra para hostiles, que genere de manera aleatoria tipo de criaturas

### Función aparición de criaturas

Esta función debe generar las criaturas generadas y debe tener por cada criatura:
- Tipo
- Nombre
- Símbolo (caracter que lo representa)
- Fila donde debe aparecer (aleatoria)
- Columna donde debe aparecer (aleatoria)
- Fecha y hora en la que aparece (tomada del sistema) 
- Debe ser instanciada a modo de función
    -Recibir como parámetros la cola de la que se deba obtener una criatura
    -Retornar una estructura de datos (tupla) con la información retornada
    -La criatura debe almacenarse en una lista de todas las criaturas que se encuentran en el juego

### Función aparición jugador

Esta función debe generar al jugador y su posición con los siguientes datos:
- Tipo (jugador)
- Nombre (alias)
- Fila donde debe aparecer (aleatoria)
- Columna donde debe aparecer (aleatoria)
- Fecha y hora en la que aparece (tomada del sistema) 
- Número de corazones (10 por defecto)
- Debe ser instanciada a modo de función
    -Recibir como parámetros el alias del jugador
    -Retornar una estructura de datos (tupla) con la información retornada

### Funciones reporte juego

#### Función maquetar mundo

Recibir
- Lista de muros
- Lista de criaturas del juego
- Estructura con datos del jugador

Retornar
- Juego con muros, criaturas y jugador

### Función sesión del juego

Calcular:
- Número total de muros
- Vidas del jugador
- Número total de criaturas en el juego

Esta función debe generar al jugador y su posición con los siguientes datos:
- Tipo (jugador)
- Nombre (alias)
- Fila donde debe aparecer (aleatoria)
- Columna donde debe aparecer (aleatoria)
- Fecha y hora en la que aparece (tomada del sistema) 
- Número de corazones (10 por defecto)
- Debe ser instanciada a modo de función
    -Recibir como parámetros el alias del jugador
    -Retornar una estructura de datos (tupla) con la información retornada

# Explorar

Para crear el pseudocódigo es necesario realizar pasos lógicos, es decir ordenar la
secuencia de funciones.

Función 1: Recopilar la información del jugador
Función 2: Generar criaturas
Función 3: Maquetación del mundo, dado que las criaturas y el jugador deben tener posiciones válidas de módulos
Función 4: Maquetar criaturas en el mundo
Función 5: De la sesión del juego

Inicio
    FuncJugador(alias del jugador)
        Definir
            Fila
            Columna
            Fecha
            Vida
        Retornar diccionario jugador con: Alias,Fila,Columna,Fecha,Vida

    FuncGenCriaturas()
        Definir
            ListaCriaturasHostiles
            ListaCriaturasPasivas
            Cantidad criaturas pasivas
            Cantidad criaturas hostiles
        Validar
            CantHostiles + CantPasivas no sea mayor a 50
        Generar criaturas
            Aleatorizar crituras y meter en dos listas
                ListHostiles((criaturaX, cant),(criaturaX1, cant)...)
                LIstPasivas((criaturaX, cant),(criaturaX1, cant)...)
        Retornar(ListHostiles, ListPasivas)

    FuncMaqMundo
        Definir dimension
        Popular LlistaMundo
            For i en dimensión
                for j en dimensión
                    Añadir vacía a ListaMundo en [i][j]

        Definir muro
            For i en dimensión
                Si aleatorio
                for j en dimensión
                Si aleatorio
                Añadir muro a ListaMundo en [i][j]
            Else
                Espacio
        Retornar(ListaMuros)

    FuncMaqCriaturas(CriatHostil, CriatPasiva, PoscMundo)
        Definir
            ListPropiedadCriatura
        Si CriatHostil es igual a 0 o Null
            Nada
        Si no
            Si PoscMundo es igual a vacía

# Actuar

    Implementar el código en el proyecto

# Lograr

    Entregar el código funcional para cumplir los siguientes requerimientos:
- Generar un número dado de criaturas pasivas y otro de criaturas hostiles
- - 5 funciones
- - - Jugador OKI
- - - Generar criaturas OKI
- - - Maquetar muros OKI
- - - Maquetar criaturas y muros en mundo NOPE
- - - Entregar reporte del juego NOPE
