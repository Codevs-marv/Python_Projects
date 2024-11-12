from pathlib import Path

ruta = Path('Recetario').resolve()
print('''        \nBIENVENIDO AL LIBRO DE RECETAS\n''', ruta)

def mostrar_menu():
    # Se encarga de mostrar las opciones del menú cada vez que se llame
    print('''
        --------- MENÚ -----------
        1) Leer receta
        2) Crear receta
        3) Crear Categoria
        4) Eliminar receta
        5) Eliminar categoria
        6) Salir''')
    opcion = input('\n¿Qué quieres hacer?\n-> ')
    return opcion

def mostrar_categorias():
    # Se encarga de mostrar las categorías existentes dentro de la carpeta Recetario
    print('''
    ------ CATEGORIAS ------
    - Carnes
    - Ensaladas
    - Pastas
    - Postres 
    ''')

def mostrar_recetas():
    # Se encarga de mostrar las recetas existentes dentro de la categoría escogida
    pass

def leer_receta(categoria, receta):
    pass




while True:
    opcion = mostrar_menu()
    
    if opcion == '6':
        break

    elif opcion == '1':
        mostrar_categorias()
        categoria = input('Escribe la categoria:\n->')

        match categoria:
            case 'carnes':
                ruta = Path('C:\\Users\\marco\\Documents\\GitHub-Repos\\Python_Projects\\Recetas\\Carnes')
                archivos = [archivo for archivo in ruta.iterdir() if archivo.is_file()]

                # mostrar las recetas dentro de la categoria Carnes
                print('\n'.join(archivo.name for archivo in archivos))
                mostrar_menu()
            
            case 'ensaladas':
                ruta = Path('C:\\Users\\marco\\Documents\\GitHub-Repos\\Python_Projects\\Recetas\\Ensaladas')
                archivos = [archivo for archivo in ruta.iterdir() if archivo.is_file()]

                # mostrar las recetas dentro de de la categoria Ensaladas
                print('\n'.join(archivo.name for archivo in archivos))
                mostrar_menu()

            case 'pastas':
                ruta = Path('C:\\Users\\marco\\Documents\\GitHub-Repos\\Python_Projects\\Recetas\\Pastas')
                archivos = [archivo for archivo in ruta.iterdir() if archivo.is_file()]

                # mostrar las recetas dentro de de la categoria Pastas
                print('\n'.join(archivo.name for archivo in archivos))
                mostrar_menu()