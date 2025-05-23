altura = int(input("De que altura desea el arbol: "))
inicio = 1


while inicio <=altura:
    espacio = " " * (altura - inicio)
    asterisco = '*' * (2* inicio -1)
    print (espacio + asterisco)
    inicio +=1

