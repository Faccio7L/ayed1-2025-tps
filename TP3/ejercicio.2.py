def patron_a(matriz):
    
    num = 1
    indice = 0 
    for f in matriz:
        for c in (f):
            f[indice] = num
            num += 2
            indice += 1 #no trabajo con el indice de elemento por que sino siempre es [0] antes del break!
            break
    return matriz

def patron_b(matriz):
    num = 27
    #step_de_rebanada = -1
    for i, f in enumerate(matriz):
          for i2, e in enumerate(f):
             if i2 == i:
                f[-i2 - 1] = num 
                num = num // 3
                break
    return matriz
def patron_c(matriz):
     
    num_inicial = len(matriz) + 1
    for x in range(num_inicial -1):
          num_inicial -= 1
          for cantidad in range(x + 1):
            matriz[x][cantidad] = num_inicial
    return matriz
          
def patron_d(matriz):
    num_inicial = len(matriz) * 2
    largo = len(matriz)
    
    for fila in range(largo):
        for columna in range(largo):
            matriz[fila][columna] = num_inicial
        num_inicial = num_inicial // 2
    return matriz

def patron_e(matriz):
    i = 0 #en la primera pasada va a terminar valiendo uno (esto es indice.)
    valor_inicial = 1
    largo = len(matriz)
    for fila in range(largo):
        if i == 1: #i en una pasada vale uno, en la otra 0, etc.
            i = 0
        else:
            i = 1 
        for columna in range(fila):
            matriz[fila][i] = valor_inicial
            valor_inicial += 1
            matriz[fila][i+2] = valor_inicial
    return matriz
            
def patron_f(matriz)-> list[list]:
    valor_inicial = 1
    largo = len(matriz)
    cantidad_por_fila = largo #lo almaceno aca por que esta variable la voy a modificar, largo no.
    for fila in range(largo):
        for columna in range(fila):
            matriz[fila][largo - 1 - columna] = valor_inicial
            valor_inicial += 1

    return matriz

def patron_g(matriz) -> list[list]:
    """
    Esta funcion esta hardcodeada, tendria que encontrar una forma de reemplazar
    los numeros por variables, no encuentro un patron para trabajarlos bien.
    pre: Recibe como parametro una matriz
    post: retorna una matriz en forma de espiral
    """
    inicial = 1
    largo = len(matriz)
    for columna in range(largo):
        matriz[0][columna] = inicial
        inicial += 1
    for fila in range(1,largo): #para no tocar [0] esa ya la complete
        matriz[fila][largo -1 ] = inicial
        inicial += 1
    for columna in range (largo -2, -1, -1):
        matriz[largo-1][columna] = inicial
        inicial += 1
    for fila in range(largo - 2, 0, -1 ): #Corta en uno, el indice 0 ya esta appendeado.
        matriz[fila][0] = inicial
        inicial += 1
    for columna in range(1,3): #solo completo 1 y 2.
         matriz[largo -3][columna] = inicial
         inicial += 1
    for fila in range(2,3):
        matriz[fila][2] = inicial
        inicial += 1
    for columna in range(2,3):
        matriz[columna][1] = inicial
    return matriz
            

            
          


          
def main():
    tamaño = int(input("Ingrese el tamaño de la matriz:"))
    matriz = []
    for f in range(tamaño): #range por qeu es no iterable
        fila = []
        for c in range(tamaño):
            fila.append(0) #hasta aca son listas de 0!!
        matriz.append(fila) #aca ya son filas de la matriz!!!
    print(patron_b(matriz))
main()