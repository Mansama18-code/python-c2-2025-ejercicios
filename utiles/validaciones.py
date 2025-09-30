def verificar_punto(cadena: str) -> str:
    """
    Función para verificar si una cadena es Texto o Número Entero, Flotante, negativo o positivo  y Booleano.
    
    Args: Recibe una cadena de texto.
    
    Returns: 'entero' si es un entero, 'flotante' si es un flotante, 'bool' si es un booleano, 'cadena' si es una cadena.
    
    """
    i = 0
    punto = 1
    bandera = True
    respuesta = 'cadena'
    while bandera == True:
            if cadena[0] == '-':

                if ord(cadena[i]) == 46 and punto == 1:
                    punto = 0
                    respuesta = 'flotante'
                    bandera = False
                elif cadena == "True" or cadena == "False":
                    respuesta = 'booleano'
                    bandera = False
                elif ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                    i += 1
                    if i == len(cadena):
                        respuesta = 'entero'
                        bandera = False
                else:
                    i +=1
            else: 

                if ord(cadena[i]) == 46 and punto == 1:
                    punto = 0
                    respuesta = 'flotante'
                    bandera = False
                elif cadena == "True" or cadena == "False":
                    respuesta = 'booleano'
                    bandera = False
                elif ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                    i += 1
                    if i == len(cadena):
                        respuesta = 'entero'
                        bandera = False
                else: 
                    respuesta = 'cadena'
                    bandera = False
        
    return respuesta


def ingresar_elemento(mensaje: str) -> any: 
    """
    Función para ingresar un elemento a la matriz
    
    Args: No recibe 
    
    Returns: El elemento ingresado parseado.
    """

    elemento = input(mensaje)

   
    #respuesta es verificar que tenga un punto.
    respuesta = verificar_punto(elemento)
    print(f'LA RESPUESTA ES: {respuesta}')

    match (respuesta):

        #INT
        case 'entero':
            elemento = int(elemento)

        #FLOAT
        case 'flotante':
            elemento = float(elemento)
            
        # BOOL
        case "True" | "False": 
            if elemento == "True":
                elemento = bool(True)
            else: 
                elemento = bool(False)
        
        case _:
            pass
            #print("El elemento se guardará como cadena de texto")
             


    return elemento