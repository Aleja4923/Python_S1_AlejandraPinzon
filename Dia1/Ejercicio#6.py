# Alejandra Pinzon ALvarez
N = int(input("Ingrese la cantidad de empleados: "))

totalBruto = 0
totalEPS = 0
totalPension = 0
totalNeto = 0
mayorSueldo = 0
menorSueldo = 0.0
nombreMayor = 0
nombreMenor = 0
sueldoa= 0
sueldom= 0

# Ciclo para procesar cada empleado
for i in range(1, N+1):
    nombre=input("Ingrese el nombre del empleado :")
    horas=int(input("Ingrese horas trabajadas"))
    bruto = horas * 20000
    eps = bruto * 0.04
    pension = bruto * 0.04
    neto = bruto - eps - pension
    # Acumular totales
    totalBruto = bruto + totalBruto
    totalEPS = eps + totalEPS
    totalPension = pension + totalPension
    totalNeto = neto + totalNeto
    mayorSueldo=neto
    if mayorSueldo>menorSueldo:
        sueldoa=mayorSueldo
        menorSueldo=mayorSueldo
        nombreMayor=nombre
        
    else:
        if mayorSueldo<menorSueldo:
            sueldom=mayorSueldo
            nombreMenor=nombre


    print("Empleado: ", nombre)
    print("Sueldo Bruto:",bruto)
    print("EPS: ", eps)
    print("Pensión: ",pension)
    print("Sueldo Neto:", neto)
# Calcular promedios
promedioBruto = totalBruto / N
promedioNeto = totalNeto / N
# Mostrar resultados finales
print("Totales:")
print("Total Salarios Brutos:",totalBruto)
print("Total EPS:", totalEPS)
print("Total Pensión: ", totalPension)
print("Total Salarios Netos: ", totalNeto)
print("Empleado que más gana:", nombreMayor,sueldoa)
print("Empleado que menos gana: ", nombreMenor,sueldom)
print("Promedio Salarios Brutos: ",promedioBruto)
print("Promedio Salarios Netos:", promedioNeto)
# Alejandra Pinzon ALvarez