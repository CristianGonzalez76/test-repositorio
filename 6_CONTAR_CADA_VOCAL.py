from operator import le
from turtle import st
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
    1) Contar cada vocal de una palabra
    2) Ver el historial""")

    nn1 = int(input("Seleccione un opcion:  "))
    r1 = 0

    if nn1==1:
        pal1 = (input("Introduzca una palabra:  "))

        file=open("6.txt", "w")
        file.write("La palabra introducida es: " + pal1 + os.linesep)

        def contar_A(VOCAL_A):
            vocales1 = 'aáAÄÁ'

            return [c for c in VOCAL_A if c in vocales1]  #retornamos caracter por caracter y verificamos si estan incluidos en la lista vocales
        
        def contar_E(VOCAL_E):
            vocales2 = 'eéEËÉ'
            return[c for c in VOCAL_E if c in vocales2]

        def contar_I(VOCAL_I):
            vocales3 = 'iíIÍÏ'
            return[c for c in VOCAL_I if c in vocales3]

        def contar_O(VOCAL_O):
            vocales4 = 'oóOÓÖ'
            return[c for c in VOCAL_O if c in vocales4]

        def contar_U(VOCAL_U):
            vocales5 = 'uúUÚÜ'
            return[c for c in VOCAL_U if c in vocales5]

        print("La palabra tiene:")
        print("A= ", len(contar_A(pal1)))  
        print("E= ", len(contar_E(pal1)))
        print("I= ", len(contar_I(pal1)))
        print("O= ", len(contar_O(pal1)))
        print("U= ", len(contar_U(pal1)))

        file.write("La palabra tiene: " + os.linesep)
        file.write("A= " + str(len(contar_A(pal1))) + os.linesep)
        file.write("E= " + str(len(contar_E(pal1))) + os.linesep)
        file.write("I= " + str(len(contar_I(pal1))) + os.linesep)
        file.write("O= " + str(len(contar_O(pal1))) + os.linesep)
        file.write("U= " + str(len(contar_U(pal1))) + os.linesep)
        file.close()

        r1 = "A=", str(len(contar_A(pal1))), "E=", str(len(contar_E(pal1))), "I=", str(len(contar_I(pal1))), "O=", str(len(contar_O(pal1))), "U=", str(len(contar_U(pal1)))

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P6:Contar_c_vocal", r1))
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