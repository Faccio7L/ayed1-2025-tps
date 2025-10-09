def main():
    """
    Elimina numeros de un set, se manejan excepciones.
    
    """
    set_por_comprension = set(x for x in range(0,10))
    print(set_por_comprension)
    while True:
        try:
          eliminar = int(input("Ingrese un numero para eliminar del set(-1 para salir:"))
          if eliminar in set_por_comprension:
            set_por_comprension.remove(eliminar)
          if eliminar == -1:
              break
        except ValueError:
           print("Ingrese un numero valido.")
    print(set_por_comprension)

main()