import random as rn
def juego():
    numero_a_adivinar = rn.randint(1,500)
    contador = 0
    while True:
        
        num = input("Ingrese un numero:")
        contador += 1
        try:
            num = int(num)
        except Exception as e:
            print("debe ser un numero entero.")
        else:
            if num < numero_a_adivinar:
                print("El numero que usted debe adivinar es mayor.")
            elif num > numero_a_adivinar:
                print("El numero que usted debe adivinar es menor.")
            else:
                print("¡Adivinaste!")
                print(f"Te llevo {contador} intentos")
                break
juego()