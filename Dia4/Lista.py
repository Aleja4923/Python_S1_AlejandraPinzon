def funcion():  
       for i in range(len(nombres)):  
         print("Estudiante #", i + 1, ": "," ".join(nombres[i])," ".join(apellidos[i]))  


nombres = [  
    ["Adrián"],  
    ["Alejandra"],  
    ["Ámbar", "Isabella"],  
    ["Andrés", "David"],  
    ["Aura", "Camila"],  
    ["Camilo", "Andrés"],  
    ["Daniel", "Esteban"],  
    ["David", "Santiago"],  
    ["Edgar", "Leonardo"],  
    ["Gerson", "Steven"],  
    ["Harley", "Yefrey"],  
    ["John", "Stiven"],  
    ["Juan", "David"],  
    ["Juan", "David"],  
    ["Juan", "David"],  
    ["Juan", "Eduardo"],  
    ["Juan", "Fernando"],  
    ["Juan", "Jose"],  
    ["Maria", "Juliana"],  
    ["Mateo", "Roman"],  
    ["Naya", "Zarela"],  
    ["Nicolas"],  
    ["Omar", "Fernando"],  
    ["Santiago"],  
    ["Santiago", "Andrés"],  
    ["Santiago"],  
    ["Sara", "Sofía"],  
    ["Sayara", "Yurley"],  
    ["Sergio", "Andrés"],  
    ["Simón", "Dante"],  
    ["Thomas", "Sebastián"],  
    ["Vladimir"]  
]  


apellidos = [  
    ["Quintero", "Pinzón"],  
    ["Pinzón", "Alvarez"],  
    ["Plata", "López"],  
    ["Reyes", "Espinel"],  
    ["Pico", "Araque"],  
    ["Suárez", "Fuentes"],  
    ["Guerrero", "Quintero"],  
    ["Vera", "Mendez"],  
    ["Acevedo", "Arteaga"],  
    ["Chaparro", "Martínez"],  
    ["Cabrales", "Vargas"],  
    ["Negron", "Regalado"],  
    ["Saavedra", "Jaimez"],  
    ["Santoyo", "Jaimes"],  
    ["Vargas", "Soto"],  
    ["Pinilla", "Guzmán"],  
    ["Umaña", "Barragan"],  
    ["Abril", "Roman"],  
    ["Saavedra", "Mejia"],  
    ["Camargo"],  
    ["Lizcano", "Jaimes"],  
    ["Chedraui", "Mantilla"],  
    ["Granados", "Parra"],  
    ["Aguilar", "Vesga"],  
    ["Quiñonez", "Sosa"],  
    ["Jaimes", "Perez"],  
    ["Díaz", "Rodríguez"],  
    ["Aparicio", "Arciniegas"],  
    ["Rueda", "Hernández"],  
    ["Salamanca", "Galvis"],  
    ["Bastos", "Garcia"],  
    ["Diaz", "Contreras"]  
]  
b=True
while (b==True):
        print("Bienvenido, ¿que desea hacer?")  
        print("1. Agregar estudiante")  
        print("2. Editar estudiante")  
        print("3. Eliminar estudiante")  
        print("4. ver lista")  
        print("5. Salir") 

        op = int(input(": "))  
        if op == 1:
                nuevo_nombre = input("Ingrese el nombre completo del estudiante : ")
                nuevo_apellido = input("Ingrese los apellidos del estudiante: ")
                nombres.append(nuevo_nombre)
                apellidos.append(nuevo_apellido)
                print("Estudiante agregado con exito.")
                funcion()

        if op == 2:  
                funcion()
                ne = int(input("Ingrese el numero del estudiante: "))  
                nu = int(input("Desea editar 1. Nombre 2. Apellido 3. Nombre y apellido: "))  
       
                match nu:  
                        case 1:  
                                funcion()
                                nombreEst = input("¿Cuál será el nombre nuevo del estudiante?: ")  
                                nombres[ne - 1] = [nombreEst]  
 


                        case 2: 
                                funcion() 
                                apellidoE = input("¿Cuál será el apellido nuevo del estudiante?: ")  
                                apellidos[ne - 1] = [apellidoE]   
                                funcion() 


                        case 3: 
                                funcion() 
                                nombreE = input("¿Cuál sera el nombre nuevo del estudiante?: ")  
                                apellidoE = input("¿Cuál sera el apellido nuevo del estudiante?: ")  
                                nombres[ne - 1] = [nombreE]    
                                apellidos[ne - 1] = [apellidoE]  
                  
        if op == 3:
                funcion()
                numeroEstudiante=int(input("Cual estudiante quieres eliminar?:"))
                nombres.pop(numeroEstudiante-1)
                apellidos.pop(numeroEstudiante-1)

        if op == 4:
                funcion()
        if op == 5:
                b=False