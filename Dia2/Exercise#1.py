def Celsius (n):
    j=0
    j=(n*9/5)+32
    return j

def Fahrenheit (n):
    f=0
    f=(n-32)*5/8
    return f
n=0
n=int(input("Ingrese la temperatura"))
op=int(input("1. Celsius a Fahrenheit o 2. Fahrenheit a Celsius"))
if op==1:
    Celsius(n)
    print (Celsius(n))
if op==2:
    Fahrenheit (n)
    print (Fahrenheit (n))


