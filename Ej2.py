def dec_bin(dec):
    bin = ""
    if dec == 0:
        return "0"
    while dec > 0:
        bin = str(dec %2 ) + bin            
        dec //=2

    return bin


resultado = dec_bin(85585)

print(resultado)


def bina_deci(bina):
    bina = str(bina)
    deci = 0
    pot = len(bina) - 1  
    for digito in bina:
        deci += int(digito) * (2 ** pot)
        pot -= 1
    return deci

res_2 = bina_deci(1010)
print(res_2)