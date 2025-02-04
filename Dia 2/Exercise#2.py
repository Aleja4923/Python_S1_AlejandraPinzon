def intsim (a,b,c):
    a=0
    b=0
    c=0
    v=(a*b*c)
    return v

def intcom (w,e,r):
    w=0
    e=0
    r=0
    n=w*(1*e)**r
    return n


op=int(input("1. Interes simple o 2. Interes compuesto"))
if op==1:
    d=int(input("Ingrese el capital inicial"))
    f=int(input("Ingrese la tasa de interes"))
    g=int(input("Ingrese el numero de periodos"))
    intsim (d,f,g)
    print ("El interes simple es",  intsim(d,f,g))

if op==2:
    o=int(input("Ingrese el capital inicial"))
    p=int(input("Ingrese la tasa de interes anual"))
    q=int(input("Ingrese el numero de periodos"))
    print ("El interes compuesto es",  intcom(o,p,q),)

    an=int(input("Ingrese el periodo de tiempo que desee que se muestre"))
    print ("Cual' interes ")



