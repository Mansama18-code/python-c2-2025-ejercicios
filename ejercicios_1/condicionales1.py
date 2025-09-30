"""
1. A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador 
en la cancha, considerando los siguientes parámetros:
    Menos de 160 cm: Base
    Entre 160 cm y 179 cm: Escolta
    Entre 180 cm y 199 cm: Alero
    200 cm o más: Ala-Pívot o Pívot
"""

altura = input("Ingrese la altura del jugador en centímetros: ")
altura = int(altura)
if altura < 160:
    print("Base")
elif altura < 180:
    print("Escolta")
elif altura < 200:
    print("Alero")
elif altura >= 200:
    print("Ala-Pívot o Pívot")