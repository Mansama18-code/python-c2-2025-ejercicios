from ejercicios_arrays.listas.creacion_listas import llamar_arreglo_estudiantes, declarar_arreglo_promedio_notas

from ejercicios_arrays.arrays import llamar_promedio_notas, agregar_nota

#Almacenar en una variable el retorno de la función #llamar_arreglo_estudiantes que contiene el arreglo de #estudiantes.


def promedio_estudiantes() -> None:
    """ 
    Esta función no retorna ningún valor, solo imprime
    el promedio de notas de cada estudiante

    Arg:
         -ninguno

    Return: None
    
    """
    nombre_estudiantes = llamar_arreglo_estudiantes()
    promedio_notas = declarar_arreglo_promedio_notas()
    print(f'Promedio inicial: {promedio_notas}, {id(promedio_notas)}')
    for i in range(len(nombre_estudiantes)):
        print(f'El nombre del estudiante es: {nombre_estudiantes[i]}')

        lista_notas = agregar_nota(nombre_estudiantes[i])
        promedio_notas = llamar_promedio_notas(lista_notas, i, promedio_notas)
        print(f'En Memoria es: {id(promedio_notas)}')
        print(f'Las notas del estudiante {nombre_estudiantes[i]} son:')
        for j in range(len(lista_notas)):
            print(f'La nota {j+1} es: {lista_notas[j]}')
        
        print(f'y el promedio de notas es: {promedio_notas[i]}')
        print(f'La lista de notas general es: {promedio_notas}')
        


        
