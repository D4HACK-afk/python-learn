# AI_loops.py
# Este archivo muestra como usar bucles (ciclos) para repetir codigo.

# 1. Bucle For (Para cada...)
# Se usa para iterar sobre una secuencia (como una lista o un rango de numeros).

print("--- Bucle For con rangos ---")
# Imprimir numeros del 0 al 4
# range(5) genera numeros: 0, 1, 2, 3, 4 (el 5 no se incluye)
for i in range(5):
    print(f"Numero: {i}")

print("\n--- Bucle For con una lista ---")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

# 2. Bucle While (Mientas...)
# Ejecuta un bloque de codigo mientras una condicion sea Verdadera.

print("\n--- Bucle While ---")
contador = 1
while contador <= 3:
    print(f"Contando: {contador}")
    contador += 1 # Importante: aumentar el contador para evitar un bucle infinito

# 3. Break y Continue
# break: Detiene el bucle por completo.
# continue: Salta a la siguiente iteracion del bucle.

print("\n--- Break ---")
for numero in range(1, 10):
    if numero == 5:
        print("Se encontro el 5, rompiendo el ciclo!")
        break # Sale del for
    print(numero)

print("\n--- Continue ---")
for numero in range(1, 6):
    if numero == 3:
        print("Saltando el 3...")
        continue # Salta el print de abajo y vuelve al inicio del for
    print(f"Numero procesado: {numero}")
