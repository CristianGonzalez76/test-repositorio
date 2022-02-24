
while True:

    n1 = int(input("Introduzca un numero:  "))
    x1 = 0
    x2 = 0
    print("Ingreso el valor", n1)
    print("Debe sumar:", end="0" )
    for i in range(0,n1):
        x1 = x1+1
        x2 = x2+x1
        print(x1, end="  ")
    print("")
    print("El resultado de la Suma es:")
    print(x2)

