from pathlib import Path

ruta = Path('Recetario').resolve()
print('''        \nBIENVENIDO AL LIBRO DE RECETAS\n''', ruta)

def mostrar_categorias():
    # Esta funcion se encarga de mostrar las categorías existentes dentro de la carpeta Recetario
    print('''
    ------ CATEGORIAS ------
    - Carnes
    - Ensaladas
    - Pastas
    - Postres 
    ''')

def mostrar_recetas():
    # Esta funcion se encarga de mostrar las recetas existentes dentro de la categoría escogida
    pass

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
        mostrar_categorias()
        categoria = input('Escribe la categoria:\n->')
        pass