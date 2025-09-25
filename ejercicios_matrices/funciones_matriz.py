def crear_matriz(filas: int, columnas: int, valor_inicial:any) -> list:

    matriz = []
    
    for i in range(filas):
           filas = [valor_inicial] * columnas
           matriz += [filas]
    
    return matriz



def imprimir_matriz(matriz: list) -> None:
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}     ", end=" ")
        print()



def verificar_punto(cadena: str) -> str:
    """
    Función para verificar si una cadena tiene un punto decimal.
    
    Args: Recibe una cadena de texto.
    
    Returns: 'entero' si es un entero, 'flotante' si es un flotante, 'bool' si es un booleano, 'cadena' si es una cadena.
    
    """
    i = 0
    bandera = True
    respuesta = 'cadena'
    while bandera:
        if cadena[i] == '-':
            
            pass
        else: 
            if cadena.count('.') == 1:
                respuesta = 'flotante'
                bandera = False
            elif cadena == "True" or cadena == "False":
                respuesta = 'booleano'
                bandera = False
            elif ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                #i += 1
                if i == len(cadena):
                    respuesta = 'entero'
                    bandera = False
            else: 
                respuesta = 'cadena'
                bandera = False
        i += 1
    return respuesta

def ingresar_elemento() -> any: 
    """
    Función para ingresar un elemento a la matriz
    
    Args: No recibe 
    
    Returns: El elemento ingresado parseado.
    """

    elemento = input("Ingrese el elemento a agregar: ")

    #ord()
    #respuesta es verificar que tenga un punto.
    respuesta = verificar_punto(elemento)
    #print(f'LA RESPUESTA ES: {respuesta}')

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



def modificar_matriz(matriz) -> None:
         
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = ingresar_elemento()
    
    #return matriz

def buscar_elemento(matriz, elemento) -> bool:

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == elemento:
                respuesta = True
    return respuesta

def eliminar_elemento(matriz, elemento) -> list:

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == elemento:
                matriz[i][j] = 0
    
    return matriz






#Operaciones con matrices
def sumar_matrices(matriz1, matriz2) -> list:
    
    matriz_suma = crear_matriz(len(matriz1), len(matriz1[0]), 0)

    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            matriz_suma[i][j] = matriz1[i][j] + matriz2[i][j]
    
    return matriz_suma











def multiplicar_matriz_escalar(matriz, escalar) -> list:

    matriz_resultado = crear_matriz(len(matriz), len(matriz[0]), 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_resultado[i][j] = matriz[i][j] * escalar
    
    return matriz_resultado

def multiplicar_matrices(matriz1, matriz2) -> list:

    matriz_resultado = crear_matriz(len(matriz1), len(matriz2[0]), 0)

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                matriz_resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return matriz_resultado


