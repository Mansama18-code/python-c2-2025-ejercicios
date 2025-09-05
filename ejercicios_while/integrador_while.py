acumulador_suma_negativos = 0
acumulador_suma_positivos = 0
contador_negativos = 0
contador_positivos = 0
maximo_positivo = 0
contador_numeros = 0
respuesta_usuario = "s"

# Input del usuario
while respuesta_usuario == "s":
    numero_actual = int(input("Ingrese un numero: "))

    if numero_actual < 0:
        contador_negativos += 1
        acumulador_suma_negativos += numero_actual
    else:
        contador_positivos += 1
        acumulador_suma_positivos += numero_actual
        if numero_actual > maximo_positivo:
            maximo_positivo = numero_actual

    contador_numeros += 1

    respuesta_usuario = input("Desea ingresar otro numero? (s/n): ")
    while respuesta_usuario != "s" and respuesta_usuario != "n":
        respuesta_usuario = input("Respuesta incorrecta, responda nuevamente \nDesea ingresar otro numero? (s/n): ")


# Procesamiento de datos
if contador_positivos > 0: promedio_de_positivos = acumulador_suma_positivos / contador_positivos
if contador_negativos > 0: porcentaje_de_negativos = contador_negativos * 100 / contador_numeros

# Output programa
print("\n##################\n") # Para separar input de output
if contador_negativos > 0:
    print(f"Cantidad de numeros negativos ingresados: {contador_negativos}")
    print(f"Suma acumulada de los numeros negativos: {acumulador_suma_negativos}")
    print(f"Se ingreso un {porcentaje_de_negativos}% de numeros negativos")
else:
    print("No se ingresaron numeros negativos")

if contador_positivos > 0:
    print(f"Suma acumulada de los numeros positivos: {acumulador_suma_positivos}")
    print(f"Maximo numero positivo ingresado: {maximo_positivo}")
    print(f"Promedio de numeros positivos ingresados: {promedio_de_positivos}")
else:
    print("No se ingresaron numeros positivos")