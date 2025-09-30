def main():
    set_por_comprension = set(x for x in range(0,10))
    print(set_por_comprension)
    while True:
        eliminar = int(input("Ingrese un numero para eliminar del set(0 para salir:"))
        if eliminar in set_por_comprension:
          set_por_comprension.remove(eliminar)
        if eliminar == 0:
            break
    print(set_por_comprension)

main()