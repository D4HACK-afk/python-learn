#!/usr/bin/env python3
Alumnos = ("Juan", "Maria", "jose")
edades = (25, 30, 20)
aprovados = (True, False, False)

#Asi es como se le le puede sumar o multiplicar depende de lo que quieras hacer a una variable con un valor no se 
#modifica directamente se anade
EdadJuan = (edades[0])
EdadJuan += 2
#asi es como se le puede sumar a una variable con un valor no se modifica directamente se anade, ejemplo, no queremos modificar la lista original
#pero si queremos agregar un nuevo valor a la lista original, y para eso creamos una lista ficticia que se basa en el contenido de la original
#por eso el contenido de la original no se modifica como en las listas comunes, esto es una principal diferencia entre las tuplas y las listas
add_Alumnos = Alumnos 
add_Alumnos += ("Pablo")

print (Alumnos)
print (EdadJuan)
print (add_Alumnos [3])