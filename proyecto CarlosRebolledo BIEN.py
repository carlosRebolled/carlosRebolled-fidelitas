'''
falta actualizar los comentarios de las lineas de codigo
Fecha: 20 abril 2024
Universidad Fidélitas
Carlos Rebolledo
Programación Básica
Christy Aguero
Proyecto

Instrucciones Paso 1

Debe introducir esos nombres: "Monestel" o "Rebolledo" # esta en la línea 253
Debe introducir la contraseña: "20" # esta en la línea 253
Después debe poner el número de la tarjeta que es: 12345678 # esta línea 256 y tarjeta() esta línea 88
Después debe poner el año de vencimiento. Solo debes poner 2024 o mayor que esa fecha. # esta línea 290 y 132
Después debe poner el número de CVV que es: 1234 # esta en la línea 292 y 147
En esa cuenta tiene 2 millones y 7 años de tiempo # esta la línea 294
Tiene varias opciones # esta la línea 68

Instrucciones Paso 2
Solo funciona para crear un nuevo usuario y guarda la información para poder llamar y mandar un correo después # esta en la línea 93 y 53
También para crear un archivo de txt dentro la computadora y lo leer

Instrucciones Paso 3
Debe introducir el CÓDIGO que le mandaron en el correo o cuando fue al banco. Es: 2585 # esta línea 247
Debe introducir cualquier nombre 
Debe introducir cualquier contraseña
Le van a dar la siguiente información en un print: número de Tarjeta 87654321, número de CVV 4321 
Se guarda en una lista

Después puedes volver y seleccionar opción 1 de ya tengo una cuenta
Debe introducir su nombre que puso anteriormente
Debe introducir su contraseña que puso anteriormente
Después debe poner el número de la tarjeta que es: "87654321" aparece también dentro el programa en un print # esta línea 302
Después debe poner el año de vencimiento. Solo debes poner 2024 o mayor que esa fecha. # esta línea 304
Después debe poner el número de CVV que es: 1234 # esta en la línea 306
En esa cuenta tiene 0 de saldo y 0 años de tiempo # esta la línea 307
Tiene varias opciones # esta la línea 68
'''


def inicioSesion():  # funcion para mover todo
    Cont=0
    nombre="1"
    contrasena="1"
    numTarjeta="1"      # para declarar las variables sin eso no funciona el programa
    numCvv="1"
    
    while Cont<=2:
        print("                  **Sistema del banco credoahorro**\n")

        print("Le damos la BIENVENIDA a nuestro banco\n")
        print("Recuerde que solo tiene TRES fallos antes que el sistema se bloquee\n")
        print("Ahora puedes hacer lo siguiente:\nDepositar a otra cuenta bancaria\nPuedes pedir una tarjeta de credito\nPuedes ahorra a largo plazo con interes a favor\nTambien puedes crear una nueva cuenta\n")
        usuario=input("Bienvenido a credoahorro por favor seleccione una opción:\n1 Si ya tienes una cuenta\n2 Para crear una nueva cuenta\n3 Si ya tiene código para crear una cuenta en línea\n4 Para cerrar el programa\n →")
        if usuario=="1":
            usuarioViejo(nombre,contrasena,numTarjeta,numCvv)
            Cont=Cont+3
        elif usuario=="2": # la segunda opcion del if de la linea 53
            newUsuario(usuario) # Funcion newUsuario(usuario) esta en la linea 93
            inicio=input("Por favor seleccione:\n1 Para volver al inicio \n2 Para cerrar el programa\n→")
            if inicio=="1":# para volver al inicio despues de crear un nuevo usuario
                Cont=0         
            else: #cerrar el programa despues de crear un nuevo usuario 
                Cont=Cont+3
        elif usuario=="3": # if de la linea 53
            nombre,contrasena,numTarjeta,numCvv =usuarioCreado (nombre,contrasena,numTarjeta,numCvv) # usuarioCreado (nombre,contrasena,numTarjeta,numCvv) esta funcion esta en la linea 247
        else: # if de la linea 53
            Cont=Cont+3

