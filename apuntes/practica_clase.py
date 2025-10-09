import random as rn
def main():
    lista = []
    while len(lista) < 10:
        num = rn.randint(0,100)
        if num not in lista:
            lista.append(num)
    return lista

print(main())

def aaaaaaaaa(): #para ver cuanto tarda en quedar en orden ascendente!
    pass
    contador = 1
    while True:
        
        lista = []
        while len(lista) < 10:
            num = rn.randint(0,100)
            if num not in lista:
                lista.append(num)
        if lista == sorted(lista):
            break
        else:
            contador += 1
    return contador


print(aaaaaaaaa())

random_ = "hola me llamo santi"
for i, e in enumerate(random_):
    print(i,e)


palos = ("oro","basto","copa","espada")
naipes = [(palo,numero) for palo in palos for numero in range(1,13)]
print(naipes)