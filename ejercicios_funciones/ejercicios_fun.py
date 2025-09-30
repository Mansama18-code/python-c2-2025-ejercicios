# Ejercicio 1
# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def solicitar_y_retornar_numero():
    return int(input("Ingrese un numero: "))

print(solicitar_y_retornar_numero())

# Ejercicio 2
# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def solicitar_y_retornar_float():
    return float(input("Ingrese un numero flotante: "))

print(solicitar_y_retornar_float())

# Ejercicio 3
# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def solicitar_string():
    return input("Ingrese una cadena de texto: ")

print(solicitar_string())

# Ejercicio 4
# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def calcular_area_rectangulo(base, altura): 
    area = base * altura
    return area

print(calcular_area_rectangulo(2, 3))

# Ejercicio 5
# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def calcular_area_circulo(radio):
    area_circulo = 3.14 * radio ** 2
    return area_circulo

print(calcular_area_circulo(4))

# Ejercicio 6
# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def es_par(numero):
    if numero % 2 == 0: print(f"El numero {numero} es par")
    else: print(f"El numero {numero} es impar")

es_par(2)
es_par(3)

# Ejercicio 7
# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def es_par_bool(numero):
    if numero % 2 == 0: return True
    else: return False

print(es_par_bool(2))
print(es_par_bool(3))

# Ejercicio 8
# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def mayor_numero(numero_a, numero_b, numero_c):
    numero_mayor = numero_a

    if (numero_b > numero_mayor): numero_mayor = numero_b
    if (numero_c > numero_mayor): numero_mayor = numero_c

    return numero_mayor

print(mayor_numero(1, 2, 3))
print(mayor_numero(4, 1, 0))
print(mayor_numero(-1, 28, 3))

# Ejercicio 9
# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def potencia(base, exponente):
    return base ** exponente

print(potencia(2, 3))

# Ejercicio 10
# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def numero_primo(numero_objetivo):
    acumulador_divisores = 0

    for numero in range(1, numero_objetivo + 1):
        if numero_objetivo % numero == 0:
            acumulador_divisores += 1

    if(acumulador_divisores > 2):
        return False
    else:
        return True
    
print(numero_primo(3))
print(numero_primo(10))
print(numero_primo(23))
print(numero_primo(24))

# Ejercicio 11
""" 
Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), 
muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
"""

def solicitar_numero():
    return int(input("Ingrese un numero para encontrar todos los primos entre el 1 y el numero ingresado: "))

def calcular_divisores(numero_objetivo):
    acumulador_divisores = 0

    for j in range(1, numero_objetivo + 1):
        if numero_objetivo % j == 0:
            acumulador_divisores += 1
    
    return acumulador_divisores

def determinar_par(numero, divisores):
    if(divisores <= 2):
        print(f"El numero {numero} es un numero primo")
        
def numeros_primos_hasta():

    numero_objetivo = solicitar_numero()
    acumulador_divisores = 0

    for i in range(1, numero_objetivo + 1):
        acumulador_divisores = calcular_divisores(i)

        determinar_par(i, acumulador_divisores)

    return acumulador_divisores

print(f"La cantidad de divisores es: {numeros_primos_hasta()}")

# Ejercicio 12
"""
Crear una función que imprima la tabla de multiplicar 
de un número recibido como parámetro. La función debe aceptar 
parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
Por defecto es del 1 al 10.
"""

def solicitar_numero_tabla():
    return int(input("Ingrese un numero para ver su tabla de multiplicar: "))

def tabla_de_multiplicar(numero, inicio = 1, fin = 10):
    for i in range(inicio, fin + 1):
        print(f"{numero} * {i} = {numero * i}")

tabla_de_multiplicar(solicitar_numero_tabla())
tabla_de_multiplicar(solicitar_numero_tabla(), 1, 20)

# Ejercicio 13
# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

def validar_tipo_input(input):
    bandera_int = False
    contador_puntos = 0
    contador_simbolo_menos = 0

    for caracter in input:
        codigo_ascii_caracter =  ord(caracter)
        
        if codigo_ascii_caracter >= 48 and codigo_ascii_caracter <= 57:
            bandera_int = True
        elif codigo_ascii_caracter == 46:
            contador_puntos += 1
        elif codigo_ascii_caracter == 45:
            contador_simbolo_menos += 1
        else:
            return str

    if contador_simbolo_menos >= 2:
            return str

    if bandera_int == True:
        if contador_puntos == 0 and contador_simbolo_menos < 2:
            return int
        elif contador_puntos == 1 and contador_simbolo_menos < 2:
            return float
        else:
            return str
        
# Por si se quiere usar especificamente para int
def input_entero():
    tipo_input_usuario = None
    input_usuario = None

    while tipo_input_usuario != int:
        input_usuario = input("Ingrese un numero entero: ")
        tipo_input_usuario = validar_tipo_input(input_usuario)

        if tipo_input_usuario != int:
            print("Tipo incorrecto, vuelva a intentarlo.")
    return int(input_usuario)

# Por si se quiere usar especificamente para float
def input_float():
    tipo_input_usuario = None
    input_usuario = None

    while tipo_input_usuario != float:
        input_usuario = input("Ingrese un numero decimal: ")
        tipo_input_usuario = validar_tipo_input(input_usuario)

        if tipo_input_usuario != float:
            print("Tipo incorrecto, vuelva a intentarlo.")
    return float(input_usuario)

# Input de usuario generico
def casted_input():
    input_usuario = input("Ingrese algo aqui: ")

    tipo_input = validar_tipo_input(input_usuario)

    if tipo_input == int:
        return int(input_usuario)
    elif tipo_input == float:
        return float(input_usuario)
    else:
        return input_usuario
    
ingreso_usuario = casted_input()

print(ingreso_usuario)
print(type(ingreso_usuario))