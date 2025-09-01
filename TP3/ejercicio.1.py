def cargar_numeros_enteros():
    N = int(input("Ingrese el tamaño de la matriz:"))
    matriz = []
    for f in range(N): #fila
        fila = [] 
        for c in range(N): #columna
            num = int(input("Ingrese el valor que desea appendear:"))
            fila.append(num)   
        matriz.append(fila)
    return matriz

def ordenar_forma_ascendente():
    matriz =[[1,4,12],
            [53,22,13],
            [33,22,14] 
                    ]
    for f in matriz:
        f.sort() #le paso la lista sub 0,1,2 etc.
    return matriz
def intercambiar_filas(num_1:int = 1,num_2:int = 2):
    matriz = [[3,2,4,2],
              [2,4,12],
              [4,12,99]]
    matriz[num_1],matriz[num_2] = matriz[num_2], matriz[num_1] #si intercambio uno por uno, tendria que trabajar con una aux. Mejor asi.
    return matriz
    
def calcular_promedio_fila(fila:int = 2):
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

def impares_por_columna(columna:int = 2):
    lista_impares_columna = []
    matriz = [[3,2,4],
              [2,4,13],
              [4,12,99]]
    for fila in matriz:
        if fila[columna] % 2 != 0:
            lista_impares_columna.append(fila[columna])
    return lista_impares_columna

def transponer_matriz ():
    matriz = [[3,2,4],
              [2,4,13],
              [4,12,99]]
    for i, fila in enumerate(matriz): #i = indice fila
        for ic, e in enumerate(fila): #indice columna, e = elemento(no lo uso)
            if ic > i: #solo intercambia una vez
             matriz[i][ic], matriz[ic][i] = matriz[ic][i], matriz[i][ic]
    return matriz


def columnas_capicuas():
    pass
    matriz = [[3,2,4],
              [2,4,12],
              [4,12,99]]
    
    
        




def main():
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
main()