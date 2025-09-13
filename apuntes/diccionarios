from tabulate import tabulate
materias = {}

materias = {}
# materias = dict()

materias["lunes"] = [6103, 7540]

materias["martes"] = [6201]

materias["miércoles"] = [6103, 7540]

materias["jueves"] = [4152]

materias["viernes"] = [6201]
materias["lunes"].append(1234)

#print(materias["lunes"])

for clave, valor in materias.items():
    print(clave, valor[0])

#si el value no es una lista, no le puedo agregar nada. ej:
materias["Sabados"] = 3000
#materias["Sabados"].append(1000) esto tiraria error.
print(f"El diccionario tiene {len(materias)} elementos")
print(materias.get("lunes",[]))
print(materias.get("domingo"),[])

for dia in materias:
    print(f"El dia {dia} tengo que cursar {materias[dia]}")

ciudades = [{"cp":1425, "nombre":"CABA"},
 {"cp":1900, "nombre":"La Plata"}] #lista con 2 diccionarios.

print(f"Código postal La Plata: {ciudades[1]['cp']}")
ciudades.append({"cp":1878, "nombre":"quilmes"})
ciudades.append({"cp":7167, "nombre:":"Pinamar"})#clave valor,clave valor.
for clave, valor in enumerate(ciudades):  #uso enumereate en vez de items por que es UNA LISTA.
    print(f"{clave,valor}")

#ejercicio practica.
calendario = list(range(1,30))


contador = 0
mes = []
semana = []
for i, e in enumerate(calendario):
    contador += 1
    semana.append(e)
    if contador == 7:
        mes.append(semana)
        contador = 0
        semana = []
mes.append(semana)
print(tabulate(mes))

semanas = [calendario[i:i+7] for i in range(0,len(calendario),7)]


        

