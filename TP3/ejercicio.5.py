import random as rn
def mostrar_butacas(filas:int,columnas:int)->list[list]:
    """
    LLena una matriz con numeros random, indica si estan ocupados o no.
    Pre: Recibe como parametro las filas y columnas requeridas
    post: Retorna la matriz completa    
    """
    matriz = []
    for f in range(filas):
        fila = []
        for num in range(columnas):
            fila.append(rn.randint(0,1))
        matriz.append(fila)
    return matriz
def reservar(matriz)->list[list]:
    """
    Se le solicita al usuario un asiento para reservar
    pre: Recibe como parametro la Matriz de asientos.
    post: Retorna True en caso de que pueda reservarse(y obviamente se reserva )
    , caso contrario retorna False
    """
    contador = 0
    reserva = int(input("Elija un asiento, van desde la silla 1 hacia adelante(las que dicen 0 estan libres):"))
    for i, f in enumerate(matriz):
        for i2, c in enumerate(f):
            contador += 1
            if contador == reserva:
                silla = matriz[i][i2]
                if silla == 1:
                    return False
                else:
                    matriz[i][i2] = 1
                    return True
def butacas_libres(matriz:list[list])->list[list]:
    """
    Cuenta la cantidad de butacas libres
    pre: Recibe como parametro la matriz de asientos
    post: Retorna el contador de asientos libres
    """
    contador = 0
    for i, f in enumerate(matriz):
        for i2, c in enumerate(f):
            if matriz[i][i2] == 0:
                contador += 1
    return contador
def butacas_contiguas(matriz:list[list])->list[list]:
    """
    Busca el patron mas largo de asientos desocupados
    pre: Matriz de asientos
    post: Retorna el contador mas largo continuo y su fila.
    """
    contador_mas_largo = 0
    contador = 0
    for i, f in enumerate(matriz):
        for i2, c in enumerate(f):
            if matriz[i][i2] == 0:
                contador += 1
                if contador > contador_mas_largo:
                    contador_mas_largo = contador
                    fila = i #en que fila ocurre la secuencia mas larga
            else:
                contador = 0
    return contador_mas_largo, fila
            

def main()->None:
    """
    Invoca al resto de funciones, se solicita la cantidad de filas y butacas
    pre: No recibe parametros
    post: Muestra en pantalla el resultado de las invocaciones de las otras funciones.
    """
    filas = int(input("Ingrese la cantidad de filas del cine:"))
    butacas = int(input("Ingrese cuantas butacas tiiene cada fila:"))
    validacion_filas = (lambda x: x > 0)(filas)
    validacion_butacas = (lambda x: x > 0)(butacas)
    if validacion_butacas and validacion_filas:
        print("valores validos")
        matriz = mostrar_butacas(filas,butacas)
        print(matriz)
        if reservar(matriz):
            print("Asiento reservado!")
            print(matriz)
        else:
            print("Asiento vendido")
        print(f"La cantidad de butacas libres es de {butacas_libres(matriz)}")
        contador, fila = butacas_contiguas(matriz)
        print(f"La secuencia mas largas de butacas es de {contador} y ocurre en la fila {fila + 1}")
main()