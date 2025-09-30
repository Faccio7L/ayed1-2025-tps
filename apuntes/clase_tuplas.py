salsas = ("salsa de tomate","salsa picante","salsa especial")

salsas = salsas + ("criolla",) #la nueva tupla salsa va a tener otro ID, NO es la misma
                                #tupla
primavera = (21, "septiembre") #recordatorio de que son heterogeneas!

tupla = (1,2,3)
lista = list(tupla) #casteo! tupla sigue existiendo.


a = 5
b = 10
a, b = (b,a) #intercambiar valores de dos variables. el parentesis no es necesario
             #pero se intercambian mediante una tupla.
print(a,b)

#CONJUNTOS.
#RECORDATORIO! tuplas, listas = ordenadas(tienen indice), diccionario = no tiene orden
#TAMPOCO tiene indices, osea NO es ordenado.
frutas = {"banana","frutilla","manzana","banana"} #NO acepta duplicados.
for fruta in frutas:
    print(fruta)

#conjunto vacio 
conjunto = set() #si o si hay que usar al construcutor.
conjunto.add(1)
conjunto.add(32)
conjunto.add(5432)
conjunto.add(9999)
conjunto.add(112313321)
print(conjunto)
conjunto.discard(32)
print(conjunto)

import random as rn

simbolos = ("copas", "espadas", "bastos", "oros") # tupla
mano = set() # conjunto
intentos = 0

while len(mano) < 7:
    numero = rn.randint(1, 12)
    # elige un palo al azar de la tupla simbolo
    palo = rn.choice(simbolos)
    carta = (numero, palo)
    # agrega datos inmutables
    mano.add(carta)
    intentos += 1

print(mano)
print(f"Intentos: {intentos}")

def genera_codigos():
    codigos = set()
    while len(codigos) < 15:
        # Agrega un dato nuevo solo si no está repetido
        codigos.add(rn.randint(100, 999))
    return sorted(codigos)

print(genera_codigos())