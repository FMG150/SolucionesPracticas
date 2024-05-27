"""EJERCICIO 5 - Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). Desarrolle una solución algorítmica para saber cuento debe pagar el cliente."""


# Precio de la leche por litro
precio_leche = 1000

# Cantidad de unidades compradas por el cliente
unidades_compradas = int(input("Ingrese la cantidad de unidades de leche que desea comprar: "))

# Calculamos el costo total sin descuento
costo_total = unidades_compradas * precio_leche

# Aplicamos descuento según la cantidad de unidades compradas
if 12 < unidades_compradas <= 24:
    descuento = costo_total * 0.10
elif unidades_compradas > 24:
    descuento = costo_total * 0.15
else:
    descuento = 0

# Aplicamos descuento adicional para jubilados
es_jubilado = input("¿Es jubilado? (s/n): ").lower()
if es_jubilado == 's':
    descuento += costo_total * 0.10

# Calculamos el costo total con descuento
costo_final = costo_total - descuento

# Mostramos el costo final al cliente
print(f"El costo total a pagar es: {costo_final} pesos.")