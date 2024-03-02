# transferir a la variable el contenido del archivo
mi_archivo = open(r'C:\Users\marco\Documents\GitHub-Repos\Python_Projects\Manipular_Archivos\Prueba.txt')


#>> MÉTODO  read()
'''Leer y devolver el contenido completo o parcial del archivo'''
mi_archivo.read()

# Abrir el archivo en modo escritura para cambiar su contenido
with open('mi_archivo.txt', 'w') as archivo:
    archivo.write('Nuevo texto')
archivo.close()

# Abrir el archivo en modo lectura para imprimir su contenido
with open('mi_archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)


#>> MÉTODO  readline()
'''Lee una linea del archivo en cada llamada, al invocarla varias veces lee la siguiente linea del archivo
desde la posicion actual del cursor'''
# .rstrip(): Quita el salto de linea

primer_linea = mi_archivo.readline()
segunda_linea = mi_archivo.readline()
tercera_linea = mi_archivo.readline()


#>> MÉTODO  readlines():
'''Devuelve una lista donde sus elementos son cada linea del archivo'''
todas = mi_archivo.readlines()


mi_archivo.close()