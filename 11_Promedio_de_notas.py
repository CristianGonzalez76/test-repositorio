

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
    1) Evaluar notas
    2) Ver historial""")

    nn1 = int(input("Seleccione una opcion: "))
    if nn1==1:

        n1 = int(input("Primer Nota:  "))
        n2 = int(input("Segunda Nota:  "))
        n3 = int(input("Tercer Nota:  "))
        file = open("11.txt","w")
        file.write("Primer Nota: " + str(n1) + os.linesep)
        file.write("Segunda Nota: " + str(n2) + os.linesep)
        file.write("Tercer Nota: " + str(n3) + os.linesep)
        x1 = (n1+n2+n3)/3

        if x1 >= 60:
            print("Aprobado")
            print("El promedio es igual a:  ", x1)
            file.write("Aprobado" + os.linesep)
            file.write("El promedio es igual a: " + str(x1) + os.linesep)

        elif x1 < 60:
            print("Reprobado")
            print("El promedio es igual a:  ", x1)
            file.write("Reprobado" + os.linesep)
            file.write("El promedio es igual a: " + str(x1) + os.linesep)

        file.close()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P11:Promedio_Notas", x1))
        conexion.commit()
        cursor.close()
        conexion.close()

    elif nn1==2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM tarea_preparatoria;"
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()