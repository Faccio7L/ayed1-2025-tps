def separar_mail(mail:str)->tuple:
    """
    separa un mail por . y @, valida que tenga el formato valido!
    pre: Recibe un mail
    post: retorna una tupla con el usuario y el segundo elemento es una lista con las partrs separadas por .
    """
    valido = True
    if mail.count("@") != 1 or mail.count(".") not in [1,2]: #todos los mails creo que tienen 1 o 2 puntos y @.
        valido = False
    if  mail[-4::] == ".com" or mail[-7::] == ".com.ar":
        pass
    else:
        valido = False
    if not valido:
        return ()
    else:
        usuario,dominio = mail.split("@") #desempaqueto en dos variables asi que no queda lista.
        #print(usuario,dominio)
        partes_dom = dominio.split(".") #aca quedan listas del dom.
    return usuario, partes_dom

def main()->None:
    """
    Se ingresa un mail y se pasa como parametro para ver si tiene un formato valido.
    
    """
    mail = input("Ingrese un mail:")
    print(separar_mail(mail))
main()