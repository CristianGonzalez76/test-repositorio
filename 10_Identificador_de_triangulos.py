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
    1) Identificar triangulo
    2) Ver historial""")

    nn1 = int(input("Seleccione una opcion:  "))
    r1 = 0
    if nn1==1:
        print("Introduzca la longitud de los lados del triangulo")

        l1 = int(input("Lada A:  "))
        l2 = int(input("Lado B:  "))
        l3 = int(input("Lado C:  "))

        file = open("10.txt", "w")
        file.write("Los lados del triangulo son: " + " A=" + str(l1)+" B="+str(l2)+" C="+str(l3) + os.linesep)


        if (l1 == l2) & (l1 == l3) & (l2 == l3):
            print("El triangulo es:")
            print("Equilatero")
            file.write("El triangulo es: Equilatero")
            r1 = "Equilatero"


        elif (l1 != l2) & (l1 != l3) & (l2 != l3):
            print("El triangulo es:")
            print("Escaleno")
            file.write("El triangulo es: Escaleno")
            r1 = "Escaleno"

        
        elif [(l1 == l2) & (l3 != l1) & (l3 != l2)] or [(l1 == l3)&(l2 != l1)&(l2 !=l3)] or [( l2 == l3)&(l1 != l2)&(l1 !=l3)]:
            print("El triangulo es")
            print("Isosceles")
            file.write("El triangulo es Isosceles")
            r1 = "Isosceles"

        file.close()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P10:Id_triangulos", r1))
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