def opciones(usuario, saldo,tiempo):
    cont=0
    print("\n*************Bienvenido ",usuario," a credoahorro**************\n")
    while cont<=1:
        opcion=input("¿Qué opción desea realizar? \n1 Si desea depositar a una cuenta\n2 Para sacar una tarjeta de credito\n3 Para ahorros a largo plazo\n4 Para colsutar el saldo que tienes o ver sus ultimos movimientos\n5 Para salir del programa\n→")
        if opcion=="1":
            saldo=transferencia(usuario,saldo,tiempo) #transferencia(usuario,saldo) Funcion esta en la linea 166
            cont=cont+3   # se pone saldo=transferencia(usuario,saldo,tiempo) para que variable saldo se actualice cada vez que hace una transferencia

        elif opcion=="2":
            credito(usuario,saldo,tiempo) # Funcion esta en la linea 191
            cont=cont+3
         
        elif opcion=="3":
            ahorros(usuario,saldo,tiempo) # Funcion esta en la linea 212
            cont=cont+3

        elif opcion=="4":
            saldos(usuario,saldo,tiempo) # Funcion esta en la linea 235
            cont=cont+3

        else:
            cont=cont+3       

    
def newUsuario (usuario):
    cont=0
    if usuario=="2" : # validacion de datos de la linea 53
        while cont <=2:
            print("\n*************Sistema de creacion de una cuenta en credoahorro**************\n")
            newUsuario=input("introduzca su nombre completo:  ")
            telefono=input("introduzca su número telefónico solamente con teclado numérico:  ")
            correo=input("introduzca su correo: ")
            print("\nHola ",newUsuario," Gracias por confiar en nuestro banco\n")
            print("Sus datos son los siguientes:\nSu número telefónico es: ",telefono,"\nSu correo es: ",correo,"\n\n¿Estamos en lo correcto?\n")
            cont2=0
            while cont2 <=1:
                confimacion=input("Por favor seleccione:\n1 Para confirmar los datos anteriores\n2 Para volver atrás para corregir un dato\n→")
                if confimacion=="1":
                    file=open("datosUsuario.txt","w") 
                    file.write("Su nombre es: "+newUsuario+"\nSu correo es: "+correo+"\nSu teléfono es: "+telefono+"\n YA PRONTO LO LLAMAREMOS\n\n")
                    file.write("******Le damos la BIENVENIDA a nuestro banco credoahorro******\n\nAhora puedes hacer lo siguiente:\nDepositar a otra cuenta bancaria\nPuedes pedir una tarjeta de credito\nPuedes ahorra a largo plazo con interes a favor\nTambien puedes crear una nueva cuenta desde linea\n")
                    print("Ya tenemos sus datos pronto lo llamaremos para crear una cuenta y también le vamos a mandar un correo de toda la información de nuestro banco \n")
                    file.close()
                    file=open("datosUsuario.txt","r")
                    mensaje=file.read()
                    print(mensaje)
                    file.close()
                    cont=cont+3
                    cont2=cont2+2
                elif confimacion=="2":
                    cont2=cont2+2 #al usuario se le regresa a la linea 97
                else: # es un bucle infinito hasta que marque una opcion correcta if linea106 
                    print("Marcó una opción que NO EXISTE, por favor marque solamente el NÚMERO por ejemplo: 1\n\n")
def tarjeta(numTarjeta,usuario):
    cont=0
    while cont<=2:
        ValidarNumTarjeta=input("¿Cuál es su número de tarjeta?\n→")
        if  usuario=="Monestel" and "12345678"==ValidarNumTarjeta or usuario=="Rebolledo" and "12345678"==ValidarNumTarjeta:
            print("Tarjeta aceptada")
            cont=cont+3
        elif numTarjeta==ValidarNumTarjeta and numTarjeta != "1":# numTarjeta != "1" es importante porque al principio puse numTarjeta = "1" eso funciona para que no pueda acceder poniendo 1
            print("Tarjeta aceptada")
            cont=cont+3
        else:
            if cont<2:
                print("Intente nuevamente")
            else:
                print("El sistema se ha bloqueado, intente más tarde")
        cont=cont+1
    return ValidarNumTarjeta

def vencimiento():
    cont=0
    while cont<=2:
        vencimientoTarjeta=int(input("¿Cuál es el año de vencimiento de su tarjeta? \n→"))#si el usuario introduce un elemento string se cae el sistema
        if 2024<=vencimientoTarjeta:
            print("Su tarjeta está al día")
            cont=cont+3
        else:
            if cont<2:
                print("Intente nuevamente, su tarjeta está vencida\n")
            else:
                print("El sistema se ha bloqueado, intente más tarde")
        cont=cont+1
    return vencimientoTarjeta
        
