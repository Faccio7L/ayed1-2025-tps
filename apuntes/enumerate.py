#salida = vuelto(pago,billete) #dos datos.
#for i, s in enumerate(salida): #i indice. Retorna tupla.
    #if s: #0 lo interpreta como False.
        #print("f{s} billetes de {valores[i]}")


lista = [100,200,300,400]
for tupla in enumerate(lista): #enumerate Pregunta el indice de cada elemento.
    indice, dato = tupla #desempaquetado.
    print(indice)
    print(dato)

nombres = ["juan","lucas"]
edades = [22, 39]

for n, e in zip(nombres,edades): #zip para desempatecar, recibe iterables y retorna tuplas
    print(f"{n} tiene { e} años")

lista1 = [2,4,5,7,9]
ultimo = lista[-1]

#Rebanadas.
lista_1 = [2,4,5,6,7]
lista_2 = lista_1[1:3] #funciona como range, se appendea 4 y 5
lista_3 = lista_1[1:] #Desde indice un hasta el final.

nom_ape = " ".join("Luciano Juan Dominguez".split()[-2:]) #Convierte esto en una lista. - 1 obtengo apellido
print(nom_ape)
#split convierte iterable a lista
#join convierte un iterable a str.

#divmod