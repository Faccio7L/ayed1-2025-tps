encabezado = ["nombre","legajo","fecha"]

empleados = [
      ["Juan Perez", "12345","15/03/1990"],
      ["Maria Garcia","54321", "22/07/1985"],
      ["Carlos Lopez", "67890", "10/11/1992"],
      ["Ana Martinez", "09876","05/01/1988"],
      ["Luis Rodriguez", "11223","30/09/1995"]  
]

#con un append y con una lista de comprension
salida = []
for fila in empleados:
    datos_de_empleado = [tupla  for tupla in zip(encabezado,fila)]
    salida.append(datos_de_empleado)
#print(salida)

#solo append
for fila in empleados:
    datos_de_empleado = []
    for tupla in zip(encabezado,fila):
        datos_de_empleado.append(tupla)
    salida.append(datos_de_empleado)
#print(salida)

#solo listas por comprension
salida = []
for empleado in empleados:
    datos_de_empleado = [[tupla for tupla in zip(encabezado,empleado)]for empleado in empleados if int(empleado[1]) > 20000 and empleado[0].upper().startswith("M")]
    
print(datos_de_empleado)

#EJERCICIO DE MATRIZ(concepto): MUCHOS FOR/WHILE QUE COMPLETEN 0, SI NO HAY 0 BREAK. FOR SIN RANGE.
#WHILE nro <= n**2:
#quizas un while true principal(if nro <= n**2 break) y un par de while true para completar abajo

#matriz[1][0] = n**2 -(n-2)**2
print(type((5)))