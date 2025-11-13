NOMBRES = "nombres.txt"
from typing import Tuple

def clasificar_apellidos(nacionalidades: Tuple[str], apellido:str, nombre:str)->None:
    """
    Clasifica apellidos y almacena tanto el apellido con el nombre en un archivo txt con
    el nombre del pais.
    pre:Recibe una tupla de tuplas con una nacionalidad y terminacion de apellido esperada.
    """
    # with open(NOMBRES, 'rt', encoding='utf-8-sig') as nom:
    for nacionalidad in nacionalidades:
        if apellido.endswith(nacionalidad[1]):
            try:
                with open(f"{nacionalidad[0]}.txt", "at", encoding="utf-8") as na:
                    na.write(f"{apellido},{nombre}\n")
            except:
                print(f"Ocurrio un eror en {nacionalidad[0]}.txt")

def main()->None: 
    """
    Recorre las lineas de un archivo de nombres, identifica apellido y nombre e invoca
    a clasificar_apellidos para realizar su respectiva clasificacion.
    """
    try:
        with open(
            NOMBRES, "rt", encoding="utf-8-sig"
        ) as nom:  
            nacionalidades = (("ITALIA", "ini"), ("ESPANIA", "ez"), ("ARMENIA", "ian"))
            while True:
                linea = nom.readline()  # leer una linea a la vez.
                if not linea:  # si no encuentra una linea, termina
                    break
                linea = linea.split(",")
                apellido, nombre = linea[0], linea[1]
                clasificar_apellidos(nacionalidades, apellido, nombre)
    except Exception as e:
        print(f"Ocurrio un error:{e}")
main()
