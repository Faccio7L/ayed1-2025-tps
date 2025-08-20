import random as rn

def cant_camiones(peso:int) -> int:
    """
    cuenta la cantidad de camiones que tienen que salir.
    pre: recibe como parametro el peso de las naranjas.
    post: retorna la cantidad de camiones que tienen que salir.
    """
    capacidad_max = 500000 # esto esta en gramos como el peso de las naranjas!!! 
    capacidad_min = 400000 
    camiones = peso // capacidad_max
    sobrante = peso % capacidad_max #para ver si usamos un camion mas.
    if sobrante >= capacidad_min: 
        camiones += 1
    return camiones


def cajones_naranjas(naranjas:int) -> int:
    """
    cuenta la cantidad de cajones, naranjas y naranjas para jugo.
    pre: recibe como parametro la cantidad de naranjas.
    post: retorna la cantidad de cajones, camiones, resto y naranjas para jugo. 
    """
    naranjas_para_jugo = 0
    peso_naranja_total = 0
    cant_naranjas = 0
    cant_cajones = 0
    for x in range(naranjas):
        peso_naranja = rn.randint(150,350)
        if peso_naranja >= 200 and peso_naranja <= 300:
            cant_naranjas += 1
            peso_naranja_total += peso_naranja
            if cant_naranjas == 100:
                cant_naranjas = 0
                cant_cajones += 1
        else:
            naranjas_para_jugo += 1
    resto = cant_naranjas % 100 #lo que sobra de las naranjas.
    camiones = cant_camiones(peso_naranja_total)
    cajones = cant_cajones
    return cajones, camiones, resto, naranjas_para_jugo
            
def validar_naranjas(naranjas:int)-> bool:
    """
    verifica que se ingrese una cantidad positiva de naranjas.
    pre: Recibe como parametro la cantidad de naranjas.
    post: Retorna True en caso de que la cantidad de naranjas sea positiva. Caso contrario, False.
    """
    return naranjas >= 1


def main()->None:
    """
    Se ingresa una cantidad de naranjas cosechadas y notifica la informacion que la misma cosecha conlleva.
    pre: no recibe parametros.
    post: Printea la cantidad de naranjas sobrantes, cajas llenadas, naranjas utilizadas para jugo y cantidad de camiones utilizados.
    """
    cant_naranjas = int(input("Ingrese la cantidad de naranjas:"))
    if validar_naranjas(cant_naranjas):
        calculos = cajones_naranjas(cant_naranjas)
    print(f"Sobran un total de {calculos[2]} naranjas, se utilizan un total de {calculos[1]} camiones , se llenaron un total de {calculos[0]} cajones y {calculos[3]} son naranjas para jugo. ")
        

main()