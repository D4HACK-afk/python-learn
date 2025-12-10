#!/usr/bin/env python3

edad = int(input("introduce tu edad: "))

nombre = str(input("introduce tu nombre: "))

print("tu nombre es " + nombre + " y" + " tienes " + str(edad) + " anos.")

## variables que guardan el valor que asigne el usuario (input) en bash, seria el read
## si te aparece un error de sintaxis es por que al momento de imprimir el entero.
# debes hacer la conversion de ese int a str en el propio print