print("***** Actividad No. 2 *****")
print("Erick Ramírez Villafuerte")
print("200915472")

tupla1=("sas","S2eS","Daito3S","Datoo4s","uDato5","Dato6","Dato7","Dato8")

print(tupla1)

print("\n\nMonstrando los valores que tiene la tupla")
for i in tupla1:
    print(i)

print("\n\nMonstrando los valores que tiene la tupla en mayúsculas")
for i in tupla1:
    print(i.upper())


print("\n\nMonstrando los valores que tiene la tupla en minúsculas")
for i in tupla1:
    print(i.lower())

print("\n\nMonstrando los valores que terminando con una letra S o s")
for i in tupla1:
    i.lower()
    if "s" in i:
        if i[-1] == "s":
            print(i)

vocala=0
vocale=0
vocali=0
vocalo=0
vocalu=0

print("\n\nContando las vocales de un texto")
for i in tupla1:
   # print(i)
    for vocal in i:
    #    print(vocal)
        if vocal == "a":
            vocala=vocala+1
        if vocal == "e":
            vocale=vocale+1
        if vocal == "i":
            vocali=vocali+1
        if vocal == "o":
            vocalo=vocalo+1
        if vocal == "u":
            vocalu=vocalu+1
total=vocala+vocale+vocali+vocalo+vocalu
print("la cantidad de a es de: ",vocala)
print("la cantidad de e es de: ",vocale)
print("la cantidad de i es de: ",vocali)
print("la cantidad de o es de: ",vocalo)
print("la cantidad de u es de: ",vocalu)
print("El total de vocales son: ",total)





