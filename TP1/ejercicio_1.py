def num_mayor(a = 5, b = 7, c = 12): #valores default para testear.
    lista = [a,b,c]
    mayor = max(lista) #designo el valor mayor y lo almaceno aca.
    if lista.count(mayor) > 1: #cuento cuantas veces aparece el valor mayor.
        print(-1)
    else:
        print(mayor)


def validar_valores(a,b,c):
    lista = [a,b,c]
    for x in lista:
        if x <= 0:
            return False
        else:
            return True
    #ABAJO OTRA FORMA QUE SE ME OCURRIO, pero la consigna pide sin and/or.
    #return a > 0 and b > 0 and c > 0 #retorna directamente True o False, como el ejemplo
                                      #de verificar horas (clase 1).
    
def main():
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
