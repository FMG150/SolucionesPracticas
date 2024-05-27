
""""EJERCICO 3 - Pedir que el usuario ingrese (input) nombre de personas y 
mostrarlos hasta que el valor de lo que ingresa sea “fin” """

    
# Creamos una lista vacía para almacenar los nombres
nombres = []

# Pedimos al usuario que ingrese nombres hasta que escriba "fin"
while True:
    nombre = input("Ingresa un nombre (o escribe 'fin' para terminar): ")
    
    # Verificamos si el usuario quiere terminar
    if nombre.lower() == 'fin':
        break
    
    # Agregamos el nombre a la lista
    nombres.append(nombre)

# Mostramos los nombres ingresados
print("Los nombres ingresados son:")
for nombre in nombres:
    print(nombre)    
    