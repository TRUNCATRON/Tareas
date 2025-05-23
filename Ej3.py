contra = "RafaMan"

intento = ""
intentos = 0
while intento != contra:
    intento = input("Introduzca la contraseña: ")
    intentos +=1

print(f"Correcto! El número de intentos hecho fue: {intentos}")

