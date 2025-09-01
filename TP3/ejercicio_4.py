import random as rn
def matriz_random(cantidad:int)->list[list[int]]:
    """
    Carga una matriz con cantidad de fabricas y sus unidades vendidias dia a dia.
    pre: Recibe como parametro la cantidad de fabricas
    post: Retorna una lista de listas(matriz)
    """
    matriz = []
    for f in range(cantidad): 
        fila = []
        for c in range(6): #6 dias que se laburan
            fila.append(rn.randint(0,150))
        matriz.append(fila)
    return matriz
def fabricadas_por_fabrica(matriz:list[list]) -> list[int]:
    """
    Hace una lista con el total fabricado de cada fabrica.
    pre: Recibe como parametro la matriz.
    post: Retorna la lista de las ventas por dia.
    """
    lista_total = list()
    acumulador = 0
    for fila in matriz:
        acumulador = 0
        for num in fila:
            acumulador = acumulador + num
        lista_total.append(acumulador)
    return lista_total
        
def mayor_produccion(matriz:list[list]) -> list[int]:
    """
    busca el dia de mayor producccion.
    pre:Recibe como parametro la matriz.
    post: Retorna el maximo dia de ventas.
    """
    maximo_dia_ventas = 0
    indice = 0
    fila = 0
    for f in matriz:
        for c in f:
            maximo_por_dia = max(f)
            if maximo_por_dia > maximo_dia_ventas:
                maximo_dia_ventas = maximo_por_dia
                indice = f.index(maximo_dia_ventas) #para saber el dia de la semana
                fila = matriz.index(f) #consulto el indice de la fila ara saber que num de fabrica es

    return maximo_dia_ventas,indice,fila

def dia_mas_productivo(matriz:list[list]) -> int:
    """
    Averigua el dia mas productivo considerando todas las fabricas
    pre: Recibe como parametro una matriz
    post: Retorna el dia con mayor ventas
    """
    ventas = [0,0,0,0,0,0] #lunes, martes...
    

    for fila in matriz:
        for i, columna in enumerate(fila):  
            ventas[i] += columna #primero en el sub 0 agrega el primer valor, despues el primer valor del sub 1...etc y dsp se repite
    venta_maxima = max(ventas)    
    dia_venta_maxima = ventas.index(venta_maxima)
    return dia_venta_maxima

            
    
        
def lista_por_comprension(matriz:list[list])->list[int]:
    """
    Genera una lista por comprension con la menor cantidad de ventas por dia
    pre: Recibe como parametro una matriz.
    post: Retorna la lista por comprension.
    """
    lista = [min(x) for x in matriz]
    return lista

def main () ->None:
    """
    Funcion principal, invoca al ressto de funciones y muestra su retorno, en caso
    de tener varios retornos, las desempaqueta.
    pre: No hay parametros
    post: Muestra en pantalla lo retornado or otras funciones.
    """
    lista = []
    dias = ["lunes","martes","miercoles","jueves","viernes","sabado"]
    cantidad = int(input("Ingrese cuantas fabricas tiene:"))
    matriz = (matriz_random(cantidad))
    print(matriz)
    for i, c in enumerate(fabricadas_por_fabrica(matriz)):
        print(f"La fabrica {i+1} vendio un total de {c}")
    maximo_dia_ventas, indice, fila = mayor_produccion(matriz)
    print(f"El dia de mayor produccion fue {dias[indice]} y es la fabrica numero {fila +1}")
    dia = dia_mas_productivo(matriz)
    print(f"EL dia de mayor produccion es el dia {dias[dia]}")
    print(f"La menor cantidad fabricada por empresa es:{lista_por_comprension(matriz)}")
    

main()
    