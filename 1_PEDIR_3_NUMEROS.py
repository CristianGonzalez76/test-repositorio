from tkinter.tix import TEXT
import psycopg2
import os





while True:

    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "12345abc",
        dbname = "Tarea_Preparatoria"
    )
    print("Conexion Realizada")

    #  file.write("Primera línea" + os.linesep)
    #  file.write("Segunda línea")

    print("""
    1) Introducir 3 valores enteros
    2) Ver Historail""")

    nn1 = int(input("Elija la operacion:  "))

    if nn1==1: 
        n1 = int(input("Primer Valor"))
        file = open('1.txt', 'w')
        file.write("Primer valor: " + str(n1) + os.linesep)

        n2 = int(input("Segundo Valor"))
        file.write('Segundo Valor: ' + str(n2) + os.linesep)


        n3 = int(input("Tercer Valor"))
        file.write('Tercer Valor: ' + str(n3) + os.linesep)
        

        x1= 0
        x2= 0
        x3= 0
        r1= 0
        
        if (n1 > n2) & (n1 > n3) & (n2 != n3):
                print("EL RESULTADO DE LA SUMA ES:")
                file.write('El Resultado de la suma es: ')
                print(n1+n2+n3)
                file.write(str(n1+n2+n3) + os.linesep)
                r1= n1+n2+n3
        
        elif (n2 > n1) & (n2 > n3) & (n1 != n3):
                print("EL RESULTADO DE LA MULTIPLICACION")
                file.write('El Resultado de la multiplicacion es: ')
                print(n1*n2*n3)
                file.write(str(n1*n2*n3) + os.linesep)
                r1 = n1*n2*n3

        elif (n3 > n2) & (n3 > n1) & (n1 != n2):
                x1= n1
                x2= n2
                x3= n3
                print("EL NUMERO CONCATENADO ES")
                file.write('El numero concatenado es: ')
                print(x1,x2,x3)
                file.write(str(x1) + str(x2) + str(x3) + os.linesep)
                r1 = (str(x1)+str(x2)+str(x3))

        elif (n1 == n3) & (n2 != n1) & (n2 != n3):
            print("El valor diferente es:")
            file.write('El valor diferente es: ')
            print(n2)
            file.write(str(n2) + os.linesep)
            r1 = n2
        elif (n1 == n2) & (n3 != n1) & (n3 != n2):
            print("El valor diferente es:")
            file.write('El valor diferente es: ')
            print(str(n3) + os.linesep)
            file.write(str(n3) + os.linesep)
            r1 = n3
        elif (n3 == n2) & (n1 != n3) & (n1 != n2):
            print("El valor diferente es:")
            file.write('El valor diferente es: ')
            print(str(n1) + os.linesep)
            file.write(str(n1) + os.linesep)
            r1 = n1
        elif (n1 == n2) & (n1 == n3) & (n2 == n3):
            print("Valor 1:",n1)
            print("Valor 2:",n2)
            print("Valor 3:",n3)
            print("Todos los numeros son iguales")
            file.write('Todos los numeros son iguales' + os.linesep)
            r1 = "Todos son iguales"

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P1: Pedir 3 Numeros", r1))
        conexion.commit()
        cursor.close()
        conexion.close()
        file.close()

    elif nn1 == 2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM tarea_preparatoria;"
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()

 