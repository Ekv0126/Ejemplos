print("Feliz día ")
print("Listas en Python")

lista=[1,2,"Hola",10+10,True,"datos",20,40]
print(lista)
print("El primer elemento es: ",lista[0])
print("El último elemento es: ",lista[-1])

print("Elementos en posición específica de una lista 2,3 y 4", lista[2:5])

print("Elementos desde una posición específica de una lista ", lista[4:])

print("Elementos en posición desde la cero hasta la 4", lista[:3])

print("Usando un ciclo para recorrer una lista")
print("reccorriendo una lista conF FOR")
for elemento in  lista:
    print(elemento)

#cantidad de elementos de una lista
cantidad=len(lista)
print("El tama;o de la lista es de: ", cantidad)

print("reccorriendo una lista con WHILE")
ciclo=0

while ciclo<cantidad:
    print(lista[ciclo])
    ciclo =ciclo+1

print("Cambio de valor dentro de un elemento de una lista")
lista[3]="Este fue el cambio"

print(lista)
lista.append("[ULTIMO")
lista.append("Este sí es el último")

print(lista)


print("Agregando en un índice específico: ")

print(lista)
lista.insert(3,"Inserté en la pos 2")

print(lista)

print("\n\n Elimiando un elemento por valor o nombre")
lista.remove(1)
print(lista)

print("\n\n Elimiando un elemento por posici[on")
print(lista)
lista.pop(0)
print(lista)

lista.pop()
print(lista)

print("\n\nIngresar textos y ordenarlos alfabeticamente")
nombres=[] # creaci[on de una lista vac[ia para llenar desde el ciclo
for i in range(11):
    print(i)
    print("Ingrese un texto, se almacenara en el indice: ",i)
    nombres.append(input(" Ingrese un nombre para almacenar: "))
    
print(nombres)
nombres.sort() # para odenar de mayor a menor
print(nombres)
nombres.reverse()
print(nombres)




    
    

