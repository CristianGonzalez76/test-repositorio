from tkinter.tix import TEXT
import psycopg2


while True:

    n1 = int(input("Primer Valor"))
    n2 = int(input("Segundo Valor"))
    n3 = int(input("Tercer Valor"))

    
    x1= 0
    x2= 0
    x3= 0
    
    if (n1 > n2) & (n1 > n3) & (n2 != n3):
            print("EL RESULTADO DE LA SUMA ES:")
            print(n1+n2+n3)
    
    elif (n2 > n1) & (n2 > n3) & (n1 != n3):
            print("EL RESULTADO DE LA MULTIPLICACION")
            print(n1*n2*n3)

    elif (n3 > n2) & (n3 > n1) & (n1 != n2):
            x1= n1
            x2= n2
            x3= n3
            print("EL NUMERO CONCATENADO ES")
            print(x1,x2,x3)

    elif (n1 == n3) & (n2 != n1) & (n2 != n3):
        print("El valor diferente es:")
        print(n2)
    elif (n1 == n2) & (n3 != n1) & (n3 != n2):
        print("El valor diferente es:")
        print(n3)
    elif (n3 == n2) & (n1 != n3) & (n1 != n2):
        print("El valor diferente es:")
        print(n1)
    elif (n1 == n2) & (n1 == n3) & (n2 == n3):
        print("Valor 1:",n1)
        print("Valor 2:",n2)
        print("Valor 3:",n3)
        print("Todos los numeros son iguales")

 