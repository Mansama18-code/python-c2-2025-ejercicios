#Para Listas pequeñas y ordenadas:
from ejercicios_matrices.funciones_matriz import imprimir_matriz, imprimir_lista, crear_matriz, crear_lista

#Para ordenar Listas
def ordenar_burbuja_list(lista: list) -> list:
    """
    La función ordena una lista.
    Args: Variable lista.
    Return: lista. ordenada.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0,n - i -1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(f'{i},{j} se intercambiaron')
                imprimir_lista(lista)

    return lista

#Para ordenar Matrices
def ordenar_burbuja(matriz: list) -> list:
    """
    La función ordena una matriz.
    Args: Variable Matriz
    Return: Matriz ordenada.
    """
    for i in range(len(matriz)):
        print(f'Ordenando fila {i+1}, lista actual:')
        imprimir_lista(matriz[i])
        print(matriz[i])
        matriz[i] = ordenar_burbuja_list(matriz[i])
        imprimir_lista(matriz[i])

    return matriz

#Para ordenar Listas
def ordenar_seleccion_lista(lista: list) -> list:
    """
    La función ordena una lista.
    Args: Variable lista
    Return: lista ordenada.
    """
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
        print(f'{i},{indice_minimo} se intercambiaron')
        imprimir_lista(lista)

    return lista


#Para ordenar Matrices
def ordenar_seleccion(matriz: list) -> list:
    """
    La función ordena una matriz.
    Args: Variable Matriz
    Return: Matriz ordenada.
    """
    for i in range(len(matriz)):
        print(f'Ordenando fila {i+1}, lista actual:')
        imprimir_lista(matriz[i])
        matriz[i] = ordenar_seleccion_lista(matriz[i])
        imprimir_lista(matriz[i])
    

    return matriz


#Para Listas Grandes y desordenadas
#Si te Preocupa la estabilidad
def particion(lista, bajo, alto):
    """
    La función Ordena la lista en base al pivote.
    Args: Variable Matriz
    Return: valor de i + 1.
    """
    pivot = lista[alto]
    i = bajo - 1

    for j in range(bajo, alto):
        if lista[j] <= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i+1], lista[alto] = lista[alto], lista[i+1]
    return i+1

#Para ordenar Listas
def ordenar_quick_lista(lista, bajo=0, alto=None) -> list:
    """
    La función ordena una lista.
    Args: Variable lista
    Return: lista ordenada.
    """
    if alto is None:
        alto = len(lista) - 1

    if bajo < alto:
        pivote= particion(lista, bajo, alto)
        ordenar_quick_lista(lista, bajo, pivote-1)
        ordenar_quick_lista(lista, pivote+1, alto)

    return lista


#Para ordenar Matrices
def ordenar_quick(matriz: list) -> list:
    """
    La función ordena una matriz.
    Args: Variable Matriz
    Return: Matriz ordenada.
    """
    for i in range(len(matriz)):
        print(f'Ordenando fila {i+1}, lista actual:')
        imprimir_lista(matriz[i])
        matriz[i] = ordenar_quick_lista(matriz[i])
        imprimir_lista(matriz[i])

    return matriz


#Si te Preocupa la memoria
#Para ordenar Listas
def ordenar_merge_lista(lista: list) -> list:
    """
        La función ordena una lista.
        Args: Variable lista
        Return: lista ordenada.
    """

    if len(lista) <= 1:
        return lista
    print(f'lenght de Lista {len(lista)}')
    if len(lista) % 2 != 0: #IMPAR
        j = 0
        mit = len(lista) // 2
        print(f'mitad es: {mit}')
        mitad_izquierda = crear_lista(1, mit, 0)
        mitad_derecha = crear_lista(1, mit+1, 0)
        print(f'Mitad Izquierda: {mitad_izquierda}, Mitad Derecha: {mitad_derecha}')
        for i in range(mit):
            mitad_izquierda[i] = lista[i]
    
        for i in range(mit):
            mitad_derecha[i] = lista[mit + i]
            j = i
                  
        print(f'j es: {j}')    
        mitad_derecha[j+1] = lista[mit +1 + j]
    else: #PAR
        mit = len(lista) // 2
        print(f'mitad es: {mit}')
        mitad_izquierda = crear_lista(1, mit, 0)
        mitad_derecha = crear_lista(1, mit, 0)
        print(f'Mitad Izquierda: {mitad_izquierda}, Mitad Derecha: {mitad_derecha}')
        for i in range(mit):
            mitad_izquierda[i] = lista[i]
    
        for i in range(mit):
            mitad_derecha[i] = lista[mit + i]
    
    
   # mitad_izquierda = lista[:mit]
   # mitad_derecha = lista[mit:]
    
    
    print(f'Mitad Izquierda: {mitad_izquierda}, Mitad Derecha: {mitad_derecha}')
    
    ordenado_izquierda = ordenar_merge_lista(mitad_izquierda)
    ordenado_derecha = ordenar_merge_lista(mitad_derecha)

    return merge(ordenado_izquierda, ordenado_derecha)

def merge(izquierda, derecha):
    """
        La función ordena lista izquierda y derecha.
        Args: Variable Izquierda y Variable Derecha
        Return: Lista ordenada.
    """
    lista = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista.append(izquierda[i])
            i += 1
        else:
            lista.append(derecha[j])
            j += 1

    lista.extend(izquierda[i:])
    lista.extend(derecha[j:])

    return lista

#Para ordenar Matrices
def ordenar_merge(matriz: list) -> list:
    """
    La función ordena una matriz.
    Args: Variable Matriz
    Return: Matriz ordenada.
    """
    for i in range(len(matriz)):
        print(f'Ordenando fila {i+1}, lista actual:')
        imprimir_lista(matriz[i])
        matriz[i] = ordenar_merge_lista(matriz[i])
        imprimir_lista(matriz[i])
    return matriz





