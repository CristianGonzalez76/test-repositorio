
from math import pi


while True:
    print("Selecione la figura, de la cual quiere calcular su area:")
    print("""
    1) Circulo
    2) Cuadrado
    3) Triangulo
    4) Rectangulo
    """)

    n1 = int(input("Seleccione su opcion:  "))
    Area = 0

    if n1 == 1:
        rad = int(input("Radio del circulo  "))
        Area = (pi*rad*rad)
        print("El area calculada es igual a:", Area)

    elif n1 == 2:
        a = int(input("Longitud de uno de los lados del cuadrado"))
        Area = (a*a)
        print("El area calculada es igual a:", Area)
    
    elif n1 == 3:
        a = int(input("Base del triangulo"))
        b = int(input("Altura del trinangulo"))
        Area = (1/2)*(a*b)
        print("El area calculada es igual a:", Area)

    elif n1 == 4:
        a = int(input("Base del rectangulo"))
        b = int(input("Altura del rectangulo"))
        Area = a*b
        print("El area calculada es igual a:", Area)

