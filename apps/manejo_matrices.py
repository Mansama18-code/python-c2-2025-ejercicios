from ejercicios_matrices.funciones_matriz import crear_matriz, modificar_matriz, imprimir_matriz, sumar_matrices, multiplicar_matriz_escalar, buscar_elemento, eliminar_elemento, multiplicar_matrices, ingresar_elemento



def listado_de_estudiantes() -> None:
    """
    Función de App para manejar una lista de estudiantes y sus notas

    Args: None
    Returns: None
    """
    estudiantes = crear_matriz(3, 3, 0)
    print(f'ESTUDANTE   NOTA   COSTO')
    imprimir_matriz(estudiantes)
    
    #MODIFCAR MATRIZ
    modificar_matriz(estudiantes)
    print(f'ESTUDANTE   NOTA   COSTO')
    imprimir_matriz(estudiantes)


def otro_ejericio_matrices() -> None:
    #Forma#1
    matriz = [[1,2,3,4,5,6,7,8,9,10],
            [1,2,3,4,5,6,7,8,9,10], 
            [1,2,3,4,5,6,7,8,9,10]]
    #Forma#2
    matriz2 = crear_matriz(3, 10, 0)

    #Recorrer una matriz
    for i in range(len(matriz)): #Recorre las filas
        for j in range(len(matriz[i])): #Recorre las columnas
            if matriz[i][j] == 5: #Buscar un elemento
                print(f'AQUI ESTA EL 5')
            elif matriz[i][j] == 7: #Modificar un elemento
                elemento = 70
                matriz[i][j] = elemento
                print(f'El numero 7 fue modificado por {elemento}')
            #imprimir cada elemento
            print(f'la fila {i} y la Columna es {j}, su contenido es: {matriz[i][j]}')
        print()  

    print(matriz)
    print(matriz2)

def manejar_matrices() -> None:
    """
    Función App principal para manejar matrices

    Args: None
    Returns: None
    """
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


def el_cuadrado_magico() -> None: 

    #declaraciones
    #lista_valores = []
    valor = 0

    print(f'------------------')
    print(f'EL CUADRADO MAGICO')
    print(f'------------------')
    print(f'ingrese el valor de n')


    n = ingresar_elemento()
    total_elementos = n**2
    bandera = True
    print(n)
    #darla tamaño a la lista
    lista_valores = [0]*total_elementos #crear_matriz(0,total_elementos,0)
    print(f'MI LISTA INICIAL ES: ')
    for columna in range(len(lista_valores)):
        print(lista_valores[columna])
    print(len(lista_valores))


    #m = (n(n**2 + 1))/2 #Constante mágica
    #print(m)
    #AQUI VALIDAMOS QUE EL TAMAÑO SEA n*n
    matriz = crear_matriz(n,n,0)
    
    #Modificar la Matriz
    for fila in range(len(matriz)): 
        for columna in range(len(matriz[fila])):
            #validar que esté en 1 y total_elemento, y no se repita (USamos una lista
            # para no evitar repetir).
                #while bandera: #ASEGURAMOS INGRESAR EL VALOR VALIDADO
                    print(f'fila {fila} - columna {columna}')
                    el_elemento = ingresar_elemento()
                    
                    if el_elemento >= 1 and el_elemento <= total_elementos:
                        for i in range(len(lista_valores)):
                            print(f'lista valores')
                            if el_elemento == lista_valores[i]: #VERIFICA QUE NO ESTE REPETIDO
                                print(f'EL NUMERO ESTÁ REPETIDO, INGRESA DE NUEVO')
                                #bandera = True
                            else:  #VERIFICA ESTE DENTRO DEL RANGO
                                print(f'ALMACENA')
                                lista_valores[valor] = el_elemento
                                valor += 1
                                #ALMACENA EN MATRIZ.
                                matriz[fila][columna] = el_elemento
                                #bandera = False
                        valor = 0  
                    else: 
                        print(f'Valor fuera de rango, ingrese otro')

    

    print(matriz) 


    #modificar_matriz(matriz)


