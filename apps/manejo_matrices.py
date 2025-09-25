from ejercicios_matrices.funciones_matriz import crear_matriz, modificar_matriz, imprimir_matriz, sumar_matrices, multiplicar_matriz_escalar, buscar_elemento, eliminar_elemento, multiplicar_matrices, ingresar_elemento



def listado_de_estudiantes() -> None:

    estudiantes = crear_matriz(3, 3, 0)
    print(f'ESTUDANTE   NOTA   COSTO')
    imprimir_matriz(estudiantes)
    
    #MODIFCAR MATRIZ
    modificar_matriz(estudiantes)
    print(f'ESTUDANTE   NOTA   COSTO')
    imprimir_matriz(estudiantes)

def manejar_matrices() -> None:

   # listado_de_estudiantes()
  
    #print('Ingresame un solo elemento ')
    #algo = ingresar_elemento()
    #print(f'El elemento es {algo} es del tipo de dato: {type(algo)}')
    """
    matriz =  crear_matriz(3, 3, 0)
    print('Matriz Inicial')
    imprimir_matriz(matriz)
    modificar_matriz(matriz)
    print('Matriz Modificada')
    imprimir_matriz(matriz)

    matriz2 = crear_matriz(3, 3, 5)

    matriz3 = sumar_matrices(matriz, matriz2)
    print('Matriz Total')
    imprimir_matriz(matriz3)"""