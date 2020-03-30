contra = input("Introduzca su contraseña: \t")
contra2 = input("Introduzca la contraseña para ingresar al sistema: \t")
while contra2 != contra:
    print ("intente de nuevo.")
    contra2 = input("Introduzca la contraseña para ingresar al sistema: \t")
if contra2 == contra:
    print ("Contraseña correcta.")