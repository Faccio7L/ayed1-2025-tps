def filtrar_por_comprension(frase,n):
    frase_separada = frase.split() #lista por palabras
    filtrar = [palabra for palabra in frase_separada if len(palabra) >= n]
    return filtrar

def filtrar_con_filter(frase,n):
    frase = frase.split()
    #filtrar = (lambda frase,n: len(frase) >= n)
    
    
    print(list(filter(lambda frase: len(frase) >= n ,frase)))
    

def main():
    frase = input("Ingrese una frase:")
    n = int(input("Desee a partir de cuantos caracteres desea filtrar:"))
    print(filtrar_por_comprension(frase,n))
    print(filtrar_con_filter(frase,n))
main()