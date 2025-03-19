T = {}

while True:

    print("Menu Principal")
    print("Escribe 1 para agregrar nuevo Proyecto")
    print("Escribe 2 para modificar un Proyecto")
    print("Escribe 3 para buscar un proyecto.")
    print("Escribe 4 8para mostrar todos los proyectos ingresados.")
    print("Escribe 5 para salir del programa.")

    opcion = (int(input("Introduce el número de la opción que deseas: ")))
    print(opcion)
   

    if (int(opcion)) == 1:
        id_proyecto = (int(input("Ingresa un código para este proyecto: ")))
        nombre = input("Ingresa el nombre del proyecto: ")
        precio = input("Ingresa el precio del proyecto: ")
        cuidad = input("Ingresa la ciudad del proyecto: ")
        T[id_proyecto] = {
            "nombre": nombre,
            "precio": precio,
            "cuidad": cuidad,
        }
        print("Has guardado el proyecto correctamente.")

    elif (int(opcion)) == 2:
        id_proyecto = (int( input("Ingresa el ID del proyecto a modificar: ")))
        nombre = input("Editar el nombre del proyecto: ")
        precio = input("Editar el precio del proyecto: ")
        cuidad = input("Editar la ciudad del proyecto: ")

        T[id_proyecto] = {
            "nombre": nombre,
            "precio": precio,
            "cuidad": cuidad,
        }
        print("Has editado el proyecto correctamente.")

    elif (int(opcion)) == 3:
        id_proyecto = (int(input("Ingresa el ID del proyecto a buscar: ")))
        nombre = input("Buscar el nombre del proyecto: ")
        T[id_proyecto] = {
            "buscar nombre del proyecto": id_proyecto,
        }
        print("Has editado el proyecto correctamente.")

    elif (int(opcion)) == 4:
        print(T)

    elif (int(opcion)) == 5:
        print("Saliste del programa.")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
