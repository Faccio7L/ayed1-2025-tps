def cargar_numeros_enteros()-> list[list]:
    """
    Genera una matriz vacia con las dimensiones elegidas por el usuario. Posteriormente
    el usuario las llena de enteros
    pre: No recibe parametros
    post: Retorna la matriz cargada
    """
    N = int(input("Ingrese el tamaño de la matriz:"))
    matriz = []
    for f in range(N): #fila
        fila = [] 
        for c in range(N): #columna
            num = int(input("Ingrese el valor que desea appendear:"))
            fila.append(num)   
        matriz.append(fila)
    return matriz

def ordenar_forma_ascendente()->list[list]:
    """
    Ordena filas de matrices en orden ascendente
    pre: No parametros.
    post: Retorna la matriz ordenada
    """
    matriz =[[1,4,12],
            [53,22,13],
            [33,22,14] 
                    ]
    for f in matriz:
        f.sort() #le paso la lista sub 0,1,2 etc.
    return matriz
def intercambiar_filas(num_1:int = 1,num_2:int = 2)->list[list]:
    """
    Intercambia filas de una matriz.
    pr: Recibe como parametro las filas a intercambiar
    post: Retorna el nuevo orden de las matrices
    """
    
    matriz = [[3,2,4,2],
              [2,4,12],
              [4,12,99]]
    matriz[num_1],matriz[num_2] = matriz[num_2], matriz[num_1] #si intercambio uno por uno, tendria que trabajar con una aux. Mejor asi.
    return matriz
    
def calcular_promedio_fila(fila:int = 2)->int:
    """
    Calcula el promedio de los valores de una fila de la matriz
    pre: Recibe como parametro la fila a calcular.
    post:Retorna el promedio
    """
    matriz = [[3,2,4,2],
              [2,4,12],
              [4,12,99]]
    contador = 0
    acumulador = 0
    for f in matriz[fila]: 
        contador += 1  
        acumulador += f   
    promedio = acumulador/ contador
    print(promedio)

def impares_por_columna(columna:int = 2)->list[int]:
    """
    Busca los impares de una columna y los appendea a una lista
    pre: Recibe como parametro la columna a buscar
    post: Retorna la lista de impares por columna 
    """
    lista_impares_columna = []
    matriz = [[3,2,4],
              [2,4,13],
              [4,12,99]]
    for fila in matriz:
        if fila[columna] % 2 != 0:
            lista_impares_columna.append(fila[columna])
    return lista_impares_columna

def transponer_matriz ()->list[list]:
    """
    Transpone una matriz
    pre:no parametros
    post: Retorna la nueva matriz
    """
    matriz = [[3,2,4],
              [2,4,13],
              [4,12,99]]
    for i, fila in enumerate(matriz): #i = indice fila
        for ic, e in enumerate(fila): #indice columna, e = elemento(no lo uso)
            if ic > i: #solo intercambia una vez
             matriz[i][ic], matriz[ic][i] = matriz[ic][i], matriz[i][ic]
    return matriz


def columnas_capicuas()->list[int]:
    """
    Revisa que columnas son capicuas.
    pre:No parametros
    post: Retorna una lista con las columnas capicua
    """
    listas_capicua = []
    matriz = [[3,2,3],
              [2,4,12],
              [3,12,99]]
    for i,l in enumerate(matriz):
        lista_a_evaluar = []
        for i2, e in enumerate(l):
            lista_a_evaluar.append(matriz[i][i2])
        if lista_a_evaluar == lista_a_evaluar[::-1]:
            listas_capicua.append(lista_a_evaluar)
    return listas_capicua

    
def simetrica_diagonal_principal()->bool:
    """
    Evalua si la diagonal principal es simetrica.
    pre: No parametros
    post: Retorna True si la  diagonal principal es simetrica. Caso contario,False.
    """
    matriz = [[3,2,3],
              [2,4,12],
              [3,12,2]]
    lista_diagonal = []
    for i,l in enumerate(matriz):
        for i2, c in enumerate(l):
            lista_diagonal.append(matriz[i][i])
            break #solo apendeo uno, despues CAMBIO de fila, primero matriz[0][0], despues matriz[1][1]
    return lista_diagonal == lista_diagonal[::-1]
        
def simetrica_diagonal_secundaria()->bool:
    """
    Evalua si la diagonal secundaria es simetrica.
    pre: No parametros
    post: Retorna True si la  diagonal secundaria es simetrica. Caso contario,False.
    """
    matriz = [[3,2,3],
              [2,4,12],
              [3,12,2]]
    lista_diagonal_secundaria = []
    for i,l in enumerate(matriz):
        for i2, c in enumerate(l):
            lista_diagonal_secundaria.append(matriz[i][-i - 1])#-i solo no funciona por que sino en la primera iteracion es - 0(tiene que ser -1)
            break
    return lista_diagonal_secundaria == lista_diagonal_secundaria[::-1]
        




def main()->None:
    """
    Menu principal para invocar otras funciones.
    
    """
    while True:
        op = int(input("Seleccione una opcion(0 para salir):"))
        if op == 0:
            break
        elif op == 1:
            print(cargar_numeros_enteros())
        elif op == 2:
            print(ordenar_forma_ascendente())
        elif op == 3:
            print(intercambiar_filas())
        elif op == 4:
            calcular_promedio_fila()
        elif op == 5:
            print(impares_por_columna())
        elif op == 6:
            print(transponer_matriz())
        elif op == 7:
            print(columnas_capicuas())
        elif op == 8:
            print(simetrica_diagonal_principal())
        elif op == 9:
            print(simetrica_diagonal_secundaria())
main()