def cvv(numCvv,usuario):
    cont=0
    while cont<=2:
        ValidaNumCvv=input("¿Cuál es su número de CVV?\n→")
        if usuario=="Monestel" and "1234"==ValidaNumCvv  or usuario=="Rebolledo" and "1234"==ValidaNumCvv  :
            print("CVV es correcto")
            cont=cont+3
            
        elif numCvv==ValidaNumCvv and numCvv != "1": #numCvv != "1" es importante porque al principio puse numCvv = "1" eso funciona para que no pueda acceder poniendo 1
            print("CVV es correcto")
            cont=cont+3
        else:
            if cont<2:
                print("\nintente nuevamente\n")
            else:
                print("El sistema se ha bloqueado, intente más tarde")
        cont=cont+1
    return ValidaNumCvv
listMoviento=[]
def transferencia(usuario,saldo,tiempo):
    cont=0
    while cont<=2:
        print ("Su saldo total es de: ",saldo) # saldo esta linea 287 y tambien esta 301
        dinero=int(input("\n¿Cuánto diniero desea transferir? →  ")) #si el usuario introduce un elemento string se cae el sistema
        cuentaTransferencia=int(input("Introduce el número de la cuenta que deseas depositar:\n→ "))
        print("¿Estás seguro de transferir ",dinero," a esa cuenta ",cuentaTransferencia," ?")
        confimar=input("\n1 Para confirma\n2 Para cancelar\n→")
        if confimar=="1":
            if saldo>=dinero:  # validar que tenga suficientes fondos para hacer una traferencia
                print("Transacción exitosa, fue enviado ",dinero, " a la cuenta de ",cuentaTransferencia)
                saldo=saldo-dinero
                listMoviento.append(dinero)
            else:
                print("Fondos insuficientes")      
        else:
            print("Su solicitud fue cancelada")      
        inicio=input("Por favor seleccione:\n1 Para volver al inicio \n2 Para cerrar el programa\n→")
        if inicio=="1":
            opciones(usuario, saldo,tiempo)
        else:
            cont=cont+5    
        cont=cont+5
    return saldo


def credito(usuario,saldo,tiempo):
    cont=0
    while cont<=2:
        confimar=input("¿Seguro que desea sacar una tarjeta de crédito?\n1 Para confirmar\n2 o otro número para cancelar\n→")
        if confimar=="1":
            if 5 <= tiempo:  # tiempo esta linea 288 y tambien esta 300
                print("Fue aprobada su tarjeta de crédito por favor pasar al banco más cercano")
            else:
                print("No cumples los requisitos para sacar una tarjeta de crédito")
        else:
            print("Su solicitud fue cancelada")
            
        inicio=input("Por favor seleccione:\n1 Para volver al inicio \n2 Para cerrar el programa\n")
        if inicio=="1":
            opciones(usuario,saldo,tiempo)
        else:
            cont=cont+5
        cont=cont+5
    return 


def ahorros(usuario,saldo,tiempo):
    dinero=int(input("Cuánto dinero puedes ganar ahorrando a largo plazo en nuestro banco \n→ "))#si el usuario introduce un elemento string se cae el sistema
    cont=0
    while cont<=1:
        planAhorro=input("Qué tipo de ahorro desea\n1 Para un ahorro del 5% por año\n2 Para un ahorro del 15% por dos años\n3 Para cancelar\n→ ")
        if planAhorro=="1":
            ganancia = dinero * 0.05
            print("Si ahorras ", dinero, " durante un año con un beneficio del 5% sería su ganancia ", ganancia, " y al final del año tendrías ",dinero+ganancia)

        elif planAhorro=="2":
            ganancia = dinero * 0.15
            print("Si ahorras ", dinero, " durante dos años con un beneficio del 15% sería su ganancia ", ganancia, "  y final de los dos años tendrías ",dinero+ganancia)

        else:
            cont=cont+2
            
        inicio=input("Por favor seleccione:\n1 Para volver al inicio \n2 Para cerrar el programa\n→")
        if inicio=="1":
            opciones(usuario,saldo,tiempo)
        else:
            cont=cont+5
        cont=cont+5
    return
def saldos (usuario,saldo,tiempo):
    cont=0
    while cont<=2:
        print("SU SALDO ES DE: ",saldo)
        print ("Sus últimos movimientos son de: ",listMoviento)
        inicio=input("Por favor seleccione:\n1 Para volver al inicio \n2 Para cerrar el programa\n→")
        if inicio=="1":
            opciones(usuario,saldo,tiempo)
        else:
            cont=cont+5
        cont=cont+5
    return 

