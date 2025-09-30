def llamar_promedio_notas(notas_estudiante: list, indice: int, promedio_notas: list) -> list:
    """ 
    Esta función retorna un arreglo el arreglo de notas de
    cada estudiante

    Arg:
         -notas_estudiante: list -> arreglo de notas del 
                            estudiante
         -indice: int -> indice del estudiante o id

    Return: arreglo de notas
    
    """
    #forma 1 de declaración VACIA: 
    #notas = list()
    #forma 2 de declaración VACIA:
    #notas = [0,2,3,4,5,6]
    suma_notas = 0
    
    #append()
    for i in range(len(notas_estudiante)):
        suma_notas += notas_estudiante[i]

    promedio = suma_notas / len(notas_estudiante)
    print(promedio)
    promedio_notas[indice] = promedio

    return promedio_notas

def agregar_nota(nombre_estudiantes: str) -> list:
    #El usuario ingresa las 5 notas del estudiante
    lista_notas = []
    #print [0,0,0,0,0]
    for i in range(5):
        #lista_notas[i] = float(input(f'Ingrese la nota {i+1} de {nombre_estudiantes}: '))nota = float(input(f'Ingrese la nota {i+1} de {nombre_estudiantes}: '))
        nota = float(input(f'Ingrese la nota {i+1} de {nombre_estudiantes}: '))
        lista_notas.append(nota)
    #print [3.5,4.0,2.5,5.0,4.5]
    return lista_notas