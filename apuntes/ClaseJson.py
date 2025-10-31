#numeros = [x for x in range(1,11)]
#letras = list("abcdefghijklmnñopqrstuvwxyz")
import json
#juntar_en_pares = [(letra,num % len(numeros))for num,letra in enumerate(letras)]
mi_dicc = {
            "Nombre": "santi",
            "Direccion": "Vulcano",
            "Edad": 18 
            }

 #obtengo keys
print(mi_dicc.keys)

#obtengo values
print(mi_dicc.values)

for k,v in mi_dicc.items():
    print(f"clave:{k},valor:{v}")

#si quiero consultar una clave:
print(mi_dicc.get("nombre".title(),[])) #evita errores retornando una lista vacia. le pongo un tittle para que coincida la mayuscula


cliente = {
    'nombre': 'Nora',
    "edad": 56,
    1: "45355",
    "color_ojos": "verdes",
    "usa_lentes": False,
    "lenguajes": ("Spanish", "English"),
}

# DUMPS - Obtener una cadena de caracteres JSON
# de Dict python a JSON
# Lee el diccionario cliente, lo indenta a 4 espacios y establece los separadores
"""
cliente_JSON = json.dumps(cliente, indent=4, separators=(", ", " : "))
"""
# @title Armando el JSON desde un CSV
import json

def csv_to_json(nombre_archivo: str) -> str:
    """
    Lee un archivo csv y retorna en forma de JSON de listas
    """
    salida = ""
    try:
        with open(nombre_archivo, "rt", encoding="utf-8-sig") as archivo:
            encabezado = archivo.readline().strip().split(",") #primera linea(str) en una lista separada por comas
            lineas = archivo.readlines() #se arma una lista, cada elemento en un renglon. TODAS MENOS LA PRIMERA .
    except Exception as e:
        print(f"Error: {e}")
    else:
        lista_alumnos = []
       
        for linea in lineas: 
            campos = linea.strip().split(",")
            dict_alu = {}
            for e, campo in zip(encabezado, campos):
                dict_alu[e] = campo
            # Forma de diccionario por comprensión
            # dict_alu = {e:campo for e, campo in zip(encabezado, campos)}
            lista_alumnos.append(dict_alu)

        salida = json.dumps(lista_alumnos, indent=4, ensure_ascii=False) 

    return salida

lista_alumnos = csv_to_json("/content/datos_alumnos.csv")

if lista_alumnos:
    print(type(lista_alumnos))
    print(lista_alumnos)
#<class 'str'>
#SE PRINTEARIA ESTO. TODAVIA NO ESTA EN EL JSON, ES SOLO LA ESTRUCTURA.
#[
"""
diccionario =  {
        "Legajo": "4366",
        "DNI": "41931388",
        "Nombre": "Valentina ",
        "Apellido": "Flores",
        "Edad": "20",
        "Nacionalidad": "Bangladesh",
        "Carrera": "Contabilidad",
        "Matemáticas": "2",
        "Ciencias": "3",
        "Lenguaje": "10"
    },
    {
        "Legajo": "6113",
        "DNI": "32431802",
        "Nombre": "Malena",
        "Apellido": "Castillo",
        "Edad": "30",
        "Nacionalidad": "Croacia",
        "Carrera": "Derecho",
        "Matemáticas": "5",
        "Ciencias": "10",
        "Lenguaje": "10"
    },
    {
        "Legajo": "836",
        "DNI": "30395814",
        "Nombre": "Catalina",
        "Apellido": "Martinez",
        "Edad": "23",
        "Nacionalidad": "Gambia",
        "Carrera": "Medicina",
        "Matemáticas": "10",
        "Ciencias": "5",
        "Lenguaje": "4"
    }
"""
#subir el diccionario a un json.
#try:
    #with open("datos.json","wt", enconding = "utf-8") as archivo_json:
        #json.dump

