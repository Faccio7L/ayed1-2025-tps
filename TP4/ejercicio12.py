def main():
    palos = ["oro","basto","espada","copa",] 
    lista = [(numeros,palo) for palo in palos  for numeros in range(1,13)]
    print(lista)
main()