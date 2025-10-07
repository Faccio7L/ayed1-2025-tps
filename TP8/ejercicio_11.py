def contar_vocales():
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    frase = input("Ingrese una frase:")
    frase = list(frase)
    for letra in frase:
        if letra == "a":
            a += 1
        elif letra == "e":
            e += 1
        elif letra == "i":
            i += 1
        elif letra == "o":
            o += 1
        elif letra == "u":
            u += 1
    print(frase)
    print(f"Hay un total de {a} A, {e} E,{i} I, {o} O, {u} U.")
contar_vocales()