# Identificar

    Crear una aplicaicón que permita construir una red de relaciones entre las criaturas del juego

# Determinar

    Información proveniente de un archivo de texto
        Tipo relación
        Criatura origen
        Lista de criaturas de contacto
            Tipos de relaciones
                Amigo
                Enemigo
                Neutro

    Ejemplo:
        - Caballo, Amigo, Aldeano, Cerdo, Ahogado
        - Aldeano Zombi, Enemigo, Aldeano, Calamar
        - Conejo, Neutro, Burro, Ajolote, Bacalao, Jinete, Slime

    Se debe realizar una función que lea un archivo con contenido
        - Como el ejemplo anterior
        - Construya la red
        - Los nodos son los nombres de las criaturas
        - Las relaciones deben llevar el tipo en sus atributos

    Se deber realizar un función que consulte contactos
        - Dado el nombre de una criatura listar los nodos con los que tiene relación

    Se debe realizar una función que encuentre el nodo más importante

    Se debe realizar una función que basado en dos criaturas calcule si hay camino entre ambos.

# Actuar

    Implementar funciones
        - Camino
            Permite crear la relación entre criatura de origen y destino
        - Centralidad
            Calcula el nodo más importante de la red
        - Contactos
            Consultar contactos: dado el nombre de una criatura listar todos los nodos con los que tiene relación
        - Diccionario Criaturas
            Permite incluír los nodos a la lista y retorna una lista con nodos
        - Ejes
            Permite añadir los ejes de las criaturas
        - Nodos
            Permite concatenar la lista de las criaturas en la red y devuelve la red
        - Función del reto
            Ejecuta los procedimientos usando las diferentes funciones para poder
            cumplir con los objetivos del reto
        - Función main
            Ejecuca Función del reto

# Lograr

    Se creó la función que lee un archivo con contenido

    Se realizó una función que consulta los contactos

    Se realizó una función que encuentra el nodo más importante

    Se debe realizó una función que basado en dos criaturas, calcula si hay camino entre ambos.
        