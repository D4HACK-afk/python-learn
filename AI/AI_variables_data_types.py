# AI_variables_data_types.py
# Este archivo explicara los tipos de datos basicos y variables en Python
# Las variables son contenedores para almacenar valores de datos.

# 1. Asignacion de Variables
# En Python, no necesitas declarar el tipo de variable.
nombre = "Juan"        # Cadena de texto (String)
edad = 25              # Entero (Integer)
altura = 1.75          # Decimal (Float)
es_estudiante = True   # Booleano (Boolean) - Verdadero o Falso

print("--- Valores de las Variables ---")
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("Es estudiante:", es_estudiante)

# 2. Tipos de Datos
# Puedes verificar el tipo de cualquier objeto usando la funcion type()
print("\n--- Tipos de Datos ---")
print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'edad':", type(edad))
print("Tipo de 'altura':", type(altura))
print("Tipo de 'es_estudiante':", type(es_estudiante))

# 3. Conversion de Tipos (Casting)
# A veces necesitas convertir un tipo de dato a otro.
print("\n--- Conversion de Tipos ---")
edad_texto = str(edad)  # Convierte int a str
print("Edad como texto:", edad_texto, "| Tipo:", type(edad_texto))

altura_entero = int(altura) # Convierte float a int (pierde decimales)
print("Altura como entero:", altura_entero, "| Tipo:", type(altura_entero))

numero_str = "100"
numero_int = int(numero_str) # Convierte str a int
print("String '100' mas 50:", numero_int + 50)

# 4. Concatenacion
# Uniendo cadenas de texto
saludo = "Hola " + nombre + ", tienes " + str(edad) + " años."
print("\n--- Concatenacion ---")
print(saludo)

# Tambien se pueden usar "f-strings" (mas moderno y recomendado)
saludo_f = f"Hola {nombre}, tienes {edad} años (usando f-string)."
print(saludo_f)
