

while True:

    n1 = int(input("Primer Valor"))
    n2 = int(input("Segundo Valor"))


    print("Ingreso los valores", n1, "y", n2)

    if n1 > n2:
        n1 = n1+1
        print("Resultado")
        for i in range(n2,n1):
            n1 = n1-1
            print(n1, end=" ")
        print("")



    elif n2 > n1:
        n2 = n2+1
        print("Resultado")
        for n in range(n1, n2):
            n2 = n2-1
            print(n2, end=" ")
        print("")