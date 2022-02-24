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
    1) Sumar la suma de un numero desde 0 hasta n
    2) Ver el historial""")

    nn1 = int(input("Selecione una opcion: "))

    if nn1==1:
        n1 = int(input("Introduzca un numero:  "))
        file = open("7.txt","w")
        file.write("El numero introducido es: " + str(n1) + os.linesep)
        x1 = 0
        x2 = 0
        print("Ingreso el valor", n1)
        print("Debe sumar:", end="0" )
        for i in range(0,n1):
            x1 = x1+1
            x2 = x2+x1
            print(x1, end="  ")
        print("")
        print("El resultado de la Suma es:")
        print(x2)
        file.write("El resultado de la suma es: " + str(x2) + os.linesep)
        file.close()

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P7:Sumar_numero", x2))
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
