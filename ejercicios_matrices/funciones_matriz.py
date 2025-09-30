from utiles.validaciones import ingresar_elemento

def crear_matriz(filas: int, columnas: int, valor_inicial:any) -> list:

    matriz = []
    
    for i in range(filas):
           filas = [valor_inicial] * columnas
           matriz += [filas]
    
    return matriz

def crear_lista(filas: int, columnas: int, valor_inicial:any) -> list:

    lista = []
    
    for i in range(filas):
           filas = [valor_inicial] * columnas
           lista += filas
    
    return lista


def imprimir_matriz(matriz: list) -> None:
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}\t", end=" ")
        print()


def imprimir_lista(lista: list) -> None:
    
    for i in range(len(lista)):
            print(f"{lista[i]}\t", end=" ")
    



def modificar_matriz(matriz) -> None:
         
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = ingresar_elemento(f'Ingrese el elemento a modificar en {i} y {j}:')
    
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


