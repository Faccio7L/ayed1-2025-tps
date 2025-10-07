def intercalar_listas(lista_1:list[int], lista_2:list[int])->list[int]:
    """
    Intercala listas
    pre: Recibe como parametro dos listas
    post: Retorna la lista intercalada.
    """
    indice_nuevo_num = 1
    for num in lista_2:
        lista_1[indice_nuevo_num:indice_nuevo_num:1] = [num]  #slice vacio, "empuja" al resto de elementos, sino sustituye.
        indice_nuevo_num += 2
    return lista_1

def main()->None:
    """
    Crea listas e invoca una funcion para intercalarlas.
    pre: no parametros
    post: muestra en pantalla el resultado de la "intercalacion"
    """
    lista_1 = [8,1,3,]
    lista_2 = [22,4,18,19]
    ver_mas_larga = (lambda x,y:  len(x) > len(y),lista_1,lista_2 )
    if ver_mas_larga:
        print(f"Las listas intercaladas son: {intercalar_listas(lista_2,lista_1)}")
    else:
         print(f"Las listas intercaladas son: {intercalar_listas(lista_1,lista_2)}")
main()