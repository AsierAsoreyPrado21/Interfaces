from fibonacci import Fibonacci
from fibonacci2 import Fibonacci2
while True:
    op = input('Tu respuesta: ')
    if op == "a":
        number = int(input("Valor de n (numero de veces que realiza la funcion): "))
        print("Secuencia Fibonacci :"+str (Fibonacci(number)))
        break
    elif op == "b":
        number = int(input("Valor de n (numero de veces que realiza la funcion): "))
        print("Secuencia Fibonacci :"+str (Fibonacci2(number)))
        break
    else:
         op = input('Tu respuesta. Debe ser a o b: ')
