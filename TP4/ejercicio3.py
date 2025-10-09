def claves(clave_maestra:str)->list:
    """
    genera dos claves mediante el str recibido, una con los indices impares y otra
    de pares.
    """
    clave_1 = [e for i, e in enumerate(clave_maestra)if i % 2 == 0 ]
    clave_2 =  [e for i, e in enumerate(clave_maestra)if i % 2 == 1 ]
    #agrego e a cada lista si el indice es par o impar(busco indice con el enumerate)
    return clave_1,clave_2
    


def main()->None:
    "genera una clave e invoca la funcion claves."
    clave_maestra = input("Ingrese la clave maestra:")
    print(claves(clave_maestra))
main()