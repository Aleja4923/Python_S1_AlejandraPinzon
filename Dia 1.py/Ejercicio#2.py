# Alejandra Pinzon ALvarez
N=int(input("Ingrese la cantidad de terminos"))
sum=0.0
for i in range(1,N): #Comienzo un bucle desde 1 para evitar el error con 0
    if i%2==0: # Si el termino es par se resta 
        sum=sum-(1/i)
    else: #Si es impar se suma
         sum=sum+(1/i)

print("La Cantidad de terminos es: ",N)
print("") # Se proyectan resultados
print("el resultado es: ",sum)

# Alejandra Pinzon ALvarez