# AI_control_flow.py
# Este archivo explicara el ujo de control con sentencias if, elif y else.

# Vamos a evaluar la calificacion de un estudiante.
calificacion = 85

print(f"La calificacion es: {calificacion}")

# 1. Estructura basica if (si)
if calificacion >= 60:
    print("El estudiante aprobo.") # Esto se ejecuta si la condicion es Verdadera

# 2. Estructura if...else (si...sino)
edad = 16
print(f"\nEdad: {edad}")
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# 3. Estructura if...elif...else (si...si no,si...sino)
# Permite verificar multiples condiciones en orden.
temperatura = 25
print(f"\nTemperatura actual: {temperatura} grados")

if temperatura > 30:
    print("Hace mucho calor.")
elif temperatura > 20:
    print("El clima es agradable.")
elif temperatura > 10:
    print("Hace un poco de frio.")
else:
    print("Hace mucho frio.")

# 4. Operadores Logicos (and, or, not)
# and: Ambas condiciones deben ser verdaderas
tienes_boleto = True
tienes_identificacion = True

print("\n--- Operadores Logicos ---")
if tienes_boleto and tienes_identificacion:
    print("Puedes entrar al evento (and).")
else:
    print("No puedes entrar (and).")

# or: Al menos una condicion debe ser verdadera
es_fin_de_semana = False
es_feriado = True

if es_fin_de_semana or es_feriado:
    print("Hoy no se trabaja (or).")
else:
    print("Hoy se trabaja (or).")

# not: Invierte el valor de verdad (Verdadero -> Falso, Falso -> Verdadero)
esta_lloviendo = False
if not esta_lloviendo:
    print("Podemos salir al parque (not).")
