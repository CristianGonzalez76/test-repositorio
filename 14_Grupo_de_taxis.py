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
    1) Ejecutar Programa
    2) Ver el historial""")

    nn1= int(input("Seleccione un opcion:  "))

    if nn1==1:
        n1 = int(input("Cual es el modelo del vehiculo?  "))
        n2 = int(input("Cuantos Kilometros tiene recorridos el vehiculos?  "))
        file = open("14.txt","w")
        file.write("El vehiculo es modelo "+str(n1)+os.linesep)
        file.write("tiene recorridos "+str(n2)+"KM" + os.linesep)
        r1 = 0
        if (n1 < 2007) & (n2 > 20000):
            print("El vehiculo debe renovarse")
            file.write("El vehiculo debe renovarse"+os.linesep)
            r1 = "El vehiculo debe renovarse"

        elif (2007 <= n1 <= 2013 ) & (n2 > 20000):
            print("El vehiculo debe recibir mantenimiento")
            file.write("El vehiculo debe recibir mantenimiento"+os.linesep)
            r1 = "El vehiculo debe recibir mantenimiento"

        elif (n1 > 2013) & ( n2 < 10000):
            print("El vehiculo esta en optimas condiciones")
            file.write("El vehiculo esta en optimas condiciones"+os.linesep)
            r1 = "El vehiculo esta en optimas condiciones"

        else:
            print("Mecánico")
            file.write("Mecánico"+os.linesep)
            r1 = "Mecánico"

        
        print("")
        file.close()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tarea_preparatoria(Programa_ejecutado, Resultado) VALUES(%s,%s);",("P14:Clasificar_Taxis", r1))
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