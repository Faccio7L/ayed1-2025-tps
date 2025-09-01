import random as rn
def main()->None:
    """
    Genera una matriz con la longitud que desea el usuario y una lista de numeros usados.
    Completa esa lista con numeros no USADOS y los muestra en pantalla.
    pre: No recibe parametros.
    post: Muestra en pantalla la matriz completa.
    """
    print("Nota: tambien s calculara el cuadrado N, en ese rango sera completada la matriz.")
    N = int(input("Ingrese el tamaño de la matriz deseada:"))
    rango_numeros = N**2 
    matriz = []
    numeros_usados = []
    for fila in range(N):
        lista = []
        while len(lista) < N:
            num = rn.randint(1,rango_numeros)
            if num not in numeros_usados:
                lista.append(num)     
                numeros_usados.append(num)
        matriz.append(lista)
    print(matriz)
    
main()
