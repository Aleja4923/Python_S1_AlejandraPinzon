def agregar (a,s,d,f):  
    d.append(a)
    f.append(s)

def funcion(nombres,apellidos):
    for i in range(len(nombres)):  
        print("Estudiante #", i + 1, ": "," ".join(nombres[i])," ".join(apellidos[i]))   

def Nuevonombre (q,w,e,):
    q[w-1] =e

def Nuevoape (o,l,p):
    o[l-1]=p

def eliminar (z,x,h):
    z.pop(x-1)
    h.pop(x-1)
