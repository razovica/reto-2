print ("ramon malo")
Cuenta = input ("Cantidad de usuarios Nuevos:  ")
Control1 = True
ok_correcto = True
#while ok_correcto:
while Control1:
    Nombre = input ("Nombre:  ")
    if len(Nombre) <= 5 or len(Nombre) >= 50:
        print("Nombre menos de 5 y mas 50")
    else:
        Control1= False

# Apellido
Control1 = True   
while Control1:
    Apellido = input ("Apellido:  ")
    if len(Apellido) <= 5 or len(Apellido) >= 50:
        print("Apellido menos de 5 y mas 50")
    else:
        Control1= False
# correo
Control1 = True   
while Control1:
    Correo = input ("Correo:  ")
    if len(Correo) <= 5 or len(Correo) >= 50:
        print("Correo menos de 5 y mas 50")
    else:
        Control1= False
# telefono
Control1 = True   
while Control1:
    Telefono = input ("Correo:  ")
    if len(Telefono) !=10:
        print("Telefono 10 digitos")
    else:
        Control1= False

    #else:
    #    ok_correcto = False           