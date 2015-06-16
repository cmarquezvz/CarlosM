
op=0

print ("Lista de Supermercado\n")
print ("1.\tAgregar elementos a su lista")
print ("2.\tEliminar elementos de su lista")
print ("3.\tVer elementos de su lista")
print ("4.\tSalir")


lista=[]
while op<4:
       op=int (input("Ingrese su opcion a elegir\n"))
if op==1:
       ele=input("Ingrese un elemento\n")
       lista.append(ele)
elif op==2:
        print (lista)
        elim=int(input("Elimine un elemento de su lista\n"))
        del  lista[elim-1]
elif op==3:
        print (lista)
