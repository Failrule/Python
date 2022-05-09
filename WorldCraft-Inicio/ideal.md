    # Identificar
        Implementar un progrma que verifique los datos de un aspirante
        a jugador y asignar un nivel

    # Determinar: Aquí determinamos toda la información que se nos brinda y se organiza para tener una mejor visibilidad.
        ## Sub-reto 1: Inscripción 
            Función inscripción
                Validación código CDIA
                    -Tipo: Booleano
                    -Variables de entrada:
                        Nombre: CDIA
                        Tipo: String
                    -Restricciones:
                        - Debe tener 10 caracteres
                        - No debe tener números
                        - Posición 6 debe ser @
                        - Primer y último caracter deben ser diferentes
                        - El caracter + debe existir en cualquier posición
                        - No debe existir más de 3 veces la letra K
                        - Debe contener al menos uno de estos caractéres: ?, =, &
                    -Retorno:
                        Si el CDIA no cumple con alguna de las anteriores retorna False.
                        Si el CDIA cumple con todas las anteriores continúa con la verificación de existencia de inscrito
                Verificación de existencia de inscrito
                    -Variables de entrada:
                            Nombre: CDIA
                            Tipo: String
                        -Restricciones:
                            Ninguna
                        -Retorno
                                Si CDIA retorna true imprime "CDIA validado correctamente" y continúa con las preguntas de ingreso
                                Si CDIA retorna false imprimer "CDIA ya existe"
                    -Preguntas de ingreso
                        Variables de entrada
                        -Fecha nacimiento
                            -Nombre: fecha_nacimiento
                            -Tipo: String
                            -Restricciones:
                                -Debe ser mayor a 12 años
                                -Debe ser convertida a tipo Date eliminando el símbolo /
                            -Retorno:
                                Si es mayor a 12 continúa
                                Si no es mayor, detiene el proceso
                    -Alias
                        -Nombre: alias_usuario
                        -Tipo: String
                        -Restricciones:
                            -Longitud mínima 5 caractéres
                            -No debe contener espacios
                    -Preguntas
                        -¿Ya has jugado?
                            -Nombre: jugador_nuevo
                            -Tipo: Boleano
                            -Restricciones: Ninguna
                        -¿Hasta qué nivel?
                            -Nombre: nivel_alcanzado
                            -Tipo: Entero
                            -Restricciones: 1-100
            #Sub-reto 2: Asignar mundo
                Función Asignar mundo
                    -Ingreso:
                        edad_jugador
                            Tipo: Entero
                        jugador_nuevo
                            Tipo: Boleano
                        nivel_alcanzado
                            Tipo: Entero
                    -Retorno:
                        nivel_asignado
                            Tipo: Entero
                    -Restricciones:
                        Mundo 1: edad:>=12 & <=20 & jugador_nuevo:True
                        Mundo 2: edad:>=12 & <=20 & jugador_nuevo:False
                        Mundo 3: edad:>=12 & <=20 & jugador_nuevo:False & nivel_alzanzado:>=50
                        Mundo 4: edad:>20 & jugador_nuevo:False
                        Mundo 5: edad:>20 & jugador_nuevo:False & nivel_alcanzado:<50
                        Mundo 6: edad:>20 & jugador_nuevo:False & nivel_alcanzado:>=50
    #Experimentar
        Pseudocódigo

        Inicio
            Función inscripción
            Verificar formato de CDIA
                Si cumple
                    Verficar existencia de CDIA
                Si no existe
                    Preguntar fecha de nacimiento
                Si es mayor o igual a 12 años
                    Solicitar alias
                Si es mayor a 5 carácteres y sin espacios
                    Preguntar
                        ¿Ya has jugado?
                        Si ya ha jugado
                            Preguntar
                                ¿Hasta qué nivel llegaste?
            Función asignar nivel
                Si edad es <16 y no ha jugado
                    Enviar a nivel 2
                Si ya ha jugado
                    Enviar a nivel que jugó
                Si edad es <=16 y ya ha jugado
                    Enviar al nivel que ya jugó + 2 niveles
                Si no ha jugado antes
                    Enviar a nivel 1
            Función asignar mundo
                Si tiene entre 12 y 20 años y no ha jugado
                    Enviar a Mundo 1
                Si tiene entre 12 y 20 años y ya ha jugado y su nivel es menor a 50
                    Enviar al Mundo 2
                Si tiene entre 12 y 20 años y ya ha jugado y su nivel es mayor o igual a 50
                    Enviar al Mundo 3
                Si tiene más de 20 años que no han jugado antes
                    Enviar a Mundo 4
                Si tiene más de 20 años que ya han jugado y su nivel es menor a 50
                    Enviar a Mundo 5
                Si tiene más de 20 años que ya han jugado y su nivel es mayor o igual a 50
        Fin

    #Actuar
        Se implementa el código en Repl.it
    #Lograr
        Se logra realizar el código con los parámetros indicados