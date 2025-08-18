from typing import Tuple
def pago(a:int,b:int)-> tuple:
    """
    Calcula cuantos billetes debe otorgar y valida
    pre:Recibe dos numeros enteros y positivos.
    post: Retorna la cantidad de billetes a devolver
    """
    billetes_10 = 0
    billetes_50 = 0
    billetes_100 = 0
    billetes_200 = 0
    billetes_500 = 0
    billetes_1000 = 0
    billetes_5000 = 0

    if a > b:
        print("El monto abonado no es suficiente.")
    elif a == b:
        print("No se debe dar vuelto.")
    else:
        vuelto = b - a
        while vuelto >= 5000:
            vuelto -= 5000
            billetes_5000 += 1
        while vuelto >= 1000:
            vuelto -= 1000
            billetes_1000 += 1
        while vuelto >= 500:
            vuelto -= 500
            billetes_500 += 1
        while vuelto >= 200:
            vuelto -= 200
            billetes_200 += 1
        while vuelto >= 100:
            vuelto -= 100
            billetes_100 += 1
        while vuelto >= 50:
            vuelto -= 50
            billetes_50 += 1
        while vuelto >= 10:
            vuelto -= 10
            billetes_10 += 1
        return billetes_5000,billetes_1000, billetes_500, billetes_200, billetes_100, billetes_50, billetes_10

def main()-> None:
    """
    Se ingresa el monto que debe ser abonado y el dinero abonado.
    pre: No recibe parametros
    post: Muestra en pantalla cuando dinero se debe devolver.
    """
    total_a_pagar = int(input("Ingrese el monto a abonar:"))
    pagado = int(input("Ingrese el monto abonado:"))
    assert total_a_pagar > 0 and pagado > 0, "Debe ingresar un monto positivo"
    billetes = pago(total_a_pagar,pagado) # lo almaceno en una variable para trabajar con la lista retornada!!!
    print(f"El cajero debe devolver {billetes[0]} billete/s de $5000")
    print(f"El cajero debe devolver {billetes[1]} billete/s de $1000")
    print(f"El cajero debe devolver {billetes[2]} billete/s de $500")
    print(f"El cajero debe devolver {billetes[3]} billete/s de $200 ")
    print(f"El cajero debe devolver {billetes[4]} billete/s de $100")
    print(f"El cajero debe devolver {billetes[5]} billete/s de $50")
    print(f"El cajero debe devolver {billetes[6]} billete/s de $10")
    
main()