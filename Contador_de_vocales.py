
while True:
    pal1 = (input("Introduzca una palabra:  "))

    def contar_vocales(frase):
        vocales = 'aeiouAEIOUáéíóúÁÉÍÓÚ'

        return [c for c in frase if c in vocales]  #retornamos caracter por caracter y verificamos si estan incluidos en la lista vocales
    print(contar_vocales(pal1))
    print("La palabra", pal1, "tiene", len(contar_vocales(pal1)), "vocales")  