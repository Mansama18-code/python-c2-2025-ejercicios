"""
2. Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
    6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
    4 y 5                ---> Aprobado, la nota es ...
    1, 2 y 3            ---> Desaprobado, la nota es ...
"""
nota = input("Ingrese la nota del alumno (1-10): ")
nota = int(nota)
if 6 <= nota and nota <= 10:
    print(f"Promoción directa, la nota es {nota}")
elif 4 <= nota and nota <= 5:            
    print(f"Aprobado, la nota es {nota}")
elif 1 <= nota and nota <= 3:            
    print(f"Desaprobado, la nota es {nota}")    