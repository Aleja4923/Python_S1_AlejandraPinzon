
from Modul import *
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
        print("4. Ver lista")  
        print("5. Salir") 

        op = int(input(": "))
        if op == 1:
                nuevo_nombre = input("Ingrese el nombre completo del estudiante : ")
                nuevo_apellido = input("Ingrese los apellidos del estudiante: ")
                agregar(nuevo_nombre,nuevo_apellido,nombres,apellidos)
                print("Estudiante agregado con exito.")

        if op == 2:  
                ne = int(input("Ingrese el numero del estudiante: "))  
                nu = int(input("Desea editar 1. Nombre 2. Apellido 3. Nombre y apellido: "))  
       
                match nu:  
                        case 1:  
                                nombreEst = input("¿Cuál será el nombre nuevo del estudiante?: ")
                                Nuevonombre(nombres,ne,nombreEst)
                        case 2: 
                                apellidoE = input("¿Cuál será el apellido nuevo del estudiante?: ")
                                Nuevoape(apellidos,ne,apellidoE)
                        case 3:  
                                nombreE = input("¿Cuál sera el nombre nuevo del estudiante?: ")  
                                apellidoE = input("¿Cuál sera el apellido nuevo del estudiante?: ") 
                                Nuevonombre(nombres,ne,nombreEst)
                                Nuevoape(apellidos,ne,apellidoE)

        if op == 3:
                funcion(nombres,apellidos)
                numeroEstudiante=int(input("Cual estudiante quieres eliminar?:"))
                eliminar(nombres,numeroEstudiante,apellidos)

        if op == 4:
                funcion(nombres,apellidos)
        if op == 5:
                b=False