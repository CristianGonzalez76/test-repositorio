
while True:
    print("El valor inicial debe ser menor al valor final")
    n1 = int(input("Numero Inicial"))
    n2 = int(input("Numero Final"))

    if n1%2==0:
        for n in range(n1, n2+1,2):
            print(n, end=", "),
    else:
        for n in range(n1,n2+1,2):
            print(n, end=", "),
    
    print("")
