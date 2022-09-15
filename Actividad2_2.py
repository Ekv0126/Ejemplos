print("***** Actividad No. 2 *****")
print("Erick Ramírez Villafuerte")
print("200915472")

numeros=[]
for i in range(10):
    numeros.append(int(input("Ingrese un numero para almacenar: ")))
print("Los numeros ingresados son: ")
print(numeros)

print("\n\n Mostrando solo el de menos valor y el mas grande")

numeros.sort()
print(numeros[0],numeros[len(numeros)-1])

print("\n\n Datos descendente")
numeros.reverse()
print(numeros)

print("\n\n sumando los datos ingresados")
contador=0

for conteo in numeros:
    contador=contador+conteo

print("La suma de todos los numeros da como resultado> ",contador)


print("\n\n verificando que el n[umero no es primo")

for con in range(2,contador):
    if contador % con ==0:
        primo=False
    else:
        primo=True
        
if primo ==True:
    print("El Numero si es primo")
else:
    print("El Numero NO es primo")
