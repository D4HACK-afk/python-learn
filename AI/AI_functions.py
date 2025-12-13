# AI_functions.py
# Este archivo muestra como definir y usar funciones.
# Las funciones son bloques de codigo reutilizables.

# 1. Definicion basica
def saludar():
    """Esta funcion imprime un saludo simple."""
    print("Hola! Bienvenido al curso de Python.")

print("--- Llamando a una funcion simple ---")
saludar() # Llamada a la funcion

# 2. Funciones con parametros
def saludar_persona(nombre):
    """Saluda a la persona especificada."""
    print(f"Hola, {nombre}!")

print("\n--- Funcion con parametros ---")
saludar_persona("Maria")
saludar_persona("Carlos")

# 3. Funciones que retornan valores
def sumar(a, b):
    """Retorna la suma de dos numeros."""
    resultado = a + b
    return resultado

print("\n--- Funcion con retorno ---")
suma_total = sumar(5, 7)
print(f"La suma de 5 y 7 es: {suma_total}")

# 4. Parametros por defecto
def presentar_mascota(nombre_mascota, animal="perro"):
    """Si no se especifica el animal, se asume que es un perro."""
    print(f"Tengo un {animal} llamado {nombre_mascota}.")

print("\n--- Parametros por defecto ---")
presentar_mascota("Max") # Usa el valor por defecto (perro)
presentar_mascota("Michi", "gato") # Sobrescribe el valor por defecto

# 5. Argumentos arbitrarios (*args)
# Cuando no sabes cuantos argumentos te pasaran.
def listar_alumnos(*nombres):
    print(f"Alumnos en la lista: {nombres}")
    for nombre in nombres:
        print(f"- {nombre}")

print("\n--- Argumentos arbitrarios ---")
listar_alumnos("Ana", "Pedro", "Luis", "Sofia")
