##Mostrar los números ascendentes desde el 1 al 10
numero = 0

for numero in range(1,11):
    print(numero)


##Mostrar los números descendentes desde el 10 al 1

numero = 10
for numero in range (10, 0, -1):
    print(numero)

##Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
num_min = 0

numero = int(input("Ingrese un numero"))

for numero in range(num_min, (numero + 1), 1):
    print(numero)


##Ingresar un número y mostrar la tabla de multiplicar de ese número. 
##Por ejemplo si se ingresa el numero 5:
## 5 x 0 = 0	5 x 1  = 5	5 x 2 = 10	5 x 3  = 15 …
multiplicando = 0
numero = 0
producto = 0

numero = int(input("Ingrese el numero del que quiere saber la tabla:"))

for multiplicando in range(-1, 10):
    producto = (numero) * multiplicando

    print(f"{numero} x {multiplicando} = {producto}")

##5_Se ingresan un máximo de 10 números o hasta que el usuario ingrese 
##el número 0. Mostrar la suma y el promedio de todos los números.
numero = 0
suma = 0
promedio = 0
ingresos = 0

for i in range(10):
    numero = int(input("Ingrese un numero o 0 para finalizar:"))
    
    if numero == 0:
        break
    ingresos += 1
    suma += numero
    promedio = suma / ingresos


print(f"\tPrograma finalizado.\nLa suma de los numeros ingresados es: {suma}") 
print(f"Y el promedio es: {promedio}")
'''
##6_Imprimir los números múltiplos de 3 entre el 1 y el 10.
'''
for i in range(1, 10):
    if i % 3 == 0:
        print(i)
'''
for i in range(3, 10, 3):
    print(i)
        
'''
##7_Mostrar los números pares que hay desde la unidad hasta el número 50.

unidad = int(input("Ingrese un numero"))
for unidad in range(unidad, 50):
    if unidad % 2 == 0:
        print(unidad)


##8_Realizar un programa que permita mostrar una pirámide de números. 
##Por ejemplo: si se ingresa el numero 5, la salida del programa 
##será la siguiente:
columna = 0
numero = int(input("Ingrese un numero para iniciar la piramide:"))
for i in range(numero):
    print(f"{i}")
    for j in range(numero):
        print(j)
      

##9_Ingresar un número. 
##Mostrar todos los divisores que hay desde el 1 hasta el número ingresado.
##Mostrar la cantidad de divisores encontrados.
divisores = 0
numero = int(input("Ingrese un numero:"))
for i in range(1, numero):
    
    if numero % i == 0:
        divisores += 1
        print(f"{i} es divisor de {numero}")
print(f"Se encontraron {divisores} divisores.")

##10_Ingresar un número. Determinar si el número es primo o no.
es_primo = True
numero = int(input("Ingrese un numero:"))
for i in range(2, numero):
    
    if numero % i == 0:
        es_primo = False
        break
if es_primo == True:
    print(f"El numero {numero} es Primo")
else:
    print(f"El numero {numero} NO es Primo")


# Ejercicio 11
# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

numero_objetivo = int(input("Ingrese un numero para encontrar todos los primos entre el 1 y el numero ingresado: "))

for i in range(1, numero_objetivo + 1):
    acumulador_divisores = 0

    for j in range(1, i + 1):
        if i % j == 0:
            acumulador_divisores += 1

    if(acumulador_divisores <= 2):
        print(f"El numero {i} es un numero primo")


        