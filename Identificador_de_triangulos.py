
while True:

    print("Introduzca la longitud de los lados del triangulo")

    l1 = int(input("Lada A:  "))
    l2 = int(input("Lado B:  "))
    l3 = int(input("Lado C:  "))

    if (l1 == l2) & (l1 == l3) & (l2 == l3):
        print("El triangulo es:")
        print("Equilatero")

    elif (l1 != l2) & (l1 != l3) & (l2 != l3):
        print("El triangulo es:")
        print("Escaleno")
    
    elif [(l1 == l2) & (l3 != l1) & (l3 != l2)] or [(l1 == l3)&(l2 != l1)&(l2 !=l3)] or [( l2 == l3)&(l1 != l2)&(l1 !=l3)]:
        print("El triangulo es")
        print("Isosceles")

