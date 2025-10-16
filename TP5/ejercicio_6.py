def main()->None:
        """
        Se llena una lista de numeros a voluntad del usuario, posteriormente el 
        usuario puede buscarlos para averiguar su indice en la lista, en caso
        de que busque numeros que no se encuentran 3 veces, se corta el programa.
        """
        lista = []
        while True:
            
            num = input("Ingrese un numero para la lista: ")
            if num == "-1":
                break
            try:
                lista.append(int(num))
            except Exception as e:
                print("Usted debe ingresar un numero entero.")
        contador = 0
        while True:
            a_buscar = input("Ingrese un numero para averiguar su indice:")
            try:
                a_buscar = int(a_buscar)
            except Exception as e:
                print("Debe ingresar un numero entero")
            else:
                if contador == 3:
                    break
                try:
                    print(lista.index(a_buscar))
                except Exception as e:
                    print("no esta en la lista.")
                    contador += 1
main()
        