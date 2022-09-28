import random
choices = [1, 2, 3]
c=0
puntos = 0
while c<2:
	choice = random.choice(choices)

	if choice == 1:
		print("Que día es hoy?")
		print("a:Lunes")
		print("b:Martes")
		print("c:Miercoles")
		opcion = input('Respuesta: ')
		if opcion == "b":
			print("Respuesta correcta,+10 puntos")
			puntos = puntos + 10
		else:
			print("Respuesta incorrecta,-5 puntos")
			puntos = puntos - 5
	elif choice == 2:
		print("En que mes estamos?")
		print("a:Agosto")
		print("b:Diciembre")
		print("c:Septiembre")
		opcion2 = input('Respuesta: ')
		if opcion2 == "c":
			print("Respuesta correcta,+10 puntos")
			puntos = puntos + 10
		else:
			print("Respuesta incorrecta,-5 puntos")
			puntos = puntos - 5
	elif choice == 3:
		print("En que año estamos?")
		print("a:2022")
		print("b:2021")
		print("c:2023")
		opcion3 = input('Respuesta: ')
		if opcion3 == "a":
			print("Respuesta correcta,+10 puntos")
			puntos = puntos + 10
		else:
			print("Respuesta incorrecta,-5 puntos")
			puntos = puntos - 5
	c+=1
print("Puntuacion total: "+str(puntos))