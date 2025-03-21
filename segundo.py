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
builder = {}



while True:

    print("Bienvenido al programa de registro de Constructoras")
    print("1.- Agregar Constructora")
    print("2.- Mostrar  cantidad de proyectos de las Constructoras")
    print("3.- ventas de proyectos por  Constructora")
    print("4.- ver proyectos guardados por Constructoras")
    print("5.-salir del programa ")

    opcion = (int(input("Introduce el número de la opción que deseas: ")))

    if opcion == 1:
        
                id_constructora =(int(input("Ingresa un ID único para esta Constructora: ")))
                nombre = input("Ingresa el nombre de la Constructora: ")
                cantidad =  (int(input("Ingresa la cantidad de proyectos vigentes de esta Constructora: ")))
                ventas = input("ingresa las ventas de la constructora: ")
                builder[id_constructora] = {
                    "nombre": nombre,
                    "cantidad": cantidad,
                    "ventas": ventas,
                    }
                
    elif opcion == 2:
        if cantidad >= 0 :
             print("no hay datos ingresados")
           
        else:
             print("la cantidad total de proyectos son :",cantidad + cantidad)

                
    elif opcion == 3:
        
            if ventas >= 0: 
                print("No existen ventas registradas")
            else:
                print(f"Ventas registradas:1",{ventas}+ {ventas})
    elif opcion == 4:
        
        print(builder,"estos son los proyectos ingresados")    
        
    elif opcion == 5:
        
        print("saliste del programa ")   
        break
    
    else :
         print("Ingresa una opcion valida ")