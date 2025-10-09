def separar_mail(mail:str)->tuple:
    """
    separa un mail por . y @, valida que tenga el formato valido!
    pre: Recibe un mail
    post: retorna una tupla con el usuario y el segundo elemento es una lista con las partrs separadas por .
    """
    if mail.count("@") != 1 or mail.count(".") != 2: #todos los mails creo que tienen 2 puntos y un @.
        return ()
    else:
        usuario,dominio = mail.split("@") #hago lista y desempaqueto en 2 variables
        #print(usuario,dominio)
        partes_dom = dominio.split(".")
    return usuario,partes_dom

    
def main()->None:
    """
    se ingresa un mail y se invoca la funcion separar mail.
    pre:no.
    post:no.
    """
    mail = input("Ingrese una direccion de mail:")
    print(separar_mail(mail))
main()