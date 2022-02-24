
while True:
    pal1 = (input("Introduzca una palabra:  "))

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