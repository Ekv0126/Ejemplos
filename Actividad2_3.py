productos={
    "1":"pro1",
    "2":"pro2",
    "3":"pro3",
    "4":"pro4",
    "5":"pro5",
    "6":"pro6",
    "7":"pro7",
    "8":"pro8",
    "9":"pro9",
    "10":"pr10",
    "11":"pro11",
    "12":"pro12",
    }

pro1={
    "codigo":"cod1",
    "Nombre":"pro1",
    "Precio":1
    }
pro2={
    "codigo":"cod2",
    "Nombre":"pro2",
    "Precio":2
    }
pro3={
    "codigo":"cod3",
    "Nombre":"pro3",
    "Precio":3
    }
pro4={
    "codigo":"cod4",
    "Nombre":"pro4",
    "Precio":4
    }
pro5={
    "codigo":"cod5",
    "Nombre":"pro5",
    "Precio":5
    }

pro6={
    "codigo":"cod6",
    "Nombre":"pro7",
    "Precio":7
    }
pro7={
    "codigo":"cod7",
    "Nombre":"pro7",
    "Precio":7
    }
pro8={
    "codigo":"cod8",
    "Nombre":"pro8",
    "Precio":8
    }
pro9={
    "codigo":"cod9",
    "Nombre":"pro9",
    "Precio":9
    }
pro10={
    "codigo":"cod10",
    "Nombre":"pro10",
    "Precio":10
    }

pro11={
    "codigo":"cod11",
    "Nombre":"pro11",
    "Precio":11
    }
pro12={
    "codigo":"cod12",
    "Nombre":"pro12",
    "Precio":12
    }
print("\n\n Listado de productos.")

for i,j in pro1.items():
    print(i,j,)
print("\n")
for i,j in pro2.items():
    print(i,j)
print("\n")

for i,j in pro3.items():
    print(i,j,)
print("\n")
for i,j in pro4.items():
    print(i,j)
print("\n")

for i,j in pro5.items():
    print(i,j,)
print("\n")
for i,j in pro6.items():
    print(i,j)
print("\n")
for i,j in pro7.items():
    print(i,j,)
print("\n")
for i,j in pro8.items():
    print(i,j)
print("\n")
for i,j in pro9.items():
    print(i,j,)
print("\n")
for i,j in pro10.items():
    print(i,j)
print("\n")
for i,j in pro11.items():
    print(i,j,)
print("\n")
for i,j in pro12.items():
    print(i,j)
print("\n")

print("\n\n Listado de productos con aumento.")
pro1["Aumento"]=(pro1.get("Precio")*110/100)
print(pro1,"\n")

pro2["Aumento"]=(pro2.get("Precio")*110/100)
print(pro2,"\n")

pro3["Aumento"]=(pro3.get("Precio")*110/100)
print(pro3,"\n")

pro4["Aumento"]=(pro4.get("Precio")*110/100)
print(pro4,"\n")

pro5["Aumento"]=(pro5.get("Precio")*110/100)
print(pro5,"\n")

pro6["Aumento"]=(pro6.get("Precio")*110/100)
print(pro6,"\n")

pro7["Aumento"]=(pro7.get("Precio")*110/100)
print(pro7,"\n")

pro8["Aumento"]=(pro8.get("Precio")*110/100)
print(pro8,"\n")

pro9["Aumento"]=(pro9.get("Precio")*110/100)
print(pro9,"\n")

pro10["Aumento"]=(pro10.get("Precio")*110/100)
print(pro10,"\n")

pro11["Aumento"]=(pro11.get("Precio")*110/100)
print(pro11,"\n")

pro12["Aumento"]=(pro12.get("Precio")*110/100)
print(pro12,"\n")

print(" Actualizando un valor dentro de un diccionario")

print(pro1)
pro1.update({"Nombre":"ProductoNo. 1"})
print(pro1)
