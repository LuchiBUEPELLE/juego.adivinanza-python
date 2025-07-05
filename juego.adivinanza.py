import random

numero_secreto = random.randint(1, 101)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("¡Bienvenido al juego de adivinanza!")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("Introduce un número entre 1 y 100:  ") 
    numero = int(entrada)
    
    if numero is numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor. Inténtalo de nuevo.")
    else:
        print("El número es menor. Inténtalo de nuevo.")
    
    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print("GAME OVER! Lo siento, has agotado tus intentos.")