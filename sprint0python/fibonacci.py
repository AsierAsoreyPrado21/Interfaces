def Fibonacci(Number):
    if(Number==0):
        return 0
    elif(Number==1):
        return 1
    else:
        return (Fibonacci(Number-2)+Fibonacci(Number-1)) 
n=int(input("Valor de n (numero de veces que realiza la funcion): "))
print("Secuencia Fibonacci :"+str (Fibonacci(n)))

