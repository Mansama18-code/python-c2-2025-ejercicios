from ejercicios_ordenamiento.funciones_ordenamiento import ordenar_burbuja, ordenar_seleccion, ordenar_quick, ordenar_merge
from utiles.validaciones import ingresar_elemento
from apps.manejo_matrices import manejar_matrices, el_cuadrado_magico, el_cuadrado_magico_funcional, imprimir_matriz

def ordenar(matriz: list, tipo: int) -> list:
    """
    La función selecciona que algoritmo de ordenamiento usar para ordenar una matriz.
    Args: Variable Matriz, variable tipo
    Return: Matriz ordenada.
    """
    respuesta = True
    while respuesta == True: 

        match tipo: 
            case 1:
                ordenar_burbuja(matriz)
                respuesta = False
            case 2:
                ordenar_seleccion(matriz)
                respuesta = False
            case 3:
                ordenar_quick(matriz)
                respuesta = False
            case 4:
                ordenar_merge(matriz)
                respuesta = False
            case _: 
                print("Tipo de rango de ordenamiento no válido, vuelva a intentar")
                tipo = ingresar_elemento("Ingrese un tipo de ordenamiento válido (1-4): ")
                if tipo >=1 and tipo <=4:
                    respuesta = True

    
    return matriz


def matriz_a_ordenar() -> None:
    """
    La función en la que ingresamos el valor del algoritmo de ordenamiento a seleccionar. Crea la matriz.
    Args: -None.
    Return: -None.
    """
    tipo = ingresar_elemento("Ingrese el tipo de ordenamiento que desea realizar: \n1. Burbuja\n2. Selección\n3. Quick Sort\n4. Merge Sort\n")

    matriz = [[64, 34, 25, 12, 22, 11, 40, 45, 46],
            [104, 34, 225, 12, 212, 111, 43, 40, 90],
            [645, 34, 525, 12, 722, 181, 45, 50, 5],
            [64, 34, 25, 12, 22, 11, 78, 49, 0],
            [64, 34, 25, 12, 22, 11, 80, 49, 34],
            [64, 34, 325, 12, 222, 111, 100, 3, 4],
            [64, 634, 625, 412, 22, 11, 30, 455, 1000]]

    print("Matriz original: ")
    imprimir_matriz(matriz)
    matriz = ordenar(matriz, tipo)
    print()
    print("Matriz ordenada: ", end="")
    print()
    imprimir_matriz(matriz)

