def positivo (num):
    if num>0:
        print ("El numero es positivo")
    elif num<0:
        print("El numero es negativo")
    if num == 1:
        print ("El numero no es primo ni compuesto")
    n=0
    for i in range (1,num+1,):
        if num % i == 0:
            n+= 1
    if n>2:
        print("El numero es compuesto")
    elif n == 2:
        print("el numero es primo")
        
    if num**0.5 == int(num**0.5):
        print ("Es un numero cuadrado perfecto")

num=int(input("Ingrese el numero a verificar"))
print (positivo(num))