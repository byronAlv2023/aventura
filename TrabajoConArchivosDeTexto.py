# Creamos un nuevo archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')

# El método write(): escribir una línea a la vez
my_notes.write("Línea 1: Hola, Soy Byron Alvarado.\n")
my_notes.write("Línea 2: Prueba método write.\n")

# El método writelines(): escribir una lista de líneas
lineas = ["Línea 3: Prueba método writelines.\n", "Línea 4: Hasta Pronto.\n"]
my_notes.writelines(lineas)

my_notes.close()

# Probamos el método 1. read()
# Abrimos el archivo my_notes.txt y lo ponemos para leer.
my_notes = open('my_notes.txt', 'r')
#Lee el contenido del archivo línea por línea utilizando el método adecuado.
print('Método 1: read()')
print('--------------------')
print(my_notes.read())
my_notes.close()

# Método 2. readlines()
my_notes = open('my_notes.txt', 'r')
print('Método 2: readlines()')
print('--------------------')
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()