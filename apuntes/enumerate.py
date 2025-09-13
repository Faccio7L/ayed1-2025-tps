from functools import reduce
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


#Clase 4.
#Lambda.
def square(num:int) -> int:
    return num ** 2
#es lo mismo que 
square = lambda x: x ** 2 #square es funcion lambda. NO variable.
lambda_func = lambda x: x**2 >= 10 #retorna True o False.

#Funciones de orden superior.
#map,filter,reduce()
#map: Agarro un iterable, por cada elemnento lo "proceso" mediante una funcion, si entran 100 salen 100.
#Filter: Filtra con True o False. "Pasan" los True. ej: es_citrico y le paso frutas.
#Reduce: Toma todos los datos y retorna uno solo.

def map_(funcion,lista)-> list[int]: #SOLO nombre de la funcion, sin parentesis.
    for i, e in enumerate(lista): #primero consulta indice y dsp el elemento el enumerate.
        lista[i] = funcion(e)
    return lista
  
def doble(x):
    return x * 2

lista = [3,3,3,3]
print(map_(doble,lista))

list_por_comprension = [x for x in range(1,11)] #lista por comprension.
lista = [3,3,3,3]


def map_(funcion,lista)-> list[int]: #SOLO nombre de la funcion, sin parentesis.
    for i, e in enumerate(lista): #primero consulta indice y dsp el elemento el enumerate.
        lista[i] = funcion(e)
    return lista
print(map_(doble,list_por_comprension))
list_por_comprension = [x for x in range(1,31)] #1: elemento QUE voy a guardar. 2: Variable. 3: ITERABLE. 4: CONDICION
lista_modificada_lambda_map = list(map(lambda x: x*2,list_por_comprension)) #ESTA ES LA FUNCION CORRECTA.
print(lista_modificada_lambda_map)
lista_modificada_filter = list(filter(lambda x: x%3 == 0,list_por_comprension))
print(lista_modificada_filter)

lista = ["uno","dos","tres"]
salida = list(map(lambda palabra: palabra.title(),lista)) 
print(salida)
salida = list(map(lambda palabra: palabra.upper(),lista))
print(salida)
print(list(filter(lambda x: not x % 2, [1,2,3,4,5])))
#importo reduce.
producto = reduce((lambda x,y : x*y),[1,2,3,4])
print(producto) 

#castear booleanos
print(int(True))
enteros = [True,False] # 1 y 0 
suma = reduce(lambda a, b: a + b,enteros) #1 + 0
print(suma)


#otra vez listas por comprension
numeros = [2,3,5]
num_cubos = []
for num in numeros:
    num_cubos.append(num**3)
print(num_cubos)
#manera correcta:
numeros = [2,3,5]
num_cubos = []
num_cubos = [num**3 for num in numeros]
print(num_cubos)
lista = [i for i in range(1,11)]
print(lista)

#MUY UTIL
cadena = "estoy aprendiendo Python3 en 2022"

digitos = [char for char in cadena if char.isdigit()]
#cuando no uso else va al final la condicion, caso contrario van al principio
print(digitos)
#caso con else
digitos = [char if char.isdigit() else char.upper() for char in cadena] #clave para tp4.
print(digitos)
#otra vez join!
paises = ["Argentina", "Uruguay", "Chile", "Paraguay", "Brasil", "Bolivia"]
paises_string = ",".join(paises) # con que los uno, join e iterable.
print(paises_string)

#split hace lo mismo, pero al reves.
nombre_string = "Mi nombre es Mariano"
nombre_lista = nombre_string.split(" ") ## maxsplit seteado a 2
print(nombre_lista)

nombre_lista[-1] = "Mateo"
print(nombre_lista)
cadena = " ".join(nombre_lista)
#cadena = nombre_lista[0] + " " + nombre_lista[1] + ......

print(cadena)
lista = [9,3,2]
lista[1:1] = [5]
print(lista)

#Libreria RE


cadenas = ["A123", "B456", "C789", "123A", "D3214"]
# una letra mayúscula o minúscula y 3 números del 1 al 3
patron = "[A-Za-z][1-3]{3}" #Busca que empiece con una letra y despues 3 numeros del 1 al 3.