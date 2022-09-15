print("Uso de Conjuntos ")
print("se abren con llaves")

conjunto={"a",10,20,20+3,"ab","e",True,"a"}
print(conjunto)

print("Ejemplo de lista")
lista=["a",10,20,20+3,"ab","e",True,"a"]
print(lista)

print("Ejemplo de tupla")
tupla=("a",10,20,20+3,"ab","e",True,"a")
print(tupla)

print("El largo del conjunto es de: ",len(conjunto))
print("Tipo de elemento ", type(conjunto)) # set es un conjunto

for i in conjunto:
    print(i)

#contador=0
#while contador<len(conjunto):
 #   print()
  #  contador=contador+1

print("verificando si esetá un elemento dentro del conjunto")
print("a" in conjunto)
print("be" in conjunto)
print(23 in conjunto)

print("Agregar elementos al conjunto")
conjunto.add("Agregado1")
conjunto.add("Agregado2")
print(conjunto)

print("creando un conjunto vacio y solicitud de datos para un conjunto")
conjunto2=set({})
for i in range(6):
    conjunto2.add(input("Ingrese un texto"))

print("Mostrando los elementos ingresados")
for elemento in conjunto2:
    print(elemento)




    






