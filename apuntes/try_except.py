y = int(input("Ingrese el valor de y:"))
assert y != 0, "y no puede ser 0." #este es un msj para programadores, se puede pasar con un comando.
if y == 0:
    raise ValueError("No podes enviar un 0") #esto es para un cliente, 
#estructura de Try/Except:
try:
    print("TRATA de hacer lo que esta en este bloque.")
except ValueError:
    print("Aca va el except, arriba el error o los errores que queremos tomar. tmb puedo usar varios except si lo considero.")
else:
    print("ACA viene si no hay errores. es decir si paso el try.")
finally:
    print("ESTO SIEMPRE SE EJECUTA. no suele ser TAN util.")

#IMPORTANTEEEE!!!!!!!!!!!!!!!!!             
#except Exception as e: # para el final, en e se almacena el nombre de la variable y la puedo printear.
#python -O try_except.py para omitir los asserts.




#creo una clase.
class ErrorPorNumeroNegativo(Exception):
    "legajos si o si tienen que ser positivas."

#error creado.
def legajos_2():
    legajo = (int(input("Ingrese un numero de legajo:")))
    if legajo < 1:
        raise ErrorPorNumeroNegativo("El legajo tiene que ser positivo.")
    else:
        print("todo ok.")
legajos_2()

lista  = [3,2,3]
lista2 = lista[:] #forma muy facil de crear copias.

a = lista[::-1] == lista #ver si es capicua.
print(a)