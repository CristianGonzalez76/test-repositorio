
while True:

    n1 = int(input("Cual es el modelo del vehiculo?  "))
    n2 = int(input("Cuantos Kilometros tiene recorridos el vehiculos?  "))

    if (n1 < 2007) & (n2 > 20000):
        print("El vehiculo debe renovarse")

    elif (2007 <= n1 <= 2013 ) & (n2 > 20000):
        print("El vehiculo debe recibir mantenimiento")

    elif (n1 > 2013) & ( n2 < 10000):
        print("El vehiculo esta en optimas condiciones")

    else:
        print("Mecánico")
    
    print("")