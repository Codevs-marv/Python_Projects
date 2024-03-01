archivo = open('Prueba1.txt', 'w')
# 'r' : solo lectura
# 'w' : sobreescribir en el archivo (reemplaza el contenido)
# 'a' : Cursor en la ultima linea y agrega contenido sin borrar lo que habia


# MÉTODO  write()
'''Agregar contenido al archivo y si el archivo no existe se creará uno nuevo con el contenido indicado'''
archivo.write('soy el nuevo texto')


# MÉTODO  writelines([])
'''Recibe una lista de elementos y los agrega al archivo concatenados (todos juntos en una linea)'''
archivo.writelines(['Hola', 'mundo', 'esta todo pegado'])










archivo.close()