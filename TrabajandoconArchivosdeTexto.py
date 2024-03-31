# Creamos un nuevo archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')

# El Método write(): escribir una línea a la vez
my_notes.write("Línea 1: Hola, soy Byron Alvarado.\n")
my_notes.write("Línea 2: Hicimos el deber en python.\n")

# El Método writelines(): escribir una lista de líneas
lineas = ["Línea 3: Probamos otro método.\n", "Línea 4: Terminamos el deber.\n"]
my_notes.writelines(lineas)

my_notes.close()

# Hacemos el Método 1. read()
# Abrimos el archivo my_notes.txt.
my_notes = open('my_notes.txt', 'r')
#Leemos el contenido del archivo línea por línea utilizando el método adecuado.
print('Método 1: read()')
print('--------------------')
print(my_notes.read())
my_notes.close()

# Hacemos el Método 2. readlines()
my_notes = open('my_notes.txt', 'r')
print('Método 2: readlines()')
print('--------------------')
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()