from fibonacci import Fibonacci
from fibonacci2 import Fibonacci2
import time
op = input('Tu respuesta: ')
while True:

    if op == "a":
        number = int(input("Valor de n (numero de veces que realiza la funcion): "))
        print("Secuencia Fibonacci :"+str (Fibonacci(number)))
        start_time = time.time()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
        break
    elif op == "b":
        number = int(input("Valor de n (numero de veces que realiza la funcion): "))
        print("Secuencia Fibonacci :"+str (Fibonacci2(number)))
        start_time = time.time()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
        break
    else:
         op = input('Tu respuesta. Debe ser a o b: ')


