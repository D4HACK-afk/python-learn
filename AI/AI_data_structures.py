# AI_data_structures.py
# Este archivo cubre las estructuras de datos fundamentales: Listas, Tuplas, Sets y Diccionarios.

# 1. Listas (Lists)
# Son ordenadas y mutables (se pueden cambiar).
print("--- Listas ---")
frutas = ["manzana", "banana", "cereza"]
print(f"Lista original: {frutas}")

frutas.append("naranja") # Agregar al final
print(f"Despues de agregar: {frutas}")

frutas[1] = "mango" # Modificar un elemento
print(f"Despues de modificar el indice 1: {frutas}")

print(f"Primer elemento: {frutas[0]}")
print(f"Ultimo elemento: {frutas[-1]}")

# 2. Tuplas (Tuples)
# Son ordenadas e INMUTABLES (no se pueden cambiar despues de crear).
print("\n--- Tuplas ---")
colores = ("rojo", "verde", "azul")
print(f"Tupla de colores: {colores}")
# colores[0] = "amarillo" # Esto daria error!

# 3. Conjuntos (Sets)
# Son desordenados y NO permiten duplicados.
print("\n--- Conjuntos (Sets) ---")
numeros = {1, 2, 3, 3, 4, 4, 5}
print(f"Set de numeros (sin duplicados): {numeros}")
numeros.add(6)
print(f"Set actualizado: {numeros}")

# 4. Diccionarios (Dictionaries)
# Almacenan datos en pares clave:valor.
print("\n--- Diccionarios ---")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(f"Diccionario persona: {persona}")

print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")

persona["profesion"] = "Ingeniero" # Agregar nuevo par
print(f"Diccionario actualizado: {persona}")
