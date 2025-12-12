# AI_input_output.py
# Este archivo muestra como interactuar con el usuario y archivos basicos.

# 1. Entrada de usuario (Input)
print("--- Entrada de Usuario ---")
# input() siempre devuelve un texto (string)
nombre = input("Por favor, introduce tu nombre: ")
print(f"Hola, {nombre}!")

# Si necesitas un numero, debes convertirlo
entrada_edad = input("Introduce tu edad: ")
# Es buena practica manejar posibles errores si el usuario no escribe un numero
try:
    edad = int(entrada_edad)
    print(f"El proximo ano tendras {edad + 1} anos.")
except ValueError:
    print("Eso no parece ser un numero valido.")

# 2. Escribir en un archivo
# 'w' significa modo escritura (write). Si el archivo no existe, lo crea.
print("\n--- Escribiendo en un archivo ---")
with open("AI_notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Esta es una linea de prueba.\n")
    archivo.write(f"Usuario: {nombre}\n")
    print("Se ha creado y escrito en 'AI_notas.txt'.")

# 3. Leer de un archivo
# 'r' significa modo lectura (read).
print("\n--- Leyendo del archivo ---")
try:
    with open("AI_notas.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
