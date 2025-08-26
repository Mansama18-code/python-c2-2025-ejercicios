"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e 
imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta 
mayúsculas y minúsculas."""


contrasena_guardada = "MiContrasena123"
contrasena_usuario = input("Por favor, ingrese la contraseña: ")
if contrasena_usuario.lower() == contrasena_guardada.lower():
    print("La Contraseña Ingresada es Correcta.")
else:
    print("La Contraseña Ingresada es Incorrecta.") 


"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 3.000.000,00$ 
mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario 
tiene que tributar o no."""

edad = int(input("Por favor, ingrese su edad: "))
ingresos_mensuales = float(input("Por favor, ingrese sus ingresos mensuales en $: "))
if edad > 16 and ingresos_mensuales >= 3000000:
    print("Usted debe tributar.")
else:
    print("Usted no debe tributar.")    

"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza 
aparecen a continuación:

- Ingredientes vegetarianos: Pimiento y tofu.
- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú 
con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están
 en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes 
 que lleva."""

tipo_pizza = input("¿Desea una pizza vegetariana? (sí/no): ").strip().lower()
if tipo_pizza == "sí":  
    print("Ingredientes vegetarianos disponibles: Pimiento, Tofu")
    ingrediente1 = input("Elija un ingrediente adicional: ").lower()
    print("Ingredientes vegetarianos disponibles: Pimiento, Tofu")
    ingrediente2 = input("Elija otro ingrediente adicional: ").lower()
    
    if ingrediente1 == "pimiento" and ingrediente2 == "tofu" or ingrediente1 == "tofu" and ingrediente2 == "pimiento":
        print(f"Ha elegido una pizza vegetariana con mozzarella, tomate, {ingrediente1} y {ingrediente2}.")
    else:
        print("Ingrediente no válido para pizza vegetariana.")
elif tipo_pizza == "no":
    print("Ingredientes no vegetarianos disponibles: peperoni, jamon, salmon")
    ingrediente1 = input("Elija un ingrediente adicional: ").lower()
    ingrediente2 = input("Elija el siguiente ingrediente adicional: ").lower()
    ingrediente3 = input("Elija otro ingrediente adicional: ").lower()
    if (ingrediente1 == "peperoni" and ingrediente2 == "jamon" and ingrediente3 == "salmon") or (ingrediente1 == "peperoni" and ingrediente2 == "salmon" and ingrediente3 == "jamon") or (ingrediente1 == "jamon" and ingrediente2 == "salmon" and ingrediente3 == "peperoni"):
        print(f"Ha elegido una pizza no vegetariana con mozzarella, tomate, {ingrediente1}, {ingrediente2} y {ingrediente3}.")
    else:
        print("Ingrediente no válido para pizza no vegetariana.")
else:
    print("Respuesta no válida. Por favor, responda 'sí' o 'no'.")  
