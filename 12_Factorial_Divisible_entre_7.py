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
    1) Factorial de un numero
    2) Ver historial""")
    nn1 = int(input("Seleccione una opcion:  "))

    if nn1==1:
        n1 = int(input("Ingrese un Valor"))
        file = open("12.txt","w")
        file.write("El valor ingresado es:  " + str(n1) + os.linesep)
        x1 = 0
        x2 = 1

        for i in range(0,n1):
                x1 = x1+1
                x2 = x2*x1
        
        if n1%7 == 0:
            print(x2)
            file.write("El resultado es: " + str(x2) + os.linesep)
        else:
            x2= "NO CUMPLE CON LO ESTABLECIDO"
            print("Error: El numero introducido no es divisible entre 7")
            file.write("Error: El numero introducido no es divisible entre 7")
        file.close()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P12:Factorial", x2))
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