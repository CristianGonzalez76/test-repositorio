from re import I


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

    print("""
    1) Calcular la lista de numeros del mayor al menor
    2) Ver historial""")

    nn1= int(input("Seleccione una opcion"))

    if nn1==1:
        n1 = int(input("Primer Valor"))
        file = open('4.txt', 'w')
        file.write("El primer valor es: " + str(n1) + os.linesep)
        n2 = int(input("Segundo Valor"))
        file.write("El segundo valor es: " + str(n2) + os.linesep)


        print("Ingreso los valores", n1, "y", n2)

        if n1 > n2:
            n1 = n1+1
            print("Resultado")
            file.write("Resultado: " + os.linesep)
            for i in range(n2,n1):
                n1 = n1-1
                print(n1, end=" ")
                file.write(str(n1)+ " ")
            print("")



        elif n2 > n1:
            n2 = n2+1
            print("Resultado")
            file.write("Resultado: " + os.linesep)
            for n in range(n1, n2):
                n2 = n2-1
                print(n2, end=" ")
                file.write(str(n2) + " ")
            print("")

        file.close()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P4:Mayor a Menor", "---"))
        conexion.commit()
        cursor.close()
        conexion.close()


    elif nn1 == 2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM tarea_preparatoria;"
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()