
from multiprocessing import Event


n1 = 0
n2 = 100
x1 = 0
print("Los limites seleccionados son:", "[", n1,",", n2, "]")
for i in range(n1,n2+1):
    if i%2==1:
        print(i, end=" ")
        x1 = x1 +1
print("")
print("La cantidad de numeros impares es: ")
print(x1)
