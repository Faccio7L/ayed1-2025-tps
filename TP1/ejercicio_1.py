def num_mayor(a:int,b:int, c:int) ->None: 
    """
    Evalua cual es el numero mayor y si se encuentra repetido.
    pre: Recibe 3 numeros enteros.
    post: Devuelve el numero mayor o, en caso de que el mismo se encuentre repetido, printea -1.
    """
    lista = [a,b,c]
    ordenada = sorted(lista)  
    if ordenada[-1] == ordenada[-2]: 
        print(-1)
    else:
        print(ordenada[-1])


def validar_valores(a:int,b:int,c:int) ->  bool:
    """""
    Valida que los numeros ingresados sean enteros
    pre:Recibe 3 numeros enteros.
    Post: retorna True en caso de que sean los 3 positivos, caso contrario retorna false.
    """""
    lista = [a,b,c]
    for x in lista:
        if x <= 0:
            return False
        else:
            return True
    #ABAJO OTRA FORMA QUE SE ME OCURRIO, pero la consigna pide sin and/or.
    #return a > 0 and b > 0 and c > 0 #retorna directamente True o False, como el ejemplo
                                      #de verificar horas (clase 1).
    
def main()->None:
    """
    Se ingresan 3 valores numericos
    pre:No recibe parametros
    Post: Luego de ser validados, invoca la funcion num_mayor.
    """
    print("A continuacion, ingrese 3 numeros mayores a 0.")
    num_1 = int(input("Ingrese el primer numero:"))
    num_2 = int(input("Ingrese el segundo numero:"))
    num_3 = int(input("Ingrese el ultimo numero:"))
    if validar_valores(num_1,num_2,num_3): #omito el True(diferencia de IaA)
        print("Valores validados correctamente.")
        num_mayor(num_1,num_2,num_3)
    else:
        print("Valores mal ingresados.")

main()
