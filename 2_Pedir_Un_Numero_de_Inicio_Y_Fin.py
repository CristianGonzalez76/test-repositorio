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
    1) Mostrar los numeros de 2 en 2 desde el numero de inicio hasta el final
    2) Ver el historial de la tabla""")

    nn1 = int(input("Seleccione una opcion:  "))
    r1 = 0
    
    if nn1 == 1:
        print("El valor inicial debe ser menor al valor final")
        n1 = int(input("Numero Inicial"))
        file = open('2.txt', 'w')
        file.write("Valor Inicial:  " + str(n1) + os.linesep)

        n2 = int(input("Numero Final"))
        file.write("Valor final:  " + str(n2) + os.linesep)

        if n1%2==0:
            for n in range(n1, n2+1,2):
                print(n, end=", "),
                file.write(str(n)+" ")
                r1 = str(n)+" "

        else:
            for n in range(n1,n2+1,2):
                print(n, end=", "),
                file.write(str(n))
                r1 = str(n)+ " "
        
            print("")
        print(r1)

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P2:Numeros de 2en2", r1))
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
