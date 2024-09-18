import random  #De París Montenegro

print("*** DEMUESTRA TU DICHA ***")
print("SÍ EL JUEGO GENERA EL NUMERO 6, GANAS")

input("presione ENTER PARA COMENNZAR")

valorObtenido=random.randint(1,6)

print(f"obtuviste un {valorObtenido}")

if valorObtenido == 6:
    print("Felicidades Ganaste!!!!")
    print("Eres dichoso!!")
else:
    print("Lo siento perdiste")