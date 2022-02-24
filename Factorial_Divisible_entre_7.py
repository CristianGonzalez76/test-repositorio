
while True:

    n1 = int(input("Ingrese un Valor"))

    x1 = 0
    x2 = 1

    for i in range(0,n1):
            x1 = x1+1
            x2 = x2*x1
    
    if n1%7 == 0:
        print(x2)
    else:
        print("Error: El numero introducido no es divisible entre 7")