# AI_drawing.py
# Este archivo muestra como crear dibujos simples usando la libreria 'turtle'.
# Es una forma muy divertida de aprender programacion grafica!

import turtle

# Crear una pantalla para dibujar
pantalla = turtle.Screen()
pantalla.title("Dibujando con Python y Turtle")
pantalla.bgcolor("white")

# Crear el "tortuga" (el pincel)
pincel = turtle.Turtle()
pincel.shape("turtle") # Forma de tortuga
pincel.color("blue")
pincel.speed(5) # Velocidad de dibujo (1-10)

print("--- Dibujando un Cuadrado ---")
# Dibujar un cuadrado
for _ in range(4):
    pincel.forward(100) # Avanzar 100 unidades
    pincel.right(90)    # Girar 90 grados a la derecha

# Mover el pincel a otra posicion sin dibujar
pincel.penup()
pincel.goto(-150, 0)
pincel.pendown()
pincel.color("red")

print("--- Dibujando una Estrella ---")
# Dibujar una estrella
for _ in range(5):
    pincel.forward(100)
    pincel.right(144) # 144 grados es el angulo para una estrella de 5 puntas

# Mover para hacer un espiral
pincel.penup()
pincel.home() # Volver al centro (0,0)
pincel.goto(0, -150)
pincel.pendown()
pincel.color("green")
pincel.speed(10) # Mas rapido

print("--- Dibujando un Espiral ---")
# Dibujar un espiral
for i in range(50):
    pincel.circle(i * 2) # Dibuja circulos cada vez mas grandes
    pincel.right(10)

print("Dibujo terminado! Haz clic en la ventana del dibujo para salir.")
# Mantener la ventana abierta hasta que el usuario haga clic
pantalla.exitonclick()
