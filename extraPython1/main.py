# Ejercicio 1
def maxi(a, b):
    list = [a, b, c]
    return max(list)
a = 2
b = 4
print(max(a, b))
# Ejercicio2
def max_de_tres(a, b, c):
    list = [a, b, c]
    return max(list)
a = 2
b = 6
c = 1
print(max_de_tres(a, b, c))
# Ejercicio3
valor = "Domingo"
def longitud(valor):
    cont = 0
    while True:
        try:
            valor[cont]
            cont = cont + 1
        except IndexError:
            break
    return cont
print(longitud(valor))
#Ejercicio4
letra = input('Introduce una letra ')
def es_vocal(letra):
    if letra.casefold() in 'aeiou':
        print('Es una vocal')
    else:
        print('No es vocal')
es_vocal(letra)
#Ejercicio5
def suma(lista):
    suma=0
    for numeros in lista:
        suma=suma+numeros
    return suma
numeros=[1,5,9]
print(suma(numeros))
def suma(lista):
    multi=1
    for numeros in lista:
        multi=multi*numeros
    return multi
numeros=[1,5,9]
print(suma(numeros))
#Ejercicio6
def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

string = "HolaMundo"

print("original: ")
print(string)
print("Reverse: ")
print(reverse_string(string))
#Ejercicio7
palabra = str("reconocer")

if str(palabra) == str(palabra)[::-1]:
    print("Es Palindroma")
else:
    print("No es Palindroma")
#Ejercicio8
def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False
lista1=["casa"]
lista2=["pera"]
print(superposicion(lista1,lista2))
#Ejercicio9
def generar_n_caracteres(a,b):
    c = b
    for i in range(a):
        b = b + c
    return b
print(generar_n_caracteres(15,"a"))
#Ejercicio10
def procedimiento (histo):
    r="*"
    z=""
    i=0
    for i in range(len(histo)):
        z=z+r
        i+=1
    return z

print(procedimiento("casa"))
