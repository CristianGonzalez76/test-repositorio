
while True:

    n1 = int(input("En que año nacío:  "))

    # el ultimo año bisiesto fue en 2020 y sucede cada 4 años

    if n1%4==0:
        print("Usted Nacio en un año bisiesto")

    else:
        print("Usted Nacion en un año no bisiesto")
    
    print("")