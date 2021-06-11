import random
import time
nombre= input("¿Cómo te llamas?")
print("Hola "+ nombre +". Es hora de jugar al ahorcado")
print(" ")
time.sleep(1)
print("Comienza adivinar")
print(" ")
time.sleep(0.5)

palabraAleatoria=random.choice(["alfa","nieve","secuencia","algoritmo","noticias","hernando","castillo", "terrorismo"])
tuPalabra=''
vidas=5

while vidas>0:
    fallas=0
    for letra in palabraAleatoria:
        if letra in tuPalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1

    if fallas==0:
        print(" Felicidades, ganaste")
        break

    tuletra=input("\n Introduce una letra: ")
    tuPalabra+=tuletra

    if tuletra not in palabraAleatoria:
        vidas -=1
        print(" ")
        print("Equivocado")
        print("Tu tienes "+ str(vidas) + " vidas")
    if vidas ==0:
        print("perdiste")

else:
    print(" ")
    print("Gracias por participar")         