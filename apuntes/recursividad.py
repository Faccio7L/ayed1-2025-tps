def suma_recursiva(n):
    # Paso Base: Si n es 1, la suma es 1. Esta es la condición que detiene la recursión.
    if n == 1:
        return 1

    # Paso Recursivo: Sumamos el número actual (n) con la suma de los números anteriores (n-1).
    else:   
        return n + suma_recursiva(n - 1)

# Calculamos la suma del 1 al 10
n = 999
resultado = suma_recursiva(n)
print(f"La suma de los números del 1 al {n} es: {resultado}")
#cualquier resolucion recursiva puede hacerse de manera iterativa(como veniamos viendo)
#y viceversa. 
#el limite de pila es 999!°!°!°!°!°!°!°!°!°!°!°
#HASTA EJERCICIO 5!!!!!!!!