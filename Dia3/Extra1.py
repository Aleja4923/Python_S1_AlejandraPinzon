cli=int(input("Ingrese el clima opciones : 1, Soleado 2.Lluvioso 3.Frio") )
ti=int(input("Ingrese hora como mañana, tarde o noche"))
match cli:
    case 1:
        if ti=="mañana":
            print ("Pan")
        elif ti=="tarde":
            print("Pan con queso")
        elif ti=="noche":
            print("Agua con pan")
    case 2:
        if ti=="mañana":
            print ("Uva")
        elif ti=="tarde":
            print("Uva con queso")
        elif ti=="noche":
            print("Agua con uva")
    case 3:
        if ti=="mañana":
            print ("Pan")
        elif ti=="tarde":
            print("Pan con queso")
        elif ti=="noche":
            print("Agua con pan")