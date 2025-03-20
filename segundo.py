t = {}


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
                t[id_constructora] = {
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
        
        print(t,"estos son los proyectos ingresados")    
        
    elif opcion == 5:
        
        print("saliste del programa ")   
        break
    
    else :
         print("Ingresa una opcion valida ")
         