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
    1) Calcular los divisores de un numero
    2) Ver historial""")
    nn1 = int(input("Seleccione una opcion:  "))

    if nn1 == 1:
        n1 = int(input("Introduzca el valor"))
        file = open('3.txt', 'w')
        file.write('Valor introducido: ' + str(n1) + os.linesep)

        print("Los divisores del Numero son:")
        file.write("Los divisores del Numero son: " + os.linesep)
        for n in range(1,n1+1):
            if n1%n==0:
                print(n, end=", ")
                file.write(str(n) + " ")
        file.write("")
        
        print("")
        file.close()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P3:Divisordenumero", "---"))
        conexion.commit()
        cursor.close()
        conexion.close()

    elif nn1 ==2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM tarea_preparatoria;"
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()
    



