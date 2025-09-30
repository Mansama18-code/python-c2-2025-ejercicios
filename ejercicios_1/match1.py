""""
Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del plata y Cataratas.
Si es otoño: se viaja a todos los lugares.
Si es primavera: se viaja a todos los lugares menos Bariloche.
a

"""

estacion = input("Ingrese la estación del año (invierno, verano, otoño, primavera): ")
match estacion:
    case "invierno":
        print("Se viaja a Bariloche")
    case "verano":
        print("Se viaja a Mar del plata y Cataratas")       
    case "otoño":
        print("Se viaja a todos los lugares")
    case "primavera":
        print("Se viaja a todos los lugares menos Bariloche")
    case _:
        print('Estación no válida')
        print("No se viaja")


        