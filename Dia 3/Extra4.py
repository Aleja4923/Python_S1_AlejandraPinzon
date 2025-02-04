print("Ingrese tipo de moneda a convertir 1 a 3")
print("1. Dolares a Euros")
print("2. Dolares a Pesos Colombianos")
op=int(input("3. Dolares a Yenes"))
cant=int(input("Ingresa la cantidad"))
re=0
match op:
    case 1:
        eu=0.85
        re=eu*cant
    case 2:
        pc=4100
        re=pc*cant
        
    case 3:
        ye=110
        re=ye*cant
    case _:
        print("Opcion incorrecta")
        re=0
print(re)
