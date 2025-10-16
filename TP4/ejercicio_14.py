def separar_mail(mail:str,dominios:set)->None:
    """
    separa un mail por . y @, valida que tenga el formato valido y ademas llena el set de dominios.
    pre: Recibe un mail y un set.
    """
    
    valido = True
    if mail.count("@") != 1 or mail.count(".") not in [1,2]: #todos los mails creo que tienen 1 o 2 puntos y @.
        valido = False
    if  mail[-4::] == ".com" or mail[-7::] == ".com.ar":
        pass #osea, valido sigue con el mismo valor
    else:
        valido = False #si no cambia/sigue en false.
    if not valido:
        return ()
    else:
        usuario,dominio = mail.split("@") #hago lista y desempaqueto en 2 variables
        #print(usuario,dominio)
        dominios.add(dominio)
        
    

def main()->None:
    """
    Solicita mails e invoca a la funcion separar_mail. almacena los dominios sin repetir
    con un set.
    
    """
    dominios = set()
    while True:
        mail = input("Ingrese un mail:").lower().strip()
        separar_mail(mail,dominios)
        if mail == "":
            break
    print(dominios)
main()