def patron_a(matriz:list[list])->list[list]:
    """
    Carga una matriz en un patron especificado.
    pre: No recibe parametros
    post: Retorna la matriz 
    """
    num = 1
    indice = 0 
    for f in matriz:
        for c in (f):
            f[indice] = num
            num += 2
            indice += 1 #no trabajo con el indice de elemento por que sino siempre es [0] antes del break!
            break
    return matriz

def patron_b(matriz:list)->list[list]:
    """
    Carga una matriz en un patron especificado.
    pre: No recibe parametros
    post: Retorna la matriz 
    """
    numero_a_elevar = len(matriz)
    num = 3 ** (numero_a_elevar  -1)
    print(num)
    for i, f in enumerate(matriz):
          for i2, e in enumerate(f):
             if i2 == i:
                f[-i2 - 1] = num 
                numero_a_elevar -= 1
                num = 3 ** (numero_a_elevar  -1)
                break
    return matriz

def patron_c(matriz:list)->list[list]:
    """
    Carga una matriz en un patron especificado.
    pre: No recibe parametros
    post: Retorna la matriz 
    """
    antes_del_break = 0
    num_inicial = len(matriz) + 1
    for i, f in enumerate(matriz):
          num_inicial -= 1
          for i2, e in enumerate(f):
            matriz[i][i2] = num_inicial
            if i2 == antes_del_break:
                antes_del_break += 1
                break

    return matriz
          
def patron_d(matriz:list)->list[list]:
    """
    Carga una matriz en un patron especificado.
    pre: No recibe parametros
    post: Retorna la matriz 
    """
    num_inicial = len(matriz) * 2
    
    
    for i, fila in enumerate(matriz):
        for i2,columna in enumerate(fila):
            fila[i2] = num_inicial
        num_inicial = num_inicial // 2
    return matriz
    
def patron_e(matriz:list)->list[list]:
    """
    Carga una matriz en un patron especificado.
    pre: No recibe parametros
    post: Retorna la matriz 
    """
   
    valor_inicial = 1
    for i,fila in enumerate(matriz):
        for i2,e in enumerate(fila):
            if i % 2 == 0: #para filas pares, appendeo en ELEMENTOS impares
                if i2 % 2 == 1:
                    matriz[i][i2] = valor_inicial
                    valor_inicial += 1
            else: #exactamente lo contrario!
                if i2 % 2 == 0:
                    matriz[i][i2] = valor_inicial
                    valor_inicial += 1
    return matriz
            
def patron_f(matriz:list)-> list[list]:
    """
    Carga una matriz en un patron especificado.
    pre: No recibe parametros
    post: Retorna la matriz 
    """
    valor_inicial = 1
    for i,f in enumerate(matriz):
        agregados = 0
        for i2,c in enumerate(f):
            matriz[i][-i2 - 1] = valor_inicial # indice negativo -1 por que -0 no existe, - 1 seria como 0 desde la derecha, -2 como 1,etc.
            agregados += 1
            valor_inicial += 1
            if  agregados == i + 1:
                 break
            

    return matriz

def patron_g(matriz,n) -> list[list]:
    """
    Esta funcion esta hardcodeada para un 4x4, 
    no encuentro un patron para trabajarlos bien.
    pre: Recibe como parametro una matriz
    post: retorna una matriz en forma de espiral
    #NOTAS CLASE CONSULTA: SI ES IMPAR TERMINA CENTRADO, SI ES PAR TERMINA EN ESPIRAL COMUN.
    """
    inicial = 1
    #largo = len(matriz)
    sub1_sub0 =  n**2 -(n-2)**2 #patron que encontramos en clase de consulta.
    for i,f in enumerate(matriz):
        for i2,c in enumerate(f):
            if i == 0: #la primera fila la completa con numeros consecutivos.
                matriz[i][i2] = inicial
                inicial += 1
            else: #ahora se completa para abajo.
                matriz[i][-1] = inicial 
                inicial += 1
                break #solo trabajo con el ultimo de cada fila.
    matriz[1][0] = sub1_sub0
    inicial = sub1_sub0 - 1 #ahora apendeamos para abajo.
    for i,f in enumerate(matriz):
        for i2,c in enumerate(f):
                if matriz[i][0] == 0:
                    matriz[i][0] = inicial
                    inicial -= 1
    for i,f in enumerate(matriz):
        for i2,c in enumerate(f):
            if matriz[-1][i2] == 0:
                matriz[-1][i2] = inicial
                inicial -= 1
    
#-----------------HASTA ACA SE COMPLETO TODA LA PARTE EXTERIOR DE CUALQUIER MATRIZ!!!--------------------
    inicial = sub1_sub0 + 1
    fila = 0
    derecha_abajo = True
    
    while True:
        fila += 1
        if fila > len(matriz):
            break
        if derecha_abajo == True:
            for i,f in enumerate(matriz):
                for i2,c in enumerate(f):
                    if matriz[fila][i2] == 0:
                        matriz[fila][i2] = inicial
                        inicial += 1
                        
                    if matriz[fila][-i2 -1 ] == 0:
                        matriz[fila][-i2 - 1] = inicial
                        inicial += 1
                        
            derecha_abajo = False
            if inicial > n**2:
                return matriz
        else:
            for i,f in enumerate(matriz):
                for i2,c in enumerate(f):
                    if matriz[fila][i2] == 0:
                        matriz[fila][-i2 -1 ] = inicial
                        inicial += 1
                        
                    if matriz[fila][i2] == 0:
                        matriz[fila][i2] = inicial
                        inicial += 1
                        

            derecha_abajo = True
            if inicial > n**2:
                return matriz

def patron_h(matriz):
    
    inicial = 4
    matriz[0][0] = 1
    matriz[0][1] = 2
    matriz[1][0] = 3
    for i,fila in enumerate(matriz):
        for i2, c in enumerate(fila):
            if c == 0:
                matriz[i][i2] = inicial
                inicial += 1
                break
            else:
                continue
    return matriz
    

        
def main():
    """
    Se crea una matriz con las dimensiones solicitadas por el usuario.
    pre: No recibe parametros
    post: Muestra en pantalla algun patron, podria modificarse para que muestre todas pero no lo considere necesario!!
    """
    tamaño = int(input("Ingrese el tamaño de la matriz:"))
    matriz = []
    for f in range(tamaño): #range por qeu es no iterable
        fila = []
        for c in range(tamaño):
            fila.append(0) #hasta aca son listas de 0!!
        matriz.append(fila) #aca ya son filas de la matriz!!!
    matriz_a_mostar = patron_h(matriz)
    for fila in matriz_a_mostar:
        print(fila)
main()