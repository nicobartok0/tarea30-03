cantidad = float(input("Introduzca la cantidad a invertir"))
interes = float(input("Introduzca el interés anual"))
años = int(input("Introduzca los años a invertir"))
for i in range(años):
    cantidad *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))