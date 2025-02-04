esta=int(input("Ingresa tu estatura"))
pes=int(input("Ingresa tu peso"))
IMC= esta/(pes**2)

if IMC<18.5:
    print ("Bajo peso")
elif IMC<24.9:
    print ("Peso normal")
elif IMC<29.9:
    print ("Sobrepeso")
elif IMC>30:
    print ("Obesidad")