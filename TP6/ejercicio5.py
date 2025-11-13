def pasar_a_csv_1() ->None:
    """
    Convierte el archivo con info de los empleados en un csv

    """
    with open("texto5.txt","rt", encoding="utf-8") as r:
        while True:
            linea = r.readline()
            if not linea:
                break
            else:
                separador = ","
                with open("texto5.csv","a+t",encoding="utf-8") as csv:
                        nombre = linea[:17].strip()
                        fecha = linea[18:26].strip()
                        domicilio = linea[27:].strip()
                        csv.write(f"{nombre}{separador}{fecha}{separador}{domicilio}\n")


pasar_a_csv_1()

def pasar_a_dos_cifras(lista:list[int])->None:
    """
    Valida y modifica una lista para comprobar que los numeros sean de dos cifras.
    """

    for num in lista:
        if num < 10:
            lugar = lista.index(num)
            num = str(num) #no se usa para calculos, se puede castear
            num =f"0{num}"
            lista[lugar] = num

def pasar_a_csv_2() ->None:
    """
    Convierte el archivo con info de los empleados en un csv, se contempla el largo
    de cada campo.

    """
    with open("texto5.txt","rt", encoding="utf-8") as r:
        while True:
            linea = r.readline()
            if not linea:
                break
            else:
                apellido_nombre = linea[0:15].strip()
                fecha = linea[15:25].strip()
                domicilio = linea[25:].strip()
                n1 = len(apellido_nombre)
                n2 = len(fecha)
                n3 = len(domicilio)
                lista = [n1,n2,n3]
                pasar_a_dos_cifras(lista)

                #separador = ","
                with open("texto5v2.csv","a+t",encoding="utf-8") as csv:
                    csv.write(f"{lista[0]}{apellido_nombre}{lista[1]}{fecha}{lista[2]}{domicilio}\n")
                    
pasar_a_csv_2()