# Alejandra Pinzon ALvarez
a = 1
b = 1
N = int(input("Hasta donde desea la secuencia?"))
for i in range(N):
    if i%2 == 0:  
        print(a)
        c = a + b  
    else:  
        print(a)
        c = a - b  
    a = b  
    b = c
# Alejandra Pinzon ALvarez