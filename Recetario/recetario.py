from pathlib import Path

ruta = Path.home()
print('''Bienvenido al Libro de Recetas\n''', ruta)


def leer_receta(categoria, receta):
    pass




while True:
    print('''
        --------- MENÚ -----------
        1) Leer receta
        2) Crear receta
        3) Crear Categoria
        4) Eliminar receta
        5) Eliminar categoria
        6) Salir''')
    opcion = input('\n¿Qué quieres hacer?\n-> ')

    if opcion == '6':
        break

    elif opcion == '1':
        print('''
        ------ CATEGORIAS -------
        Carnes
        Ensaladas
        Pastas
        Postres
        ''')
        categoria = input('Elige una categoria\n-> ')
        