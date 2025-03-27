""""
Registro de Constructoras

Desarrolla un programa que permita registrar constructoras. Para cada constructora, se
deben solicitar los siguientes datos por teclado: 
Nombre de la constructora
Cantidad de proyectos vigentes (debe ser un número entero mayor o igual a 0)
Cantidad de ventas por cada proyecto vigente (debe ser un número entero mayor o igual a 0)
El programa debe cumplir con los siguientes requisitos:

1. Validación de datos: No se deben aceptar valores vacíos ni datos inválidos (por
ejemplo, valores negativos o caracteres en campos numéricos).

2. Uso de arreglos: Los datos de las constructoras y sus proyectos deben almacenarse
en una estructura adecuada (por ejemplo, listas o diccionarios). 

3. Salida de datos: Una vez ingresada la información de al menos una constructora, mostrar un resumen con:

o Nombre de la constructora
o Total de proyectos vigentes
o Total de ventas sumando todas las ventas de los proyectos

Opcional: Permitir el ingreso de varias constructoras y finalizar el programa cuando
el usuario lo indique. Exportación de datos: Al finalizar, permitir al usuario exportar los datos ingresados
en un archivo de texto (.txt) con el siguiente formato:
Nombre: Construcciones XYZ
Total de proyectos vigentes: 2
Total de ventas: 15
---
Nombre: Construcciones ABC
Total de proyectos vigentes: 3
Total de ventas: 25
--- Ejemplo de
"""

"""
 {
    builderName: "CONSTRUCTORA BOLIVAR",
    projectNumber: 56,
    salesProject: 1
 }

"""
# Diccionario de constructoras 
bbuilder = {}

def validator(input_text):
    option = 0
    while True:
        try:
            option = int(input_text)
            if option <= 0:
                print("Ingresa un número mayor a 0")
            else: 
                return option
        except ValueError:
            print("Por favor, ingresa un número válido")
        input_text = input("Introduce nuevamente el número:")  

while True:
    print("Bienvenido al programa de registro de Constructoras")
    print("1.- Agregar Constructora")
    print("2.- Mostrar cantidad de proyectos de las Constructoras")
    print("3.- Ventas de proyectos por Constructora")
    print("4.- Ver proyectos guardados por Constructoras")
    print("5.- Salir del programa")

    opcion = input("Introduce el número de la opción que deseas: ")        
    try:
        opcion = validator(opcion)
        
        if opcion == 1:
            constructora = input("Ingresa el nombre de la constructora: ")
            proyecto = input("Ingresa proyecto de la constructora: ")
            venta = input("Ingresa venta de la constructora: ")
            id_proyecto = len(builder) + 1
            builder[id_proyecto] = {
                "constructora": constructora,
                "Proyecto": proyecto,
                "venta": venta,
            }
            print("Constructora y sus datos guardados correctamente")

        elif opcion == 2:
            print("Los proyectos registrados son:", len(builder))

        elif opcion == 3:
            for id_proyecto, datos in builder.items():
                print(f"ID: {id_proyecto}, Ventas: {datos['venta']}")

        elif opcion == 4:
            for id_proyecto, datos in builder.items():
                print(f"ID: {id_proyecto}, Datos: {datos}")

        elif opcion == 5:
            print("Saliendo del programa...")
            break

    except Exception as e:
        print(f"Error inesperado: {e}")
