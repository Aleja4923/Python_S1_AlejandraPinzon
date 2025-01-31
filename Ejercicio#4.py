# Alejandra Pinzon ALvarez
grande=0.0
pequeno=0.0
for i in range (1,10):
    num= int(input("Ingrese numero"))
    if grande == 0 or pequeno == 0:
        grande=num
        pequeno=num
    else:
        if num > grande:
            grande = num
        if num < pequeno:
            pequeno = num
print ("Grande:",grande)
print ("Pequeño:",pequeno)
# Alejandra Pinzon ALvarez
                    