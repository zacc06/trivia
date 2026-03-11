"""# trivia
# es juego de triviaaa!
# Challenge: Mini Trivia en Python

## Debes crear:
Un archivo llamado `trivia.py`

## Tu programa debe:
- pedir el nombre del jugador
- mostrar una bienvenida
- hacer 4 preguntas
- sumar 1 punto por cada respuesta correcta
- mostrar el nombre y el puntaje final

## Resultado final
- si `puntaje == 4` → **Excelente**
- si `puntaje >= 2` → **Muy bien**
- si no → **Puedes mejorar**

## Recuerda
- trabaja paso a paso
- no hace falta terminar perfecto
- usa Git durante el proceso
- haz varios commits pequeños"""
print("····BIENVENIDO AL JUEGO DE TRIVIA····")
nom_jug=input("Ingrese su nombre: ")
preg_1=int(input("¿Cuantas patas tienen los perros?"))
preg_2=int(input("¿Cuanto es 9 x 9?"))
preg_3=input("¿Las vacas son mamiferos o oviparos?")
preg_4=input("¿Como se llama el femenino de los caballos?")
puntaje= 0

while puntaje>0:
    puntaje =+ 1
    if preg_1 == "4":
        print("**Excelente**")
        
    