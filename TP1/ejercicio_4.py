from typing import List
def pago(a:int,b:int)-> list:
    """
    Calcula cuantos billetes debe otorgar y valida
    pre:Recibe dos numeros enteros y positivos.
    post: Retorna la cantidad de billetes a devolver
    """
    
    valores = [5000, 1000, 500, 200, 100, 50, 10]  
    cantidades = []  


    vuelto = b - a
    for valor in valores:
        cantidad = vuelto // valor     
        vuelto = vuelto % valor        
        cantidades.append(cantidad)    
    return cantidades,valores

def main()-> None:
    """
    Se ingresa el monto que debe ser abonado y el dinero abonado.
    pre: No recibe parametros
    post: Muestra en pantalla cuando dinero se debe devolver.
    """
    
    total_a_pagar = int(input("Ingrese el monto a abonar:"))
    pagado = int(input("Ingrese el monto abonado:"))
    assert total_a_pagar > 0 and pagado > 0, "Debe ingresar un monto positivo"
    if pagado < total_a_pagar:
        print("Monto insuficiente.")
    elif pagado == total_a_pagar:
        print("Monto justo.")
    else:
        billetes,valores = pago(total_a_pagar,pagado) # lo almaceno en una variable para trabajar con la lista retornada!!!
        for b, v in zip(billetes,valores):
            print(f"El cajero debe devolver {b} billetes de ${v}")
    
main()

