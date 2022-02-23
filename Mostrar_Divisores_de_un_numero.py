while True:
    n1 = int(input("Introduzca el valor"))
    
    print("Los divisores del Numero son:")
    for n in range(1,n1+1):
        if n1%n==0:
            print(n, end=", ")
    
    print("")
            


