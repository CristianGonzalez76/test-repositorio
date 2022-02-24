
from math import pi
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

    print("""
    1) Usar calculadora geometrica
    2) ver historial""")

    nn1= int(input("Seleccione una opcion:  "))

    if nn1==1:
        print("Selecione la figura, de la cual quiere calcular su area:")
        print("""
        1) Circulo
        2) Cuadrado
        3) Triangulo
        4) Rectangulo
        """)

        n1 = int(input("Seleccione su opcion:  "))
        Area = 0
        file = open("9.txt","w")
        if n1 == 1:
            file.write("Figura seleccinada: Circulo" + os.linesep)
            rad = int(input("Radio del circulo  "))
            Area = (pi*rad*rad)
            print("El area calculada es igual a:", Area)
            file.write("El resultado es: " + str(Area) + os.linesep)

        elif n1 == 2:
            file.write("Figura seleccionada: Cuadrado" + os.linesep)
            a = int(input("Longitud de uno de los lados del cuadrado"))
            Area = (a*a)
            print("El area calculada es igual a:", Area)
            file.write("El resultado es: " + str(Area) + os.linesep)
        
        elif n1 == 3:
            file.write("Figura seleccionada: triangulo" + os.linesep)
            a = int(input("Base del triangulo"))
            b = int(input("Altura del trinangulo"))
            Area = (1/2)*(a*b)
            print("El area calculada es igual a:", Area)
            file.write("El resultado es: " + str(Area) + os.linesep)

        elif n1 == 4:
            file.write("Figura seleccionada: Rectangulo" + os.linesep )
            a = int(input("Base del rectangulo"))
            b = int(input("Altura del rectangulo"))
            Area = a*b
            print("El area calculada es igual a:", Area)
            file.write("El resultado es: " + str(Area) + os.linesep)
        
        file.close()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P9:Calcu_geometrica", Area))
        conexion.commit()
        cursor.close()
        conexion.close()
        file.close()
    

    elif nn1==2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM tarea_preparatoria;"
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()

