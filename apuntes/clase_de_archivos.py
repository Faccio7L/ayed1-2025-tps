try:
    with open('alumnos.txt', 'wt', encoding='utf-8') as arch: #primero nombre de archivo, segundo "wt","rt","xt(no la vamos a usar.)"at"
        while True:                                            #W solo para crear archivo nuevo O PISA AL ANTERIOR. #R SOLO LEE. #A agrega informacion o CREA si no hay nada
            lu = input('LU (Enter para terminar): ')
            lu = lu.strip()
            if not lu:
                break
            else:
                if lu.isnumeric():
                    while True:
                        nombre = input('Nombre: ') #   santino faccio  
                        nombre = nombre.strip() #santino faccio
                        dato = nombre.split() # [santino,faccio]
                        dato = ''.join(dato) #santinofaccio
                        dato = dato.isalpha() #retorna True
                        # dato = ''.join(nombre.strip().split()).isalpha()
                        if dato:
                            arch.write(f'{lu},{nombre}\n')
                            break

except FileNotFoundError as msg:
    print(f'No se encuentra el archivo: {msg}')
except OSError as msg:
    print(f'No se puede grabar el archivo: {msg}')
else:
    print(f'Archivo creado correctamente')
finally:
    print(f'Todo terminado')


# Un ejemplo con csv, funciona igual pero hay que usar un separador.
separador = ';'
encabezado = f'legajo{separador}nombre\n'
primera = True
try:
    # Modo W crea el archivo y en caso de existir lo sobreescribe, borra los datos anteriores
    with open('alumnos.csv', 'wt', encoding='utf-8') as arch:
        while True:
            # Legajo Unico
            lu = input('LU (Enter para terminar): ')
            if not lu:
                break
            if not lu.isdigit():
                continue
            while True:
                nombre = input('Nombre: ')
                if nombre:
                    # Escritura de los datos con método write
                    # se hace en forma de string y se termina con escape n (\n) para tener salto de línea
                    if primera:
                        arch.write(encabezado)
                        primera = False
                    arch.write(f'{lu}{separador}{nombre}\n')
                    break

except FileNotFoundError as msg:
    print(f'No se encuentra el archivo: {msg}')
except OSError as msg:
    print(f'No se puede grabar el archivo: {msg}')
except:
    print('Error en los datos')
else:
    print(f'\nArchivo creado correctamente')


# Ejemplo 1 de lectura y cierre (Método: Readline). USAR SIG AL MOMENTO DE LA LECTURA. SIEMPRE!!!!!!!!!!!
separador = ';'
try:
    with open('/content/alumnos.csv', 'rt', encoding='utf-8-sig') as arch:
        linea = arch.readline() #leer una linea a la vez.
        print(linea)
        while True:
            # método readline (lectura línea por línea con control de final)
            linea = arch.readline() #retorna un string.
            if not linea:
                break
            lu, nombre = linea.rstrip().split(separador) #["123456","Alejandro"]
            if lu.isdigit() and int(lu) < 10_000_000: #primero veo si se puede castear, despues casteo
                print(f'LU: {lu:>7} - Nombre: {nombre}')

except FileNotFoundError as msg:
    print(f'No se encuentra el archivo: {msg}')
except OSError as msg:
    print(f'No se puede leer el archivo: {msg}')
except:
    print('Error en los datos')
else:
    print(f'\nArchivo leído correctamente')










