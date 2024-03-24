# Diccionario
informacion_personal = {
    'Nombre':'Byron Alvarado',
    'Edad':'25 años',
    'Ciudad':'Lago Agrio_Lumbaqui',
    'Provincia':'Sucumbios',
}
print('----------------------')
print('Informacion personal sin modificar')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')
# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['Ciudad'] = 'Tena'
informacion_personal['Provincia'] = 'Napo'
# Nueva clave-valor al diccionario "profesion"
informacion_personal['Profesion'] = 'Ingenieria en Sistemas'
# Verifica si la clave "telefono" existe
if 'Telefono' not in informacion_personal:
    informacion_personal['Telefono'] = '0992261512'
# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('Edad')
print('----------------------')
print('Informacion personal Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')