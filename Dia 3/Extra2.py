def kil(km):
    return km * 0.621371

def celsius(celsius):
    return (celsius * 9/5) + 32

def kilo(kg):
    return kg * 2.20462

print("1. Puedes elegir lo siguiente")
print("2. Celsius a Fahrenheit")
oP=int(input("3. Kilogramos a libras"))
cant=int(input("Escriba la cantidad que desea convertir"))

match oP:
    case 1:
        kil(cant)
        print (kil(cant))
    case 2:
        celsius(cant)
        print (celsius(cant))
    case 3:
        kilo(cant)
        print (kilo(cant))

