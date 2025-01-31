print("Hola Mundo!")
## Tipos de dayos
#1. String
cadenaTexto= "Texto"
prynt (type(cadenaTexto)) # Imprimir Tipo de dato

# 2. Numero Entero - int 
numeroEntero=2
print (type(numeroEntero))

# 3. Numero FLotante - float
numeroFlotante= 1.1
print(type(numeroFlotante))

# 4. Numero Doble
numeroDouble=3.141658694
print (type(numeroDouble))

# 5. Booleano- True/False
booleano= True
print (type(booleano))


# Entradas usuario
x=input("Ingrese un numero: ")
print (type(x))

#Conversion tipos de datos
x=int input ("Ingrese el tipo de dato")


#Ejercicio sumar 2 numeros

num1= int(input("Ingrese el primer numero"))
num2= int(input ("Ingrese el segundo numero"))
resultadosumatorio= num1+num2
print ("El resultado es : "),resultadosumatorio

##Ciclos for y while 
##Ciclo for nomal
for i in range(5):##i será el iterador e irá hasta el 5
    print(i)
##Ciclo desde hasta
print("#############")
for i in range(0,5):##i será el iterador e irá desde el cero hasta el 5
    print(i)

##Ciclo con pasos
print("#############")
for i in range(0,5,2):##i será el iterador e irá desde el cero hasta el 5 en paso de 2 en 2
    print(i)

#Ciclo WHile
booleano1= True
while (booleano1== True):
    print(booleano1)
    booleano1=False

#4 Tipos de funciones
#FUncion sin parametros y sin retorno
def funcion1():
    print("FUncion")

funcion1()
#Funcion sin parametros pero con retorno
def funcion2():
    return 5
print ("Su numero es:",funcion2())

#Funcion con parametros pero sin retorno
def funcion3 (nombre,apellido):
    print("Su nombre es : ",nombre" su apellido es",apellido)
funcion3("Alejandra","Pinzon")

#Funcion con parametros y retonor
def funcion4(a,b):
    c=a**b
    return c
funcionA= int(input("Ingrese el numero base:"))
funcionB=int(input("Ingrese la elevación deseada:"))
print("El resultado de su elevación es de:",funcion4(funcionA,funcionB))
##Desarrollado por : Alejandra Pinzon / C.C:1097498715