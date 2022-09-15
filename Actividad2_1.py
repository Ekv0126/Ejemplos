print("***** Actividad No. 2 *****")
print("Erick Ramírez Villafuerte")
print("200915472")

lista=[]
for i in range(15):
    lista.append(input("Ingrese un nombre para almacenar: "))
print("\n\n Datos ordenados alfabeticamente a/z")
lista.sort()
print(lista)
print("\n\n Datos ordenados alfabeticamente z/a")
lista.reverse()
print(lista)

contador=0
print("\n\n promedio de la cantidad de cada elemento de la lista")

for letra in lista:
    contador=contador+len(letra)

promedio=contador/len(lista)
print("El promedio de letars usadas en cada elemento de la lista es de ",promedio)

print("\n\n Mostrando solo los nombres que terminan con vocal")
for vocal in lista:
   # print(vocal)
    if vocal[-1]== "a":
        print(vocal)
    elif vocal[-1]== "e":
        print(vocal)
    elif vocal[-1]== "i":
        print(vocal)
    elif vocal[-1]== "o":
        print(vocal)
    elif vocal[-1]== "u":
        print(vocal)
     

