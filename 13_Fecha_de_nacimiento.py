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
    1) Introducir Fecha
    2) Ver historial""")

    nn1 = int(input("Seleccione un opcion"))

    if nn1==1:
        n1 = int(input("En que año nacío:  "))
        file = open("13.txt","w")
        file.write("Nacio en el año:  " + str(n1) + os.linesep)
        r1 = 0
        # el ultimo año bisiesto fue en 2020 y sucede cada 4 años

        if n1%4==0:
            print("Usted Nacio en un año bisiesto")
            file.write("Usted nacio en un año bisiesto." + os.linesep)
            r1 = "Nacio en un Año bisiesto"

        else:
            print("Usted Nacion en un año no bisiesto")
            file.write("Usted nacio en un año no bisiesto." + os.linesep)
            r1 = "Nacio en un Año no bisiesto"
        
        print("")
        file.close()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P13:Año_bisiesto", r1))
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
