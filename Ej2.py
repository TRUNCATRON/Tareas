num = int(input("Introduzca un numero entero positivo: "))

if num <= 0:
    print("Numero no valido")
else:
    impar = 1
    resultado = ''
   
while impar <= num:
    resultado += str(impar)
    if impar +2 <=num:
        resultado += ","
    impar += 2

print(f"Numeros impares: {resultado}")