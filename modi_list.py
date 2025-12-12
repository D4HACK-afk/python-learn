#!/usr/bin/env python3
nombres = ["juan", "pablo", "daniel"]
edades = [21, 22, 23]
aprobado = [True, False, True]

    #aqui aprendemos a modificar listas con funciones
    
nombres.append("dani")
nombres.append("prueba de eliminacion")
nombres.insert(0, "juanito")
nombres.remove("prueba de eliminacion")

    #otra funcion es la .clear(), pero no la pongo debido a que esta elimina todo el contenido de una lista

print(nombres)  