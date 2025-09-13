def nueva_cadena(cadena:str, caracteres:int):
    texto_nuevo = cadena[-caracteres::]
    return texto_nuevo

def main():
    cadena = input("Ingrese un texto")
    caracteres = int(input("Seleccione cuantos caracteres quiere ver:"))
    print(nueva_cadena(cadena,caracteres))
main()