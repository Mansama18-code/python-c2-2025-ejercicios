""""
Facturación del Servicio de Agua Potable

El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso 
y establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. 

Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también 
pueden otorgarse descuentos adicionales.

A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.

Tarifa base:
    Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
    El costo por metro cúbico (m³) de agua es de $200/m³.
    Bonificaciones y Recargos según tipo de cliente:
Cliente Residencial: 
    Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
    Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
Cliente Comercial:
    Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
    Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
    Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
Cliente Industrial:
    Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
        consumo.
    Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.

    Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

Casos especiales:
    Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un  descuento 
    adicional del 5%.
    En todos los casos, se aplica el IVA del 21% sobre el total.

Requerimientos del programa:
    - Solicitar al usuario:
    - Cantidad de metros consumidos
    - Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.

Calcular:
    - Subtotal de consumo.
    - Bonificaciones, si corresponde
    - Recargos, si corresponde
    - Subtotal, con recargos y bonificaciones.
    - IVA aplicado (21%), si corresponde.
    - Total final a pagar.
    - Mostrar en pantalla el desglose de los cálculos.
"""

# Solicitar al usuario la cantidad de metros consumidos y el tipo de cliente
metros_consumidos = float(input("Ingrese la cantidad de metros cúbicos consumidos: "))
tipo_cliente = input("Ingrese el tipo de cliente (Residencial, Comercial, Industrial): ").strip().lower()   
# Definir constantes
CARGO_FIJO = 7000
COSTO_POR_M3 = 200
IVA = 0.21      
# Calcular el subtotal de consumo
subtotal_consumo = metros_consumidos * COSTO_POR_M3
# Inicializar bonificaciones y recargos
bonificacion = 0
recargo = 0
# Calcular bonificaciones y recargos según el tipo de cliente y el consumo
if tipo_cliente == "residencial":
    if metros_consumidos < 30:
        bonificacion = 0.10 * subtotal_consumo
    elif metros_consumidos > 80:
        recargo = 0.15 * subtotal_consumo
elif tipo_cliente == "comercial":   
    if metros_consumidos > 300:
        bonificacion = 0.12 * subtotal_consumo
    elif metros_consumidos > 150:
        bonificacion = 0.08 * subtotal_consumo
    elif metros_consumidos < 50:
        recargo = 0.05 * subtotal_consumo
elif tipo_cliente == "industrial":
    if metros_consumidos > 1000:
        bonificacion = 0.30 * subtotal_consumo
    elif metros_consumidos > 500:
        bonificacion = 0.20 * subtotal_consumo
    elif metros_consumidos < 200:
        recargo = 0.10 * subtotal_consumo
else:
    print("Tipo de cliente no válido. Por favor, ingrese Residencial, Comercial o Industrial.")
    exit()
# Calcular el subtotal con recargos y bonificaciones
subtotal = subtotal_consumo - bonificacion + recargo + CARGO_FIJO
# Aplicar caso especial para clientes residenciales
if tipo_cliente == "residencial" and subtotal < 35000:
    descuento_adicional = 0.05 * subtotal
    subtotal -= descuento_adicional
else:
    descuento_adicional = 0
# Calcular el IVA
iva_aplicado = IVA * subtotal
# Calcular el total final a pagar
total_final = subtotal + iva_aplicado
# Mostrar el desglose de los cálculos
print("\n--- Desglose de la Factura ---")
print(f"Subtotal de consumo: ${subtotal_consumo:.2f}")
print(f"Bonificación aplicada: -${bonificacion:.2f}")
print(f"Recargo aplicado: +${recargo:.2f}")
if descuento_adicional > 0:
    print(f"Descuento adicional aplicado: -${descuento_adicional:.2f}")
print(f"Cargo fijo: +${CARGO_FIJO:.2f}")
print(f"Subtotal (con recargos y bonificaciones): ${subtotal:.2f}")
print(f"IVA aplicado (21%): +${iva_aplicado:.2f}")
print(f"Total final a pagar: ${total_final:.2f}")       