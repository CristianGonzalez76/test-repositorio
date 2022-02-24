
while True:

    n1 = int(input("Primer Nota:  "))
    n2 = int(input("Segunda Nota:  "))
    n3 = int(input("Tercer Nota:  "))

    x1 = (n1+n2+n3)/3

    if x1 >= 60:
        print("Aprobado")
        print("El promedio es igual a:  ", x1)

    elif x1 < 60:
        print("Reprobado")
        print("El promedio es igual a:  ", x1)