def usuarioCreado (nombre,contrasena,numTarjeta,numCvv):
    cont=0
    while cont<=2:
        codigo=input("Por favor introduzca su código que le mandamos a su correo para poder crear una cuenta online: \n→ ")
        if codigo=="2585":
            nombre,contrasena,numTarjeta,numCvv=lista(nombre,contrasena,numTarjeta,numCvv)
            cont=cont+3
        else: # if linea 251
            print("Código Incorrecto inténtelo de nuevo\n")
            inicio=input("Por favor seleccione:\n1 Para volver a intentarlo \n2 Para volver menu principal\n→")
            if inicio=="1":
                cont=0
            else:
                cont=cont+3
    return nombre, contrasena,numTarjeta,numCvv
                
def usuarioViejo(nombre,contrasena,numTarjeta,numCvv):
    Cont=0
    while Cont<=2:
        usuario=input("Ingrese su apellido:\n→ ")
        clave=input("Ingrese la clave:\n→ ")
        Cont=Cont+1 # Eso funciona para que el usuario solamente tenga 3 intentos antes que cierre el programa linea 306
        if usuario=="Monestel" or usuario=="Rebolledo" and clave=="20": 
            print("Inicio de sesión exitosa") 
            ValidarNumTarjeta=tarjeta(numTarjeta,usuario) # Funcion tarjeta() esta en la linea 114 
            if "12345678"==ValidarNumTarjeta:
                vencimientoTarjeta = vencimiento()# Funcion vencimiento() esta en la linea 132 
                if 2024 <= vencimientoTarjeta:
                    ValidaNumCvv=cvv(numCvv,usuario) # Funcion cvv() esta en la linea 147
                    if "1234"==ValidaNumCvv:
                        saldo=2000000
                        tiempo=7
                        opciones(usuario,saldo,tiempo) # funcuion opciones(usuario,saldo,tiempo) esta la linea 68
                        Cont=Cont+3
            Cont=Cont+3                
        elif usuario==nombre and clave==contrasena and usuario!="1" :# usuario!= "1" es importante porque al principio puse nombre= "1" eso funciona para que no pueda acceder poniendo 1
            print("Inicio de sesión exitosa")
            ValidarNumTarjeta=tarjeta(numTarjeta,usuario) # Funcion tarjeta() esta en la linea 114 
            if numTarjeta==ValidarNumTarjeta:
                vencimientoTarjeta = vencimiento()# Funcion vencimiento() esta en la linea 132  
                if 2024 <= vencimientoTarjeta:
                    ValidaNumCvv=cvv(numCvv,usuario) # Funcion cvv() esta en la linea 147
                    if numCvv==ValidaNumCvv:
                        tiempo=0
                        saldo=0
                        opciones(usuario,saldo,tiempo)  # funcuion opciones(usuario,saldo,tiempo) esta la linea 68
                        Cont=Cont+3
            Cont=Cont+3                            
        else: # el if es de la linea 279
            if Cont<=2:
                print("\nIntente nuevamente\n")
            else:
                print("El sistema se ha bloqueado, intente más tarde")
                Cont=Cont+3
    return nombre, contrasena

listNewUsuario=[]
listNewpassword =[]
def lista(nombre,contrasena,numTarjeta,numCvv):
    for C in range (1):
        cont2=0
        cont=0
        while cont2<=2:
            nombre=input("Introduzca su nombre y un apellido: ")
            confimacion=input("Por favor seleccione:\n1 Para confimar su nombre\n2 Para volver atras para corregir su nombre\n→")
            if confimacion=="1":
                cont2=cont2+3
            elif confimacion=="2":
                cont2=0
        while cont<=2:
            contrasena=input("Introduzca su nueva cotraseña: ")
            confimacionContrasena= input("Introduzca otra vez su cotraseña para confimar: ")
            if contrasena==confimacionContrasena:
                numTarjeta="87654321"
                numCvv="4321"
                print("\nPor favor apunte los siguientes DATOS:\nSu número de tarjeta es: ",numTarjeta,"\nSu numero de Cvv es: ",numCvv,"\n")
                input("PRECIONE ENTER PARA SEGUIR")
                listNewUsuario.append(nombre)
                listNewpassword.append(contrasena)
                cont=cont+3
            else: #if linea 256
                print("\nNO coincide con la contraseña anterior inténtelo de nuevo\n")# es un bucle infinito hasta que ponga bien la contraseña         
    return nombre,contrasena,numTarjeta,numCvv
#Main
inicioSesion()



