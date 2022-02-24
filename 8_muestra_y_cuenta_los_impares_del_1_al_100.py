
from multiprocessing import Event
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
    1) Ejecutar operacion
    2) Ver historial""")

    nn1 = int(input("Seleccione una opcion:  "))
    if nn1==1:
        n1 = 0
        n2 = 100
        x1 = 0
        print("Los limites seleccionados son:", "[", n1,",", n2, "]")
        file = open("8.txt", "w")
        file.write("Los limites selecionados son:" + str(n1) + ", " + str(n2) + os.linesep)
        for i in range(n1,n2+1):
            if i%2==1:
                print(i, end=" ")
                x1 = x1 +1
                file.write(str(i) + " ")
        print("")
        file.write("" + os.linesep)
        print("La cantidad de numeros impares es: ")
        print(x1)
        file.write("La cantidad de numeros impares es: " + str(x1))
        file.close()

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P8:Cont_de_impares", x1))
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
